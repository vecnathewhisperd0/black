![Black Logo](https://raw.githubusercontent.com/psf/black/master/docs/_static/logo2-readme.png)

<h2 align="center">The Uncompromising Code Formatter</h2>

<p align="center">
<a href="https://travis-ci.com/psf/black"><img alt="Build Status" src="https://travis-ci.com/psf/black.svg?branch=master"></a>
<a href="https://github.com/psf/black/actions"><img alt="Actions Status" src="https://github.com/psf/black/workflows/Test/badge.svg"></a>
<a href="https://black.readthedocs.io/en/stable/?badge=stable"><img alt="Documentation Status" src="https://readthedocs.org/projects/black/badge/?version=stable"></a>
<a href="https://coveralls.io/github/psf/black?branch=master"><img alt="Coverage Status" src="https://coveralls.io/repos/github/psf/black/badge.svg?branch=master"></a>
<a href="https://github.com/psf/black/blob/master/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://pypi.org/project/black/"><img alt="PyPI" src="https://img.shields.io/pypi/v/black"></a>
<a href="https://pepy.tech/project/black"><img alt="Downloads" src="https://pepy.tech/badge/black"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

> “Any color you like.”

_Black_ is the uncompromising Python code formatter. By using it, you agree to cede
control over minutiae of hand-formatting. In return, _Black_ gives you speed,
determinism, and freedom from `pycodestyle` nagging about formatting. You will save time
and mental energy for more important matters.

Blackened code looks the same regardless of the project you're reading. Formatting
becomes transparent after a while and you can focus on the content instead.

_Black_ makes code review faster by producing the smallest diffs possible.

Try it out now using the [Black Playground](https://black.now.sh). Watch the
[PyCon 2019 talk](https://youtu.be/esZLCuWs_2Y) to learn more.

---

_Contents:_ **[Installation and usage](#installation-and-usage)** |
**[Code style](#the-black-code-style)** | **[pyproject.toml](#pyprojecttoml)** |
**[Editor integration](#editor-integration)** | **[blackd](#blackd)** |
**[Version control integration](#version-control-integration)** |
**[Ignoring unmodified files](#ignoring-unmodified-files)** | **[Used by](#used-by)** |
**[Testimonials](#testimonials)** | **[Show your style](#show-your-style)** |
**[Contributing](#contributing-to-black)** | **[Change Log](#change-log)** |
**[Authors](#authors)**

---

## Installation and usage

### Installation

_Black_ can be installed by running `pip install black`. It requires Python 3.6.0+ to
run but you can reformat Python 2 code with it, too.

### Usage

To get started right away with sensible defaults:

```
black {source_file_or_directory}
```

### Command line options

_Black_ doesn't provide many options. You can list them by running `black --help`:

```text
black [OPTIONS] [SRC]...

Options:
  -c, --code TEXT                 Format the code passed in as a string.
  -l, --line-length INTEGER       How many characters per line to allow.
                                  [default: 88]
  -t, --target-version [py27|py33|py34|py35|py36|py37|py38]
                                  Python versions that should be supported by
                                  Black's output. [default: per-file auto-
                                  detection]
  --py36                          Allow using Python 3.6-only syntax on all
                                  input files.  This will put trailing commas
                                  in function signatures and calls also after
                                  *args and **kwargs. Deprecated; use
                                  --target-version instead. [default: per-file
                                  auto-detection]
  --pyi                           Format all input files like typing stubs
                                  regardless of file extension (useful when
                                  piping source on standard input).
  -S, --skip-string-normalization
                                  Don't normalize string quotes or prefixes.
  --check                         Don't write the files back, just return the
                                  status.  Return code 0 means nothing would
                                  change.  Return code 1 means some files
                                  would be reformatted.  Return code 123 means
                                  there was an internal error.
  --diff                          Don't write the files back, just output a
                                  diff for each file on stdout.
  --fast / --safe                 If --fast given, skip temporary sanity
                                  checks. [default: --safe]
  --include TEXT                  A regular expression that matches files and
                                  directories that should be included on
                                  recursive searches.  An empty value means
                                  all files are included regardless of the
                                  name.  Use forward slashes for directories
                                  on all platforms (Windows, too).  Exclusions
                                  are calculated first, inclusions later.
                                  [default: \.pyi?$]
  --exclude TEXT                  A regular expression that matches files and
                                  directories that should be excluded on
                                  recursive searches.  An empty value means no
                                  paths are excluded. Use forward slashes for
                                  directories on all platforms (Windows, too).
                                  Exclusions are calculated first, inclusions
                                  later.  [default: /(\.eggs|\.git|\.hg|\.mypy
                                  _cache|\.nox|\.tox|\.venv|_build|buck-
                                  out|build|dist)/]
  -q, --quiet                     Don't emit non-error messages to stderr.
                                  Errors are still emitted, silence those with
                                  2>/dev/null.
  -v, --verbose                   Also emit messages to stderr about files
                                  that were not changed or were ignored due to
                                  --exclude=.
  --version                       Show the version and exit.
  --config PATH                   Read configuration from PATH.
  -h, --help                      Show this message and exit.
```

_Black_ is a well-behaved Unix-style command-line tool:

- it does nothing if no sources are passed to it;
- it will read from standard input and write to standard output if `-` is used as the
  filename;
- it only outputs messages to users on standard error;
- exits with code 0 unless an internal error occurred (or `--check` was used).

### NOTE: This is a beta product

_Black_ is already [successfully used](#used-by) by many projects, small and big. It
also sports a decent test suite. However, it is still very new. Things will probably be
wonky for a while. This is made explicit by the "Beta" trove classifier, as well as by
the "b" in the version number. What this means for you is that **until the formatter
becomes stable, you should expect some formatting to change in the future**. That being
said, no drastic stylistic changes are planned, mostly responses to bug reports.

Also, as a temporary safety measure, _Black_ will check that the reformatted code still
produces a valid AST that is equivalent to the original. This slows it down. If you're
feeling confident, use `--fast`.

## The _Black_ code style

_Black_ reformats entire files in place. It is not configurable. It doesn't take
previous formatting into account. It doesn't reformat blocks that start with
`# fmt: off` and end with `# fmt: on`. `# fmt: on/off` have to be on the same level of
indentation. It also recognizes [YAPF](https://github.com/google/yapf)'s block comments
to the same effect, as a courtesy for straddling code.

### How _Black_ wraps lines

_Black_ ignores previous formatting and applies uniform horizontal and vertical
whitespace to your code. The rules for horizontal whitespace can be summarized as: do
whatever makes `pycodestyle` happy. The coding style used by _Black_ can be viewed as a
strict subset of PEP 8.

As for vertical whitespace, _Black_ tries to render one full expression or simple
statement per line. If this fits the allotted line length, great.

```py3
# in:

j = [1,
     2,
     3
]

# out:

j = [1, 2, 3]
```

If not, _Black_ will look at the contents of the first outer matching brackets and put
that in a separate indented line.

```py3
# in:

ImportantClass.important_method(exc, limit, lookup_lines, capture_locals, extra_argument)

# out:

ImportantClass.important_method(
    exc, limit, lookup_lines, capture_locals, extra_argument
)
```

If that still doesn't fit the bill, it will decompose the internal expression further
using the same rule, indenting matching brackets every time. If the contents of the
matching brackets pair are comma-separated (like an argument list, or a dict literal,
and so on) then _Black_ will first try to keep them on the same line with the matching
brackets. If that doesn't work, it will put all of them in separate lines.

```py3
# in:

def very_important_function(template: str, *variables, file: os.PathLike, engine: str, header: bool = True, debug: bool = False):
    """Applies `variables` to the `template` and writes to `file`."""
    with open(file, 'w') as f:
        ...

# out:

def very_important_function(
    template: str,
    *variables,
    file: os.PathLike,
    engine: str,
    header: bool = True,
    debug: bool = False,
):
    """Applies `variables` to the `template` and writes to `file`."""
    with open(file, "w") as f:
        ...
```

You might have noticed that closing brackets are always dedented and that a trailing
comma is always added. Such formatting produces smaller diffs; when you add or remove an
element, it's always just one line. Also, having the closing bracket dedented provides a
clear delimiter between two distinct sections of the code that otherwise share the same
indentation level (like the arguments list and the docstring in the example above).

If a data structure literal (tuple, list, set, dict) or a line of "from" imports cannot
fit in the allotted length, it's always split into one element per line. This minimizes
diffs as well as enables readers of code to find which commit introduced a particular
entry. This also makes _Black_ compatible with [isort](https://pypi.org/p/isort/) with
the following configuration.

<details>
<summary>A compatible `.isort.cfg`</summary>

```
[settings]
multi_line_output=3
include_trailing_comma=True
force_grid_wrap=0
use_parentheses=True
line_length=88
```

The equivalent command line is:

```
$ isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=88 [ file.py ]
```

</details>

### Line length

You probably noticed the peculiar default line length. _Black_ defaults to 88 characters
per line, which happens to be 10% over 80. This number was found to produce
significantly shorter files than sticking with 80 (the most popular), or even 79 (used
by the standard library). In general,
[90-ish seems like the wise choice](https://youtu.be/wf-BqAjZb8M?t=260).

If you're paid by the line of code you write, you can pass `--line-length` with a lower
number. _Black_ will try to respect that. However, sometimes it won't be able to without
breaking other rules. In those rare cases, auto-formatted code will exceed your allotted
limit.

You can also increase it, but remember that people with sight disabilities find it
harder to work with line lengths exceeding 100 characters. It also adversely affects
side-by-side diff review on typical screen resolutions. Long lines also make it harder
to present code neatly in documentation or talk slides.

If you're using Flake8, you can bump `max-line-length` to 88 and forget about it.
Alternatively, use [Bugbear](https://github.com/PyCQA/flake8-bugbear)'s B950 warning
instead of E501 and keep the max line length at 80 which you are probably already using.
You'd do it like this:

```ini
[flake8]
max-line-length = 80
...
select = C,E,F,W,B,B950
ignore = E203, E501, W503
```

You'll find _Black_'s own .flake8 config file is configured like this. Explanation of
why W503 and E203 are disabled can be found further in this documentation. And if you're
curious about the reasoning behind B950,
[Bugbear's documentation](https://github.com/PyCQA/flake8-bugbear#opinionated-warnings)
explains it. The tl;dr is "it's like highway speed limits, we won't bother you if you
overdo it by a few km/h".

**If you're looking for a minimal, black-compatible flake8 configuration:**

```ini
[flake8]
max-line-length = 88
extend-ignore = E203
```

### Empty lines

_Black_ avoids spurious vertical whitespace. This is in the spirit of PEP 8 which says
that in-function vertical whitespace should only be used sparingly.

_Black_ will allow single empty lines inside functions, and single and double empty
lines on module level left by the original editors, except when they're within
parenthesized expressions. Since such expressions are always reformatted to fit minimal
space, this whitespace is lost.

It will also insert proper spacing before and after function definitions. It's one line
before and after inner functions and two lines before and after module-level functions
and classes. _Black_ will not put empty lines between function/class definitions and
standalone comments that immediately precede the given function/class.

_Black_ will enforce single empty lines between a class-level docstring and the first
following field or method. This conforms to
[PEP 257](https://www.python.org/dev/peps/pep-0257/#multi-line-docstrings).

_Black_ won't insert empty lines after function docstrings unless that empty line is
required due to an inner function starting immediately after.

### Trailing commas

_Black_ will add trailing commas to expressions that are split by comma where each
element is on its own line. This includes function signatures.

Unnecessary trailing commas are removed if an expression fits in one line. This makes it
1% more likely that your line won't exceed the allotted line length limit. Moreover, in
this scenario, if you added another argument to your call, you'd probably fit it in the
same line anyway. That doesn't make diffs any larger.

One exception to removing trailing commas is tuple expressions with just one element. In
this case _Black_ won't touch the single trailing comma as this would unexpectedly
change the underlying data type. Note that this is also the case when commas are used
while indexing. This is a tuple in disguise: `numpy_array[3, ]`.

One exception to adding trailing commas is function signatures containing `*`, `*args`,
or `**kwargs`. In this case a trailing comma is only safe to use on Python 3.6. _Black_
will detect if your file is already 3.6+ only and use trailing commas in this situation.
If you wonder how it knows, it looks for f-strings and existing use of trailing commas
in function signatures that have stars in them. In other words, if you'd like a trailing
comma in this situation and _Black_ didn't recognize it was safe to do so, put it there
manually and _Black_ will keep it.

### Strings

_Black_ prefers double quotes (`"` and `"""`) over single quotes (`'` and `'''`). It
will replace the latter with the former as long as it does not result in more backslash
escapes than before.

_Black_ also standardizes string prefixes, making them always lowercase. On top of that,
if your code is already Python 3.6+ only or it's using the `unicode_literals` future
import, _Black_ will remove `u` from the string prefix as it is meaningless in those
scenarios.

The main reason to standardize on a single form of quotes is aesthetics. Having one kind
of quotes everywhere reduces reader distraction. It will also enable a future version of
_Black_ to merge consecutive string literals that ended up on the same line (see
[#26](https://github.com/psf/black/issues/26) for details).

Why settle on double quotes? They anticipate apostrophes in English text. They match the
docstring standard described in
[PEP 257](https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring). An empty
string in double quotes (`""`) is impossible to confuse with a one double-quote
regardless of fonts and syntax highlighting used. On top of this, double quotes for
strings are consistent with C which Python interacts a lot with.

On certain keyboard layouts like US English, typing single quotes is a bit easier than
double quotes. The latter requires use of the Shift key. My recommendation here is to
keep using whatever is faster to type and let _Black_ handle the transformation.

If you are adopting _Black_ in a large project with pre-existing string conventions
(like the popular
["single quotes for data, double quotes for human-readable strings"](https://stackoverflow.com/a/56190)),
you can pass `--skip-string-normalization` on the command line. This is meant as an
adoption helper, avoid using this for new projects.

### Numeric literals

_Black_ standardizes most numeric literals to use lowercase letters for the syntactic
parts and uppercase letters for the digits themselves: `0xAB` instead of `0XAB` and
`1e10` instead of `1E10`. Python 2 long literals are styled as `2L` instead of `2l` to
avoid confusion between `l` and `1`.

### Line breaks & binary operators

_Black_ will break a line before a binary operator when splitting a block of code over
multiple lines. This is so that _Black_ is compliant with the recent changes in the
[PEP 8](https://www.python.org/dev/peps/pep-0008/#should-a-line-break-before-or-after-a-binary-operator)
style guide, which emphasizes that this approach improves readability.

This behaviour may raise `W503 line break before binary operator` warnings in style
guide enforcement tools like Flake8. Since `W503` is not PEP 8 compliant, you should
tell Flake8 to ignore these warnings.

### Slices

PEP 8
[recommends](https://www.python.org/dev/peps/pep-0008/#whitespace-in-expressions-and-statements)
to treat `:` in slices as a binary operator with the lowest priority, and to leave an
equal amount of space on either side, except if a parameter is omitted (e.g.
`ham[1 + 1 :]`). It also states that for extended slices, both `:` operators have to
have the same amount of spacing, except if a parameter is omitted (`ham[1 + 1 ::]`).
_Black_ enforces these rules consistently.

This behaviour may raise `E203 whitespace before ':'` warnings in style guide
enforcement tools like Flake8. Since `E203` is not PEP 8 compliant, you should tell
Flake8 to ignore these warnings.

### Parentheses

Some parentheses are optional in the Python grammar. Any expression can be wrapped in a
pair of parentheses to form an atom. There are a few interesting cases:

- `if (...):`
- `while (...):`
- `for (...) in (...):`
- `assert (...), (...)`
- `from X import (...)`
- assignments like:
  - `target = (...)`
  - `target: type = (...)`
  - `some, *un, packing = (...)`
  - `augmented += (...)`

In those cases, parentheses are removed when the entire statement fits in one line, or
if the inner expression doesn't have any delimiters to further split on. If there is
only a single delimiter and the expression starts or ends with a bracket, the
parenthesis can also be successfully omitted since the existing bracket pair will
organize the expression neatly anyway. Otherwise, the parentheses are added.

Please note that _Black_ does not add or remove any additional nested parentheses that
you might want to have for clarity or further code organization. For example those
parentheses are not going to be removed:

```py3
return not (this or that)
decision = (maybe.this() and values > 0) or (maybe.that() and values < 0)
```

### Call chains

Some popular APIs, like ORMs, use call chaining. This API style is known as a
[fluent interface](https://en.wikipedia.org/wiki/Fluent_interface). _Black_ formats
those by treating dots that follow a call or an indexing operation like a very low
priority delimiter. It's easier to show the behavior than to explain it. Look at the
example:

```py3
def example(session):
    result = (
        session.query(models.Customer.id)
        .filter(
            models.Customer.account_id == account_id,
            models.Customer.email == email_address,
        )
        .order_by(models.Customer.id.asc())
        .all()
    )
```

### Typing stub files

PEP 484 describes the syntax for type hints in Python. One of the use cases for typing
is providing type annotations for modules which cannot contain them directly (they might
be written in C, or they might be third-party, or their implementation may be overly
dynamic, and so on).

To solve this,
[stub files with the `.pyi` file extension](https://www.python.org/dev/peps/pep-0484/#stub-files)
can be used to describe typing information for an external module. Those stub files omit
the implementation of classes and functions they describe, instead they only contain the
structure of the file (listing globals, functions, and classes with their members). The
recommended code style for those files is more terse than PEP 8:

- prefer `...` on the same line as the class/function signature;
- avoid vertical whitespace between consecutive module-level functions, names, or
  methods and fields within a single class;
- use a single blank line between top-level class definitions, or none if the classes
  are very small.

_Black_ enforces the above rules. There are additional guidelines for formatting `.pyi`
file that are not enforced yet but might be in a future version of the formatter:

- all function bodies should be empty (contain `...` instead of the body);
- do not use docstrings;
- prefer `...` over `pass`;
- for arguments with a default, use `...` instead of the actual default;
- avoid using string literals in type annotations, stub files support forward references
  natively (like Python 3.7 code with `from __future__ import annotations`);
- use variable annotations instead of type comments, even for stubs that target older
  versions of Python;
- for arguments that default to `None`, use `Optional[]` explicitly;
- use `float` instead of `Union[int, float]`.

## pyproject.toml

_Black_ is able to read project-specific default values for its command line options
from a `pyproject.toml` file. This is especially useful for specifying custom
`--include` and `--exclude` patterns for your project.

**Pro-tip**: If you're asking yourself "Do I need to configure anything?" the answer is
"No". _Black_ is all about sensible defaults.

### What on Earth is a `pyproject.toml` file?

[PEP 518](https://www.python.org/dev/peps/pep-0518/) defines `pyproject.toml` as a
configuration file to store build system requirements for Python projects. With the help
of tools like [Poetry](https://poetry.eustace.io/) or
[Flit](https://flit.readthedocs.io/en/latest/) it can fully replace the need for
`setup.py` and `setup.cfg` files.

### Where _Black_ looks for the file

By default _Black_ looks for `pyproject.toml` starting from the common base directory of
all files and directories passed on the command line. If it's not there, it looks in
parent directories. It stops looking when it finds the file, or a `.git` directory, or a
`.hg` directory, or the root of the file system, whichever comes first.

If you're formatting standard input, _Black_ will look for configuration starting from
the current working directory.

You can also explicitly specify the path to a particular file that you want with
`--config`. In this situation _Black_ will not look for any other file.

If you're running with `--verbose`, you will see a blue message if a file was found and
used.

Please note `blackd` will not use `pyproject.toml` configuration.

### Configuration format

As the file extension suggests, `pyproject.toml` is a
[TOML](https://github.com/toml-lang/toml) file. It contains separate sections for
different tools. _Black_ is using the `[tool.black]` section. The option keys are the
same as long names of options on the command line.

Note that you have to use single-quoted strings in TOML for regular expressions. It's
the equivalent of r-strings in Python. Multiline strings are treated as verbose regular
expressions by Black. Use `[ ]` to denote a significant space character.

<details>
<summary>Example `pyproject.toml`</summary>

```toml
[tool.black]
line-length = 88
target-version = ['py37']
include = '\.pyi?$'
exclude = '''

(
  /(
      \.eggs         # exclude a few common directories in the
    | \.git          # root of the project
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | _build
    | buck-out
    | build
    | dist
  )/
  | foo.py           # also separately exclude a file named foo.py in
                     # the root of the project
)
'''
```

</details>

### Lookup hierarchy

Command-line options have defaults that you can see in `--help`. A `pyproject.toml` can
override those defaults. Finally, options provided by the user on the command line
override both.

_Black_ will only ever use one `pyproject.toml` file during an entire run. It doesn't
look for multiple files, and doesn't compose configuration from different levels of the
file hierarchy.

## Editor integration

### Emacs

Use [proofit404/blacken](https://github.com/proofit404/blacken) or
[Elpy](https://github.com/jorgenschaefer/elpy).

### PyCharm/IntelliJ IDEA

1. Install `black`.

```console
$ pip install black
```

2. Locate your `black` installation folder.

On macOS / Linux / BSD:

```console
$ which black
/usr/local/bin/black  # possible location
```

On Windows:

```console
$ where black
%LocalAppData%\Programs\Python\Python36-32\Scripts\black.exe  # possible location
```

3. Open External tools in PyCharm/IntelliJ IDEA

On macOS:

`PyCharm -> Preferences -> Tools -> External Tools`

On Windows / Linux / BSD:

`File -> Settings -> Tools -> External Tools`

4. Click the + icon to add a new external tool with the following values:

   - Name: Black
   - Description: Black is the uncompromising Python code formatter.
   - Program: <install_location_from_step_2>
   - Arguments: `"$FilePath$"`

5. Format the currently opened file by selecting `Tools -> External Tools -> black`.

   - Alternatively, you can set a keyboard shortcut by navigating to
     `Preferences or Settings -> Keymap -> External Tools -> External Tools - Black`.

6. Optionally, run _Black_ on every file save:

   1. Make sure you have the
      [File Watcher](https://plugins.jetbrains.com/plugin/7177-file-watchers) plugin
      installed.
   2. Go to `Preferences or Settings -> Tools -> File Watchers` and click `+` to add a
      new watcher:
      - Name: Black
      - File type: Python
      - Scope: Project Files
      - Program: <install_location_from_step_2>
      - Arguments: `$FilePath$`
      - Output paths to refresh: `$FilePath$`
      - Working directory: `$ProjectFileDir$`

   - Uncheck "Auto-save edited files to trigger the watcher"

### Wing IDE

Wing supports black via the OS Commands tool, as explained in the Wing documentation on
[pep8 formatting](https://wingware.com/doc/edit/pep8). The detailed procedure is:

1. Install `black`.

```console
$ pip install black
```

2. Make sure it runs from the command line, e.g.

```console
$ black --help
```

3. In Wing IDE, activate the **OS Commands** panel and define the command **black** to
   execute black on the currently selected file:

- Use the Tools -> OS Commands menu selection
- click on **+** in **OS Commands** -> New: Command line..
  - Title: black
  - Command Line: black %s
  - I/O Encoding: Use Default
  - Key Binding: F1
  - [x] Raise OS Commands when executed
  - [x] Auto-save files before execution
  - [x] Line mode

4. Select a file in the editor and press **F1** , or whatever key binding you selected
   in step 3, to reformat the file.

### Vim

Commands and shortcuts:

- `:Black` to format the entire file (ranges not supported);
- `:BlackUpgrade` to upgrade _Black_ inside the virtualenv;
- `:BlackVersion` to get the current version of _Black_ inside the virtualenv.

Configuration:

- `g:black_fast` (defaults to `0`)
- `g:black_linelength` (defaults to `88`)
- `g:black_skip_string_normalization` (defaults to `0`)
- `g:black_virtualenv` (defaults to `~/.vim/black` or `~/.local/share/nvim/black`)

To install with [vim-plug](https://github.com/junegunn/vim-plug):

```
Plug 'psf/black'
```

or with [Vundle](https://github.com/VundleVim/Vundle.vim):

```
Plugin 'psf/black'
```

or you can copy the plugin from
[plugin/black.vim](https://github.com/psf/black/tree/master/plugin/black.vim).

```
mkdir -p ~/.vim/pack/python/start/black/plugin
curl https://raw.githubusercontent.com/psf/black/master/plugin/black.vim -o ~/.vim/pack/python/start/black/plugin/black.vim
```

Let me know if this requires any changes to work with Vim 8's builtin `packadd`, or
Pathogen, and so on.

This plugin **requires Vim 7.0+ built with Python 3.6+ support**. It needs Python 3.6 to
be able to run _Black_ inside the Vim process which is much faster than calling an
external command.

On first run, the plugin creates its own virtualenv using the right Python version and
automatically installs _Black_. You can upgrade it later by calling `:BlackUpgrade` and
restarting Vim.

If you need to do anything special to make your virtualenv work and install _Black_ (for
example you want to run a version from master), create a virtualenv manually and point
`g:black_virtualenv` to it. The plugin will use it.

To run _Black_ on save, add the following line to `.vimrc` or `init.vim`:

```
autocmd BufWritePre *.py execute ':Black'
```

To run _Black_ on a key press (e.g. F9 below), add this:

```
nnoremap <F9> :Black<CR>
```

**How to get Vim with Python 3.6?** On Ubuntu 17.10 Vim comes with Python 3.6 by
default. On macOS with Homebrew run: `brew install vim`. When building Vim from source,
use: `./configure --enable-python3interp=yes`. There's many guides online how to do
this.

### Visual Studio Code

Use the
[Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
([instructions](https://code.visualstudio.com/docs/python/editing#_formatting)).

### SublimeText 3

Use [sublack plugin](https://github.com/jgirardet/sublack).

### Jupyter Notebook Magic

Use [blackcellmagic](https://github.com/csurfer/blackcellmagic).

### Python Language Server

If your editor supports the [Language Server Protocol](https://langserver.org/) (Atom,
Sublime Text, Visual Studio Code and many more), you can use the
[Python Language Server](https://github.com/palantir/python-language-server) with the
[pyls-black](https://github.com/rupert/pyls-black) plugin.

### Atom/Nuclide

Use [python-black](https://atom.io/packages/python-black).

### Kakoune

Add the following hook to your kakrc, then run black with `:format`.

```
hook global WinSetOption filetype=python %{
    set-option window formatcmd 'black -q  -'
}
```

### Thonny

Use [Thonny-black-code-format](https://github.com/Franccisco/thonny-black-code-format).

### Other editors

Other editors will require external contributions.

Patches welcome! ✨ 🍰 ✨

Any tool that can pipe code through _Black_ using its stdio mode (just
[use `-` as the file name](https://www.tldp.org/LDP/abs/html/special-chars.html#DASHREF2)).
The formatted code will be returned on stdout (unless `--check` was passed). _Black_
will still emit messages on stderr but that shouldn't affect your use case.

This can be used for example with PyCharm's or IntelliJ's
[File Watchers](https://www.jetbrains.com/help/pycharm/file-watchers.html).

## blackd

`blackd` is a small HTTP server that exposes _Black_'s functionality over a simple
protocol. The main benefit of using it is to avoid paying the cost of starting up a new
_Black_ process every time you want to blacken a file.

### Usage

`blackd` is not packaged alongside _Black_ by default because it has additional
dependencies. You will need to do `pip install black[d]` to install it.

You can start the server on the default port, binding only to the local interface by
running `blackd`. You will see a single line mentioning the server's version, and the
host and port it's listening on. `blackd` will then print an access log similar to most
web servers on standard output, merged with any exception traces caused by invalid
formatting requests.

`blackd` provides even less options than _Black_. You can see them by running
`blackd --help`:

```text
Usage: blackd [OPTIONS]

Options:
  --bind-host TEXT                Address to bind the server to.
  --bind-port INTEGER             Port to listen on
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.
```

There is no official blackd client tool (yet!). You can test that blackd is working
using `curl`:

```
blackd --bind-port 9090 &  # or let blackd choose a port
curl -s -XPOST "localhost:9090" -d "print('valid')"
```

### Protocol

`blackd` only accepts `POST` requests at the `/` path. The body of the request should
contain the python source code to be formatted, encoded according to the `charset` field
in the `Content-Type` request header. If no `charset` is specified, `blackd` assumes
`UTF-8`.

There are a few HTTP headers that control how the source is formatted. These correspond
to command line flags for _Black_. There is one exception to this: `X-Protocol-Version`
which if present, should have the value `1`, otherwise the request is rejected with
`HTTP 501` (Not Implemented).

The headers controlling how code is formatted are:

- `X-Line-Length`: corresponds to the `--line-length` command line flag.
- `X-Skip-String-Normalization`: corresponds to the `--skip-string-normalization`
  command line flag. If present and its value is not the empty string, no string
  normalization will be performed.
- `X-Fast-Or-Safe`: if set to `fast`, `blackd` will act as _Black_ does when passed the
  `--fast` command line flag.
- `X-Python-Variant`: if set to `pyi`, `blackd` will act as _Black_ does when passed the
  `--pyi` command line flag. Otherwise, its value must correspond to a Python version or
  a set of comma-separated Python versions, optionally prefixed with `py`. For example,
  to request code that is compatible with Python 3.5 and 3.6, set the header to
  `py3.5,py3.6`.
- `X-Diff`: corresponds to the `--diff` command line flag. If present, a diff of the
  formats will be output.

If any of these headers are set to invalid values, `blackd` returns a `HTTP 400` error
response, mentioning the name of the problematic header in the message body.

Apart from the above, `blackd` can produce the following response codes:

- `HTTP 204`: If the input is already well-formatted. The response body is empty.
- `HTTP 200`: If formatting was needed on the input. The response body contains the
  blackened Python code, and the `Content-Type` header is set accordingly.
- `HTTP 400`: If the input contains a syntax error. Details of the error are returned in
  the response body.
- `HTTP 500`: If there was any kind of error while trying to format the input. The
  response body contains a textual representation of the error.

The response headers include a `X-Black-Version` header containing the version of
_Black_.

## Version control integration

Use [pre-commit](https://pre-commit.com/). Once you
[have it installed](https://pre-commit.com/#install), add this to the
`.pre-commit-config.yaml` in your repository:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: stable
    hooks:
      - id: black
        language_version: python3.6
```

Then run `pre-commit install` and you're ready to go.

### Configuring pre-commit

If you want a project-wide setting, you can store the necessary configuration in
`pyproject.toml` so that pre-commit, editors and command-line invocation of Black all
behave consistently for your project. See _Black_'s own
[pyproject.toml](https://github.com/psf/black/blob/master/pyproject.toml) for an
example.

You can use `args` in the hook to separately customize how pre-commit should invoke
_Black_.

If you're already using Python 3.7, switch the `language_version` accordingly. Finally,
`stable` is a tag that is pinned to the latest release on PyPI. If you'd rather run on
master, this is also an option.

`pre-commit` has
[settings for all hooks](https://pre-commit.com/#adding-pre-commit-plugins-to-your-project)
and [settings for each hook](https://pre-commit.com/#pre-commit-configyaml---hooks).

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: stable
    hooks:
      - id: black
        # Use Python 3.7
        language_version: python3.7
        # Customize options for black command
        args: [--arg-for-black, "value", --flag-for-black]
        # Include only these files
        files: "^src/.*"
        # Exclude patterns
        exclude: "tests/.*$"
```

## Ignoring unmodified files

_Black_ remembers files it has already formatted, unless the `--diff` flag is used or
code is passed via standard input. This information is stored per-user. The exact
location of the file depends on the _Black_ version and the system on which _Black_ is
run. The file is non-portable. The standard location on common operating systems is:

- Windows:
  `C:\\Users\<username>\AppData\Local\black\black\Cache\<version>\cache.<line-length>.<file-mode>.pickle`
- macOS:
  `/Users/<username>/Library/Caches/black/<version>/cache.<line-length>.<file-mode>.pickle`
- Linux:
  `/home/<username>/.cache/black/<version>/cache.<line-length>.<file-mode>.pickle`

`file-mode` is an int flag that determines whether the file was formatted as 3.6+ only,
as .pyi, and whether string normalization was omitted.

To override the location of these files on macOS or Linux, set the environment variable
`XDG_CACHE_HOME` to your preferred location. For example, if you want to put the cache
in the directory you're running _Black_ from, set `XDG_CACHE_HOME=.cache`. _Black_ will
then write the above files to `.cache/black/<version>/`.

## Used by

The following notable open-source projects trust _Black_ with enforcing a consistent
code style: pytest, tox, Pyramid, Django Channels, Hypothesis, attrs, SQLAlchemy,
Poetry, PyPA applications (Warehouse, Pipenv, virtualenv), pandas, Pillow, every Datadog
Agent Integration, Home Assistant.

Are we missing anyone? Let us know.

## Testimonials

**Dusty Phillips**,
[writer](https://smile.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=dusty+phillips):

> _Black_ is opinionated so you don't have to be.

**Hynek Schlawack**, [creator of `attrs`](https://www.attrs.org/), core developer of
Twisted and CPython:

> An auto-formatter that doesn't suck is all I want for Xmas!

**Carl Meyer**, [Django](https://www.djangoproject.com/) core developer:

> At least the name is good.

**Kenneth Reitz**, creator of [`requests`](http://python-requests.org/) and
[`pipenv`](https://docs.pipenv.org/):

> This vastly improves the formatting of our code. Thanks a ton!

## Show your style

Use the badge in your project's README.md:

```markdown
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
```

Using the badge in README.rst:

```
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
```

Looks like this:
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## License

MIT

## Contributing to _Black_

In terms of inspiration, _Black_ is about as configurable as _gofmt_. This is
deliberate.

Bug reports and fixes are always welcome! However, before you suggest a new feature or
configuration knob, ask yourself why you want it. If it enables better integration with
some workflow, fixes an inconsistency, speeds things up, and so on - go for it! On the
other hand, if your answer is "because I don't like a particular formatting" then you're
not ready to embrace _Black_ yet. Such changes are unlikely to get accepted. You can
still try but prepare to be disappointed.

More details can be found in [CONTRIBUTING](CONTRIBUTING.md).

## Change Log

### 19.10b0

- added support for PEP 572 assignment expressions (#711)

- added support for PEP 570 positional-only arguments (#943)

- added support for async generators (#593)

- added support for pre-splitting collections by putting an explicit trailing comma
  inside (#826)

- added `black -c` as a way to format code passed from the command line (#761)

- --safe now works with Python 2 code (#840)

- fixed grammar selection for Python 2-specific code (#765)

- fixed feature detection for trailing commas in function definitions and call sites
  (#763)

- `# fmt: off`/`# fmt: on` comment pairs placed multiple times within the same block of
  code now behave correctly (#1005)

- _Black_ no longer crashes on Windows machines with more than 61 cores (#838)

- _Black_ no longer crashes on standalone comments prepended with a backslash (#767)

- _Black_ no longer crashes on `from` ... `import` blocks with comments (#829)

- _Black_ no longer crashes on Python 3.7 on some platform configurations (#494)

- _Black_ no longer fails on comments in from-imports (#671)

- _Black_ no longer fails when the file starts with a backslash (#922)

- _Black_ no longer merges regular comments with type comments (#1027)

- _Black_ no longer splits long lines that contain type comments (#997)

- removed unnecessary parentheses around `yield` expressions (#834)

- added parentheses around long tuples in unpacking assignments (#832)

- added parentheses around complex powers when they are prefixed by a unary operator
  (#646)

- fixed bug that led _Black_ format some code with a line length target of 1 (#762)

- _Black_ no longer introduces quotes in f-string subexpressions on string boundaries
  (#863)

- if _Black_ puts parenthesis around a single expression, it moves comments to the
  wrapped expression instead of after the brackets (#872)

- `blackd` now returns the version of _Black_ in the response headers (#1013)

- `blackd` can now output the diff of formats on source code when the `X-Diff` header is
  provided (#969)

### 19.3b0

- new option `--target-version` to control which Python versions _Black_-formatted code
  should target (#618)

- deprecated `--py36` (use `--target-version=py36` instead) (#724)

- _Black_ no longer normalizes numeric literals to include `_` separators (#696)

- long `del` statements are now split into multiple lines (#698)

- type comments are no longer mangled in function signatures

- improved performance of formatting deeply nested data structures (#509)

- _Black_ now properly formats multiple files in parallel on Windows (#632)

- _Black_ now creates cache files atomically which allows it to be used in parallel
  pipelines (like `xargs -P8`) (#673)

- _Black_ now correctly indents comments in files that were previously formatted with
  tabs (#262)

- `blackd` now supports CORS (#622)

### 18.9b0

- numeric literals are now formatted by _Black_ (#452, #461, #464, #469):

  - numeric literals are normalized to include `_` separators on Python 3.6+ code

  - added `--skip-numeric-underscore-normalization` to disable the above behavior and
    leave numeric underscores as they were in the input

  - code with `_` in numeric literals is recognized as Python 3.6+

  - most letters in numeric literals are lowercased (e.g., in `1e10`, `0x01`)

  - hexadecimal digits are always uppercased (e.g. `0xBADC0DE`)

- added `blackd`, see [its documentation](#blackd) for more info (#349)

- adjacent string literals are now correctly split into multiple lines (#463)

- trailing comma is now added to single imports that don't fit on a line (#250)

- cache is now populated when `--check` is successful for a file which speeds up
  consecutive checks of properly formatted unmodified files (#448)

- whitespace at the beginning of the file is now removed (#399)

- fixed mangling [pweave](http://mpastell.com/pweave/) and
  [Spyder IDE](https://pythonhosted.org/spyder/) special comments (#532)

- fixed unstable formatting when unpacking big tuples (#267)

- fixed parsing of `__future__` imports with renames (#389)

- fixed scope of `# fmt: off` when directly preceding `yield` and other nodes (#385)

- fixed formatting of lambda expressions with default arguments (#468)

- fixed `async for` statements: _Black_ no longer breaks them into separate lines (#372)

- note: the Vim plugin stopped registering `,=` as a default chord as it turned out to
  be a bad idea (#415)

### 18.6b4

- hotfix: don't freeze when multiple comments directly precede `# fmt: off` (#371)

### 18.6b3

- typing stub files (`.pyi`) now have blank lines added after constants (#340)

- `# fmt: off` and `# fmt: on` are now much more dependable:

  - they now work also within bracket pairs (#329)

  - they now correctly work across function/class boundaries (#335)

  - they now work when an indentation block starts with empty lines or misaligned
    comments (#334)

- made Click not fail on invalid environments; note that Click is right but the
  likelihood we'll need to access non-ASCII file paths when dealing with Python source
  code is low (#277)

- fixed improper formatting of f-strings with quotes inside interpolated expressions
  (#322)

- fixed unnecessary slowdown when long list literals where found in a file

- fixed unnecessary slowdown on AST nodes with very many siblings

- fixed cannibalizing backslashes during string normalization

- fixed a crash due to symbolic links pointing outside of the project directory (#338)

### 18.6b2

- added `--config` (#65)

- added `-h` equivalent to `--help` (#316)

- fixed improper unmodified file caching when `-S` was used

- fixed extra space in string unpacking (#305)

- fixed formatting of empty triple quoted strings (#313)

- fixed unnecessary slowdown in comment placement calculation on lines without comments

### 18.6b1

- hotfix: don't output human-facing information on stdout (#299)

- hotfix: don't output cake emoji on non-zero return code (#300)

### 18.6b0

- added `--include` and `--exclude` (#270)

- added `--skip-string-normalization` (#118)

- added `--verbose` (#283)

- the header output in `--diff` now actually conforms to the unified diff spec

- fixed long trivial assignments being wrapped in unnecessary parentheses (#273)

- fixed unnecessary parentheses when a line contained multiline strings (#232)

- fixed stdin handling not working correctly if an old version of Click was used (#276)

- _Black_ now preserves line endings when formatting a file in place (#258)

### 18.5b1

- added `--pyi` (#249)

- added `--py36` (#249)

- Python grammar pickle caches are stored with the formatting caches, making _Black_
  work in environments where site-packages is not user-writable (#192)

- _Black_ now enforces a PEP 257 empty line after a class-level docstring (and/or
  fields) and the first method

- fixed invalid code produced when standalone comments were present in a trailer that
  was omitted from line splitting on a large expression (#237)

- fixed optional parentheses being removed within `# fmt: off` sections (#224)

- fixed invalid code produced when stars in very long imports were incorrectly wrapped
  in optional parentheses (#234)

- fixed unstable formatting when inline comments were moved around in a trailer that was
  omitted from line splitting on a large expression (#238)

- fixed extra empty line between a class declaration and the first method if no class
  docstring or fields are present (#219)

- fixed extra empty line between a function signature and an inner function or inner
  class (#196)

### 18.5b0

- call chains are now formatted according to the
  [fluent interfaces](https://en.wikipedia.org/wiki/Fluent_interface) style (#67)

- data structure literals (tuples, lists, dictionaries, and sets) are now also always
  exploded like imports when they don't fit in a single line (#152)

- slices are now formatted according to PEP 8 (#178)

- parentheses are now also managed automatically on the right-hand side of assignments
  and return statements (#140)

- math operators now use their respective priorities for delimiting multiline
  expressions (#148)

- optional parentheses are now omitted on expressions that start or end with a bracket
  and only contain a single operator (#177)

- empty parentheses in a class definition are now removed (#145, #180)

- string prefixes are now standardized to lowercase and `u` is removed on Python 3.6+
  only code and Python 2.7+ code with the `unicode_literals` future import (#188, #198,
  #199)

- typing stub files (`.pyi`) are now formatted in a style that is consistent with PEP
  484 (#207, #210)

- progress when reformatting many files is now reported incrementally

- fixed trailers (content with brackets) being unnecessarily exploded into their own
  lines after a dedented closing bracket (#119)

- fixed an invalid trailing comma sometimes left in imports (#185)

- fixed non-deterministic formatting when multiple pairs of removable parentheses were
  used (#183)

- fixed multiline strings being unnecessarily wrapped in optional parentheses in long
  assignments (#215)

- fixed not splitting long from-imports with only a single name

- fixed Python 3.6+ file discovery by also looking at function calls with unpacking.
  This fixed non-deterministic formatting if trailing commas where used both in function
  signatures with stars and function calls with stars but the former would be
  reformatted to a single line.

- fixed crash on dealing with optional parentheses (#193)

- fixed "is", "is not", "in", and "not in" not considered operators for splitting
  purposes

- fixed crash when dead symlinks where encountered

### 18.4a4

- don't populate the cache on `--check` (#175)

### 18.4a3

- added a "cache"; files already reformatted that haven't changed on disk won't be
  reformatted again (#109)

- `--check` and `--diff` are no longer mutually exclusive (#149)

- generalized star expression handling, including double stars; this fixes
  multiplication making expressions "unsafe" for trailing commas (#132)

- _Black_ no longer enforces putting empty lines behind control flow statements (#90)

- _Black_ now splits imports like "Mode 3 + trailing comma" of isort (#127)

- fixed comment indentation when a standalone comment closes a block (#16, #32)

- fixed standalone comments receiving extra empty lines if immediately preceding a
  class, def, or decorator (#56, #154)

- fixed `--diff` not showing entire path (#130)

- fixed parsing of complex expressions after star and double stars in function calls
  (#2)

- fixed invalid splitting on comma in lambda arguments (#133)

- fixed missing splits of ternary expressions (#141)

### 18.4a2

- fixed parsing of unaligned standalone comments (#99, #112)

- fixed placement of dictionary unpacking inside dictionary literals (#111)

- Vim plugin now works on Windows, too

- fixed unstable formatting when encountering unnecessarily escaped quotes in a string
  (#120)

### 18.4a1

- added `--quiet` (#78)

- added automatic parentheses management (#4)

- added [pre-commit](https://pre-commit.com) integration (#103, #104)

- fixed reporting on `--check` with multiple files (#101, #102)

- fixed removing backslash escapes from raw strings (#100, #105)

### 18.4a0

- added `--diff` (#87)

- add line breaks before all delimiters, except in cases like commas, to better comply
  with PEP 8 (#73)

- standardize string literals to use double quotes (almost) everywhere (#75)

- fixed handling of standalone comments within nested bracketed expressions; _Black_
  will no longer produce super long lines or put all standalone comments at the end of
  the expression (#22)

- fixed 18.3a4 regression: don't crash and burn on empty lines with trailing whitespace
  (#80)

- fixed 18.3a4 regression: `# yapf: disable` usage as trailing comment would cause
  _Black_ to not emit the rest of the file (#95)

- when CTRL+C is pressed while formatting many files, _Black_ no longer freaks out with
  a flurry of asyncio-related exceptions

- only allow up to two empty lines on module level and only single empty lines within
  functions (#74)

### 18.3a4

- `# fmt: off` and `# fmt: on` are implemented (#5)

- automatic detection of deprecated Python 2 forms of print statements and exec
  statements in the formatted file (#49)

- use proper spaces for complex expressions in default values of typed function
  arguments (#60)

- only return exit code 1 when --check is used (#50)

- don't remove single trailing commas from square bracket indexing (#59)

- don't omit whitespace if the previous factor leaf wasn't a math operator (#55)

- omit extra space in kwarg unpacking if it's the first argument (#46)

- omit extra space in
  [Sphinx auto-attribute comments](http://www.sphinx-doc.org/en/stable/ext/autodoc.html#directive-autoattribute)
  (#68)

### 18.3a3

- don't remove single empty lines outside of bracketed expressions (#19)

- added ability to pipe formatting from stdin to stdin (#25)

- restored ability to format code with legacy usage of `async` as a name (#20, #42)

- even better handling of numpy-style array indexing (#33, again)

### 18.3a2

- changed positioning of binary operators to occur at beginning of lines instead of at
  the end, following
  [a recent change to PEP 8](https://github.com/python/peps/commit/c59c4376ad233a62ca4b3a6060c81368bd21e85b)
  (#21)

- ignore empty bracket pairs while splitting. This avoids very weirdly looking
  formattings (#34, #35)

- remove a trailing comma if there is a single argument to a call

- if top level functions were separated by a comment, don't put four empty lines after
  the upper function

- fixed unstable formatting of newlines with imports

- fixed unintentional folding of post scriptum standalone comments into last statement
  if it was a simple statement (#18, #28)

- fixed missing space in numpy-style array indexing (#33)

- fixed spurious space after star-based unary expressions (#31)

### 18.3a1

- added `--check`

- only put trailing commas in function signatures and calls if it's safe to do so. If
  the file is Python 3.6+ it's always safe, otherwise only safe if there are no `*args`
  or `**kwargs` used in the signature or call. (#8)

- fixed invalid spacing of dots in relative imports (#6, #13)

- fixed invalid splitting after comma on unpacked variables in for-loops (#23)

- fixed spurious space in parenthesized set expressions (#7)

- fixed spurious space after opening parentheses and in default arguments (#14, #17)

- fixed spurious space after unary operators when the operand was a complex expression
  (#15)

### 18.3a0

- first published version, Happy 🍰 Day 2018!

- alpha quality

- date-versioned (see: https://calver.org/)

## Authors

Glued together by [Łukasz Langa](mailto:lukasz@langa.pl).

Maintained with [Carol Willing](mailto:carolcode@willingconsulting.com),
[Carl Meyer](mailto:carl@oddbird.net),
[Jelle Zijlstra](mailto:jelle.zijlstra@gmail.com),
[Mika Naylor](mailto:mail@autophagy.io), and
[Zsolt Dollenstein](mailto:zsol.zsol@gmail.com).

Multiple contributions by:

- [Abdur-Rahmaan Janhangeer](mailto:cryptolabour@gmail.com)
- [Adam Johnson](mailto:me@adamj.eu)
- [Alexander Huynh](mailto:github@grande.coffee)
- [Andrew Thorp](mailto:andrew.thorp.dev@gmail.com)
- [Andrey](mailto:dyuuus@yandex.ru)
- [Andy Freeland](mailto:andy@andyfreeland.net)
- [Anthony Sottile](mailto:asottile@umich.edu)
- [Arjaan Buijk](mailto:arjaan.buijk@gmail.com)
- [Artem Malyshev](mailto:proofit404@gmail.com)
- [Asger Hautop Drewsen](mailto:asgerdrewsen@gmail.com)
- [Augie Fackler](mailto:raf@durin42.com)
- [Aviskar KC](mailto:aviskarkc10@gmail.com)
- [Benjamin Woodruff](mailto:github@benjam.info)
- [Brandt Bucher](mailto:brandtbucher@gmail.com)
- Charles Reid
- [Christian Heimes](mailto:christian@python.org)
- [Chuck Wooters](mailto:chuck.wooters@microsoft.com)
- [Daniel Hahler](mailto:github@thequod.de)
- [Daniel M. Capella](mailto:polycitizen@gmail.com)
- Daniele Esposti
- dylanjblack
- [Eli Treuherz](mailto:eli@treuherz.com)
- [Florent Thiery](mailto:fthiery@gmail.com)
- hauntsaninja
- Hugo van Kemenade
- [Ivan Katanić](mailto:ivan.katanic@gmail.com)
- [Jason Fried](mailto:me@jasonfried.info)
- [jgirardet](mailto:ijkl@netc.fr)
- [Joe Antonakakis](mailto:jma353@cornell.edu)
- [Jon Dufresne](mailto:jon.dufresne@gmail.com)
- [Jonas Obrist](mailto:ojiidotch@gmail.com)
- [Josh Bode](mailto:joshbode@fastmail.com)
- [Juan Luis Cano Rodríguez](mailto:hello@juanlu.space)
- [Katie McLaughlin](mailto:katie@glasnt.com)
- Lawrence Chan
- [Linus Groh](mailto:mail@linusgroh.de)
- [Luka Sterbic](mailto:luka.sterbic@gmail.com)
- Mariatta
- [Matt VanEseltine](mailto:vaneseltine@gmail.com)
- [Michael Flaxman](mailto:michael.flaxman@gmail.com)
- [Michael J. Sullivan](mailto:sully@msully.net)
- [Michael McClimon](mailto:michael@mcclimon.org)
- [Miguel Gaiowski](mailto:miggaiowski@gmail.com)
- [Mike](mailto:roshi@fedoraproject.org)
- [Min ho Kim](mailto:minho42@gmail.com)
- [Miroslav Shubernetskiy](mailto:miroslav@miki725.com)
- [Neraste](mailto:neraste.herr10@gmail.com)
- [Ofek Lev](mailto:ofekmeister@gmail.com)
- [Osaetin Daniel](mailto:osaetindaniel@gmail.com)
- [Pablo Galindo](mailto:Pablogsal@gmail.com)
- [Peter Bengtsson](mailto:mail@peterbe.com)
- pmacosta
- [Rishikesh Jha](mailto:rishijha424@gmail.com)
- [Stavros Korokithakis](mailto:hi@stavros.io)
- [Stephen Rosen](mailto:sirosen@globus.org)
- [Sunil Kapil](mailto:snlkapil@gmail.com)
- [Thom Lu](mailto:thomas.c.lu@gmail.com)
- [Tom Christie](mailto:tom@tomchristie.com)
- [Tzu-ping Chung](mailto:uranusjr@gmail.com)
- [Utsav Shah](mailto:ukshah2@illinois.edu)
- vezeli
- [Vishwas B Sharma](mailto:sharma.vishwas88@gmail.com)
- [Yngve Høiseth](mailto:yngve@hoiseth.net)
- [Yurii Karabas](mailto:1998uriyyo@gmail.com)
