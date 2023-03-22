from typing import Callable, TypeVar

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")
W = TypeVar("W", bound=Callable)


def Idiot(x: T) -> T:
    """The Identity λx.x"""
    return x


def MockingBird(x: W) -> W:
    """Self application λf.ff"""
    return x(x)


def Cardinal(f: Callable[[U], Callable[[T], T]]) -> Callable[[T], Callable[[U], T]]:
    """Flipping arguments λfab.fba"""

    def _Cardinal1(a: T) -> Callable[[U], T]:
        def _Cardinal2(b: U) -> T:
            return f(b)(a)

        return _Cardinal2

    return _Cardinal1
