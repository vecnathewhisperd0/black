# Regression test for https://github.com/psf/black/issues/3129.
setup(
    entry_points={
        # fmt: off
        "console_scripts": [
            "foo-bar"
            "=foo.bar.:main",
        # fmt: on
        ]
    },
)


# Regression test for https://github.com/psf/black/issues/3129.
run(
    # fmt: off
    [
        "ls",
        "-la",
    ]
    # fmt: on
    + path
    ,
    check=True,
)


# Regression test for https://github.com/psf/black/issues/3026.
def test_func():
    # yapf: disable
    if a:
        return True
    # yapf: enable
    elif b:
        return True

    return False
