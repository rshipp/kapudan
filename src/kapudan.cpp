#include <experimental/optional>

#include <QtCore>
#include <QApplication>
#include <QString>
#include <QMainWindow>
#include <QDesktopWidget>

#include <KSharedConfig>

#include "kapudan.h"

struct GlobalState {
  std::experimental::optional<void*> screenData;
  int moveInc =1;
  QString menuText;
  QStringList titles;
  QStringList descriptions;
  QString currentDir;
  KSharedConfigPtr plasmaConfig;
};


void centerWindow(QMainWindow* window)
{
    // center window
    auto rect = QDesktopWidget().screenGeometry();
    auto width = 0;
    auto height = 0;

    if (rect.width() <= 640) {
      width = 620;
    } else if (rect.width() <= 800) {
      width = 720;
    } else {
      width = 960;
    }

    if (rect.height() <= 480) {
      height = 450;
    } else if (rect.height() <= 600) {
      height = 520;
    } else {
      height = 680;
    }

    window->resize(width, height);
    window->move(rect.width() / 2 - window->width() / 2,
                 rect.height() / 2 - window->height() / 2);
}


KapudanMainWindow::KapudanMainWindow(QWidget* parent)
   : QMainWindow(parent)
{
    ui.setupUi(this);
}


int main(int argc, char *argv[])
{
  QApplication app(argc, argv);
  app.setAttribute(Qt::AA_UseHighDpiPixmaps, true);

  KapudanMainWindow *mw = new KapudanMainWindow();
  centerWindow(mw);
  
  mw->show();

  return app.exec();
}
