from typing import Callable
from typing import TypeVar
from .utils import withrepr

T = TypeVar("T")


@withrepr(lambda x: "TRUE")
def TRUE(thn: T) -> Callable[[T], T]:
    def _TRUE(els: T) -> T:
        return thn

    return TRUE


@withrepr(lambda x: "FALSE")
def FALSE(thn: T) -> Callable[[T], T]:
    def _FALSE(els: T) -> T:
        return els

    return _FALSE
