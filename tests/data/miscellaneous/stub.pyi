X: int

def f(): ...


class D: 
    ...


class C:
    ...

class B:
    this_lack_of_newline_should_be_kept: int
    def b(self) -> None: ...

    but_this_newline_should_also_be_kept: int

class A:
    attr: int
    attr2: str

    def f(self) -> int:
        ...

    def g(self) -> str: ...



def g():
    ...

def h(): ...

if sys.version_info >= (3, 8):
    class E:
        def f(self): ...
    class F:

        def f(self): ...
    class G: ...
    class H: ...
else:
    class I: ...
    class J: ...
    def f(): ...

    class K:
        def f(self): ...
    def f(): ...

class Nested:
    class dirty: ...
    class little: ...
    class secret:
        def who_has_to_know(self): ...
    def verse(self): ...

class Outer:
    class Inner:
        inner_attr: int
    outer_attr: int

class Conditional:
    def f(self): ...
    if sys.version_info >= (3, 8):
        def g(self): ...
    else:
        def g(self): ...
    def h(self): ...
    def i(self): ...
    if sys.version_info >= (3, 8):
        def j(self): ...
    def k(self): ...
    if sys.version_info >= (3, 8):
        class A: ...
        class B: ...
        class C:
            def l(self): ...
            def m(self): ...


# output
X: int

def f(): ...

class D: ...
class C: ...

class B:
    this_lack_of_newline_should_be_kept: int
    def b(self) -> None: ...

    but_this_newline_should_also_be_kept: int

class A:
    attr: int
    attr2: str

    def f(self) -> int: ...
    def g(self) -> str: ...

def g(): ...
def h(): ...

if sys.version_info >= (3, 8):
    class E:
        def f(self): ...

    class F:
        def f(self): ...

    class G: ...
    class H: ...

else:
    class I: ...
    class J: ...

    def f(): ...

    class K:
        def f(self): ...

    def f(): ...

class Nested:
    class dirty: ...
    class little: ...

    class secret:
        def who_has_to_know(self): ...

    def verse(self): ...

class Outer:
    class Inner:
        inner_attr: int

    outer_attr: int

class Conditional:
    def f(self): ...
    if sys.version_info >= (3, 8):
        def g(self): ...
    else:
        def g(self): ...

    def h(self): ...
    def i(self): ...
    if sys.version_info >= (3, 8):
        def j(self): ...

    def k(self): ...
    if sys.version_info >= (3, 8):
        class A: ...
        class B: ...

        class C:
            def l(self): ...
            def m(self): ...
