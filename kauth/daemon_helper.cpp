#include <QDBusInterface>
#include <QDBusConnection>
#include "daemon_helper.h"
ActionReply DaemonHelper::enabledaemon(QVariantMap args)
{
	QString daemon = args["daemonname"].toString();
	QDBusInterface sytemdManager( "org.freedesktop.systemd1", "/Manager",
		       "org.freedesktop.systemd1.Manager", QDBusConnection::systemBus());
	QList<QVariant> arguments;
	arguments.append(args["daemonname"]); // name of the daemon
	arguments.append(false); // enable persistently
	arguments.append(true); // replace symlinks if necessary
	systemdManagerInterface->callWithArgumentList("EnableUnitFiles", arguments)
	return ActionReply::SuccessReply;
}

ActionReply DaemonHelper::disabledaemon(QVariantMap args)
{
	QString daemon = args["daemonname"].toString();
	QDBusInterface sytemdManager( "org.freedesktop.systemd1", "/Manager",
		       "org.freedesktop.systemd1.Manager", QDBusConnection::systemBus());
	QList<QVariant> arguments;
	arguments.append(args["daemonname"]); // name of the daemon
	arguments.append(false); // disable persistently
	systemdManagerInterface->callWithArgumentList("DisableUnitFiles", arguments)
	return ActionReply::SuccessReply;
}

KDE4_AUTH_HELPER_MAIN("org.chakraproject.org.kapudan.daemon", DaemonHelper)
