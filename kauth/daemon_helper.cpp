#include <QDBusInterface>
#include <QDBusConnection>
#include <QDBusMessage>
#include <QStringList>
#include <QDebug>
#include "daemon_helper.h"

ActionReply DaemonHelper::enabledaemon(QVariantMap args)
{
	ActionReply reply;
	QString daemon = args["daemonname"].toString();
	QDBusInterface systemdManager( "org.freedesktop.systemd1", "/org/freedesktop/systemd1",
		       "org.freedesktop.systemd1.Manager", QDBusConnection::systemBus());
	if (!systemdManager.isValid()) {
		reply =  ActionReply::HelperErrorReply;
		reply.setErrorDescription("invalid interface");
		reply.setErrorCode(42);
		return reply;
	}
	 //arguments: name of the daemons, enable persistently, replace symlinks if necessary
	QDBusMessage msg = systemdManager.call(QDBus::Block, "EnableUnitFiles", 
			(QStringList() << args["daemonname"].toString()), false, true);
	if (msg.type() != QDBusMessage::ReplyMessage) {
		reply =  ActionReply::HelperErrorReply;
		reply.setErrorDescription(systemdManager.lastError().message());
		//reply.setErrorDescription("we got an error :-(");
		reply.setErrorCode(43);
		return reply;
	}
	reply = ActionReply::SuccessReply;
	reply.addData("contents", msg.arguments().first());
	return reply;
}

ActionReply DaemonHelper::disabledaemon(QVariantMap args)
{
	ActionReply reply;
	QString daemon = args["daemonname"].toString();
	QDBusInterface systemdManager( "org.freedesktop.systemd1", "/org/freedesktop/systemd1",
		       "org.freedesktop.systemd1.Manager", QDBusConnection::systemBus());
	if (!systemdManager.isValid()) {
		reply =  ActionReply::HelperErrorReply;
		reply.setErrorDescription("invalid interface");
		reply.setErrorCode(42);
		return reply;
	}
	 //arguments: name of the daemons, enable persistently
	QDBusMessage msg = systemdManager.call(QDBus::Block, "DisableUnitFiles", 
			(QStringList() << args["daemonname"].toString()), false);
	if (msg.type() != QDBusMessage::ReplyMessage) {
		reply =  ActionReply::HelperErrorReply;
		reply.setErrorDescription(systemdManager.lastError().message());
		//reply.setErrorDescription("we got an error :-(");
		reply.setErrorCode(43);
		return reply;
	}
	reply = ActionReply::SuccessReply;
	return reply;
}

KDE4_AUTH_HELPER_MAIN("org.chakraproject.kapudan.daemon", DaemonHelper)
