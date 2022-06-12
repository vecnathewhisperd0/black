"""
Simple formatting on strings. Further string formatting code is in trans.py.
"""

import re
import sys
from functools import lru_cache
from typing import List, Pattern, Iterator, Tuple

if sys.version_info < (3, 8):
    from typing_extensions import Final
else:
    from typing import Final


STRING_PREFIX_CHARS: Final = "furbFURB"  # All possible string prefix characters.
STRING_PREFIX_RE: Final = re.compile(
    r"^([" + STRING_PREFIX_CHARS + r"]*)(.*)$", re.DOTALL
)
FIRST_NON_WHITESPACE_RE: Final = re.compile(r"\s*\t+\s*(\S)")


def sub_twice(regex: Pattern[str], replacement: str, original: str) -> str:
    """Replace `regex` with `replacement` twice on `original`.

    This is used by string normalization to perform replaces on
    overlapping matches.
    """
    return regex.sub(replacement, regex.sub(replacement, original))


def has_triple_quotes(string: str) -> bool:
    """
    Returns:
        True iff @string starts with three quotation characters.
    """
    raw_string = string.lstrip(STRING_PREFIX_CHARS)
    return raw_string[:3] in {'"""', "'''"}


def lines_with_leading_tabs_expanded(s: str) -> List[str]:
    """
    Splits string into lines and expands only leading tabs (following the normal
    Python rules)
    """
    lines = []
    for line in s.splitlines():
        # Find the index of the first non-whitespace character after a string of
        # whitespace that includes at least one tab
        match = FIRST_NON_WHITESPACE_RE.match(line)
        if match:
            first_non_whitespace_idx = match.start(1)

            lines.append(
                line[:first_non_whitespace_idx].expandtabs()
                + line[first_non_whitespace_idx:]
            )
        else:
            lines.append(line)
    return lines


def fix_docstring(docstring: str, prefix: str) -> str:
    # https://www.python.org/dev/peps/pep-0257/#handling-docstring-indentation
    if not docstring:
        return ""
    lines = lines_with_leading_tabs_expanded(docstring)
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxsize
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxsize:
        last_line_idx = len(lines) - 2
        for i, line in enumerate(lines[1:]):
            stripped_line = line[indent:].rstrip()
            if stripped_line or i == last_line_idx:
                trimmed.append(prefix + stripped_line)
            else:
                trimmed.append("")
    return "\n".join(trimmed)


def get_string_prefix(string: str) -> str:
    """
    Pre-conditions:
        * assert_is_leaf_string(@string)

    Returns:
        @string's prefix (e.g. '', 'r', 'f', or 'rf').
    """
    assert_is_leaf_string(string)

    prefix = ""
    prefix_idx = 0
    while string[prefix_idx] in STRING_PREFIX_CHARS:
        prefix += string[prefix_idx]
        prefix_idx += 1

    return prefix


def assert_is_leaf_string(string: str) -> None:
    """
    Checks the pre-condition that @string has the format that you would expect
    of `leaf.value` where `leaf` is some Leaf such that `leaf.type ==
    token.STRING`. A more precise description of the pre-conditions that are
    checked are listed below.

    Pre-conditions:
        * @string starts with either ', ", <prefix>', or <prefix>" where
        `set(<prefix>)` is some subset of `set(STRING_PREFIX_CHARS)`.
        * @string ends with a quote character (' or ").

    Raises:
        AssertionError(...) if the pre-conditions listed above are not
        satisfied.
    """
    dquote_idx = string.find('"')
    squote_idx = string.find("'")
    if -1 in [dquote_idx, squote_idx]:
        quote_idx = max(dquote_idx, squote_idx)
    else:
        quote_idx = min(squote_idx, dquote_idx)

    assert (
        0 <= quote_idx < len(string) - 1
    ), f"{string!r} is missing a starting quote character (' or \")."
    assert string[-1] in (
        "'",
        '"',
    ), f"{string!r} is missing an ending quote character (' or \")."
    assert set(string[:quote_idx]).issubset(
        set(STRING_PREFIX_CHARS)
    ), f"{set(string[:quote_idx])} is NOT a subset of {set(STRING_PREFIX_CHARS)}."


def normalize_string_prefix(s: str) -> str:
    """Make all string prefixes lowercase."""
    match = STRING_PREFIX_RE.match(s)
    assert match is not None, f"failed to match string {s!r}"
    orig_prefix = match.group(1)
    new_prefix = (
        orig_prefix.replace("F", "f")
        .replace("B", "b")
        .replace("U", "")
        .replace("u", "")
    )

    # Python syntax guarantees max 2 prefixes and that one of them is "r"
    if len(new_prefix) == 2 and "r" != new_prefix[0].lower():
        new_prefix = new_prefix[::-1]
    return f"{new_prefix}{match.group(2)}"


# Re(gex) does actually cache patterns internally but this still improves
# performance on a long list literal of strings by 5-9% since lru_cache's
# caching overhead is much lower.
@lru_cache(maxsize=64)
def _cached_compile(pattern: str) -> Pattern[str]:
    return re.compile(pattern)


