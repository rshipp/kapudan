#include <kauth.h>
#include <QDBusInterface.h>

using namespace KAuth;

class DaemonHelper : pulbic QObject
{
	Q_OBJECT
	
	public slots:
		ActionReply enabledaemon(QVariantMap args);
		ActionReply disabledaemon(QVariantMap args);
	private:
		QDBusInterface systemdManagerInterface;
}
