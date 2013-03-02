import warnings
import functools
import re
import os
import dbus
from PyKDE4.kdecore import i18n


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
    """ Represents a system daemon (works only with systemd).
    It currently allows for checking if a daemon is installed and wether
    it is enabled. Later versions will feature code to enable them and to
    create log messages.
    """
    # we can share this
    _matcher = re.compile("(en|dis)abled")
    _bus = dbus.SystemBus()
    _proxy = _bus.get_object(
        'org.freedesktop.systemd1',
        '/org/freedesktop/systemd1')
    _interface = dbus.Interface(_proxy, 'org.freedesktop.systemd1.Manager')

    def __init__(self, name=None, descriptive_name=None):
        """:name The name of the daemon
           :enabled_changed: if the enabled state changed
           :descriptive name: name that the user willl see, e.g "the firewall"
            for ufw
        """
        if name is None:
            warnings.warn("Using  Daemon this way is deprecated")
        self.name = name
        if descriptive_name is None:
            self.descriptive_name = name
        else:
            self.descriptive_name = descriptive_name
        self.enabled_changed = False
        self._enabled = self.is_enabled()

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
        """Returns true if and only if the daemon's state is enabled.
        Note that false is returned when the state is e.g. static.
        """
        if not self.is_installed():
            return True
        result = str(Daemon._interface.GetUnitFileState(self.name + ".service"))
        match = re.search(Daemon._matcher, result)
        if match:
            return "enabled" == match.group()
        return False

    def is_installed(self):
        """Checks if a daemon is installed"""
        result = os.path.exists("/usr/lib/systemd/system/%s.service" % self.name)
        return result

    def toggle_enable(self):
        """Signals that the daemon should be en/disabled later.
          The change will only take place after a call to apply_changes"""
        self.enabled_changed = not self.enabled_changed
        self._enabled = not self._enabled

    def apply_changes(self):
        """If the configuration was changed, apply the changes"""
        # TODO
        if not self.is_installed():
            raise IOError("Daemon is not installed!")
        raise Exception()

    def report(self):
        """Return a string which explains what has changed"""
        if not self.is_installed():
            raise IOError("Daemon is not installed!")
        if self.enabled_changed:
            if self.enabled:
                return i18n("{} has been enabled".format(self.descriptive_name))
            else:
                return i18n("{} has been disabled".format(self.descriptive_name))
