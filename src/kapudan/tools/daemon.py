import sys
import warnings
import functools


def deprecated(message=None):
    '''This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.'''

    if message:
        warnings.warn(message)

    def real_decorator(func):
        @functools.wraps(func)
        def new_func(*args, **kwargs):
            warnings.warn_explicit(
                "Call to deprecated function {}.".format(func.__name__),
                category=DeprecationWarning,
                filename=func.func_code.co_filename,
                lineno=func.func_code.co_firstlineno + 1
            )
            return func(*args, **kwargs)
        return new_func
    return real_decorator


class Daemon(object):
    def __init__(self):
        print >> sys.stderr, "Unfinished"

    @deprecated("You shouldn't rely on this method, as it doesn't work with systemd")
    def isEnabled(self, name):
        return False

    @deprecated("You shouldn't rely on this method, as it doesn't work with systemd")
    def isInstalled(self, name):
        return True