def normalize_string_quotes(s: str) -> str:
    """Prefer double quotes but only if it doesn't cause more escaping.

    Adds or removes backslashes as appropriate. Doesn't parse and fix
    strings nested in f-strings.
    """
    value = s.lstrip(STRING_PREFIX_CHARS)
    if value[:3] == '"""':
        return s

    elif value[:3] == "'''":
        orig_quote = "'''"
        new_quote = '"""'
    elif value[0] == '"':
        orig_quote = '"'
        new_quote = "'"
    else:
        orig_quote = "'"
        new_quote = '"'
    first_quote_pos = s.find(orig_quote)
    if first_quote_pos == -1:
        return s  # There's an internal error

    prefix = s[:first_quote_pos]
    unescaped_new_quote = _cached_compile(rf"(([^\\]|^)(\\\\)*){new_quote}")
    escaped_new_quote = _cached_compile(rf"([^\\]|^)\\((?:\\\\)*){new_quote}")
    escaped_orig_quote = _cached_compile(rf"([^\\]|^)\\((?:\\\\)*){orig_quote}")
    body = s[first_quote_pos + len(orig_quote) : -len(orig_quote)]
    if "r" in prefix.casefold():
        if unescaped_new_quote.search(body):
            # There's at least one unescaped new_quote in this raw string
            # so converting is impossible
            return s

        # Do not introduce or remove backslashes in raw strings
        new_body = body
    else:
        # remove unnecessary escapes
        new_body = sub_twice(escaped_new_quote, rf"\1\2{new_quote}", body)
        if body != new_body:
            # Consider the string without unnecessary escapes as the original
            body = new_body
            s = f"{prefix}{orig_quote}{body}{orig_quote}"
        new_body = sub_twice(escaped_orig_quote, rf"\1\2{orig_quote}", new_body)
        new_body = sub_twice(unescaped_new_quote, rf"\1\\{new_quote}", new_body)
    if "f" in prefix.casefold():
        matches = re.findall(
            r"""
            (?:(?<!\{)|^)\{  # start of the string or a non-{ followed by a single {
                ([^{].*?)  # contents of the brackets except if begins with {{
            \}(?:(?!\})|$)  # A } followed by end of the string or a non-}
            """,
            new_body,
            re.VERBOSE,
        )
        for m in matches:
            if "\\" in str(m):
                # Do not introduce backslashes in interpolated expressions
                return s

    if new_quote == '"""' and new_body[-1:] == '"':
        # edge case:
        new_body = new_body[:-1] + '\\"'
    orig_escape_count = body.count("\\")
    new_escape_count = new_body.count("\\")
    if new_escape_count > orig_escape_count:
        return s  # Do not introduce more escaping

    if new_escape_count == orig_escape_count and orig_quote == '"':
        return s  # Prefer double quotes

    return f"{prefix}{new_quote}{new_body}{new_quote}"


def iterate_f_string(s: str) -> Iterator[Tuple[int, int]]:
    """
    Yields spans corresponding to expressions in a given f-string.
    Spans are half-open ranges (left inclusive, right exclusive).
    Assumes the input string is a valid f-string, but will not crash if the input
    string is invalid.
    """
    stack: List[int] = []  # our curly paren stack
    i = 0
    while i < len(s):
        if s[i] == "{":
            # if we're in a string part of the f-string, ignore escaped curly braces
            if not stack and i + 1 < len(s) and s[i + 1] == "{":
                i += 2
                continue
            stack.append(i)
            i += 1
            continue

        if s[i] == "}":
            if not stack:
                i += 1
                continue
            j = stack.pop()
            # we've made it back out of the expression! yield the span
            if not stack:
                yield (j, i + 1)
            i += 1
            continue

        # if we're in an expression part of the f-string, fast forward through strings
        # note that backslashes are not legal in the expression portion of f-strings
        if stack:
            delim = None
            if s[i : i + 3] in ("'''", '"""'):
                delim = s[i : i + 3]
            elif s[i] in ("'", '"'):
                delim = s[i]
            if delim:
                i += len(delim)
                while i < len(s) and s[i : i + len(delim)] != delim:
                    i += 1
                i += len(delim)
                continue
        i += 1


def fstring_contains_expr(s: str) -> bool:
    """Checks if a given f-string contains an actual f-expression."""
    return any(iterate_f_string(s))


def normalize_f_string(string: str, prefix: str) -> str:
    """
    Pre-Conditions:
        * assert_is_leaf_string(@string)

    Returns:
        * If @string is an f-string that contains no f-expressions, we
        return a string identical to @string except that the 'f' prefix
        has been stripped and all double braces (i.e. '{{' or '}}') have
        been normalized (i.e. turned into '{' or '}').
            OR
        * Otherwise, we return @string.
    """
    assert_is_leaf_string(string)

    if "f" in prefix and not fstring_contains_expr(string):
        new_prefix = prefix.replace("f", "")

        temp = string[len(prefix) :]
        temp = re.sub(r"\{\{", "{", temp)
        temp = re.sub(r"\}\}", "}", temp)
        new_string = temp

        return f"{new_prefix}{new_string}"
    else:
        return string
