#include <kauth.h>

using namespace KAuth;

class DaemonHelper : pulbic QObject
{
	Q_OBJECT
	
	public slots:
		ActionReply checkdaemon(QVariantMap args);
		ActionReply enabledaemon(QVariantMap args);
		ActionReply disabledaemon(QVariantMap args);
}
