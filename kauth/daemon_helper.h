#ifndef DAEMON_HELPER_H
#define DAEMON_HELPER_H

#include <kauth.h>

#include <QDBusInterface>

using namespace KAuth;

class DaemonHelper : public QObject
{
	Q_OBJECT
	
	public slots:
		ActionReply enabledaemon(QVariantMap args);
		ActionReply disabledaemon(QVariantMap args);
};

#endif
