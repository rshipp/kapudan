#include <experimental/optional>

#include <QtCore>
#include <QObject>
#include <QApplication>
#include <QStackedWidget>
#include <QString>
#include <QMainWindow>
#include <QDesktopWidget>

#include <KSharedConfig>

#include "kapudan.h"
#include "progress_pie.h"

#include "screens.h"

struct GlobalState {
  std::experimental::optional<void*> screenData;
  int moveInc =1;
  QString menuText;
  QStringList titles;
  QStringList descriptions;
  QString currentDir;
  KSharedConfigPtr plasmaConfig;
};

void centerWindow(QWidget* window)
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
   : QWidget(parent)
{
    ui.setupUi(this);

    // add screens
    ui.mainStack->removeWidget(ui.page);
    ui.mainStack->addWidget(new WelcomeScreen {});
    ui.mainStack->addWidget(new FolderScreen {});

    // draw progress pie
    // TODO: there's a terrible inversion of control here...
    auto pie = new ProgressPie(ui.mainStack->count(), this->ui.labelProgress);
    (void) pie;

    // connect signals
    QObject::connect(ui.buttonNext, &QPushButton::clicked, this, &KapudanMainWindow::forward);
    QObject::connect(ui.buttonBack, &QPushButton::clicked, this, &KapudanMainWindow::back);
}

void KapudanMainWindow::forward() {
  ui.mainStack->setCurrentIndex(ui.mainStack->currentIndex()+1);
}

void KapudanMainWindow::back() {
  ui.mainStack->setCurrentIndex(ui.mainStack->currentIndex()-1);
}


int main(int argc, char *argv[])
{
  QApplication app(argc, argv);
  app.setAttribute(Qt::AA_UseHighDpiPixmaps, true);
  app.setApplicationName("kapudan");

  KapudanMainWindow *mw = new KapudanMainWindow();
  centerWindow(mw);

  mw->show();

  return app.exec();
}
