import functools


class reprwrapper(object):
    def __init__(self, repr, func):
        self._repr = repr
        self._func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kw):
        return self._func(*args, **kw)

    def __repr__(self):
        return self._repr(self._func)


def withrepr(reprfun):
    def _wrap(func):
        return reprwrapper(reprfun, func)

    return _wrap
