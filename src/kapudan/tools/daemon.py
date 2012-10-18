import warnings
import functools
import re
import os


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
    _matcher = re.compile("(en|dis)abled")

    def __init__(self, name=None):
        if name is None:
            warnings.warn("Using  Daemon this way is deprecated")
        self.name = name

    @deprecated("You shouldn't rely on this method, but rather use is_enabled")
    def isEnabled(self, name):
        if self.name:
            raise Warning("Using the old API, but name is not None! Aborting")
        self.name = name
        result = self.is_enabled()
        self.name = None
        return result

    @deprecated("You shouldn't rely on this method, but rather use is_installed")
    def isInstalled(self, name):
        if self.name:
            raise Warning("Using the old API, but name is not None! Aborting")
        self.name = name
        result = self.is_installed()
        self.name = None
        return result

    def is_enabled(self):
        result = os.popen("systemctl show --property=UnitFileState %s" % self.name)
        match = re.search(Daemon._matcher, result.read())
        result.close()
        if match:
            return "enabled" == match.group()
        return False

    def is_installed(self):
        result = os.path.exists("/usr/lib/systemd/system/%s.service" % self.name)
        return result
