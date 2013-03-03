#include <QDBusInterface>
#include <QDBusConnection>
#include "daemon_helper.h"

ActionReply DaemonHelper::enabledaemon(QVariantMap args)
{
	ActionReply reply;
	QString daemon = args["daemonname"].toString();
	QDBusInterface systemdManager( "org.freedesktop.systemd1", "/Manager",
		       "org.freedesktop.systemd1.Manager", QDBusConnection::systemBus());
	if (!systemdManager.isValid()) {
		reply =  ActionReply::HelperErrorReply;
		reply.setErrorDescription("invalid interface");
		reply.setErrorCode(42);
		return reply;
	}
	QList<QVariant> arguments;
	arguments.append(args["daemonname"]); // name of the daemon
	arguments.append(false); // enable persistently
	arguments.append(true); // replace symlinks if necessary
	QDBusMessage msg = systemdManager.callWithArgumentList(QDBus::Block, "EnableUnitFiles", arguments);
	if (msg.type() != QDBusMessage::ReplyMessage) {
		reply =  ActionReply::HelperErrorReply;
		//reply.setErrorDescription(systemdManager.lastError().message());
		reply.setErrorDescription("we got an error :-(");
		reply.setErrorCode(43);
		return reply;
	}
	reply = ActionReply::SuccessReply;
	reply.addData("contents", msg.arguments());
	reply.addData("number", 1);
	return reply;
}

ActionReply DaemonHelper::disabledaemon(QVariantMap args)
{
	QString daemon = args["daemonname"].toString();
	QDBusInterface systemdManager( "org.freedesktop.systemd1", "/Manager",
		       "org.freedesktop.systemd1.Manager", QDBusConnection::systemBus());
	QList<QVariant> arguments;
	arguments.append(args["daemonname"]); // name of the daemon
	arguments.append(false); // disable persistently
	systemdManager.callWithArgumentList(QDBus::Block, "DisableUnitFiles", arguments);
	return ActionReply::SuccessReply;
}

KDE4_AUTH_HELPER_MAIN("org.chakraproject.org.kapudan.daemon", DaemonHelper)
