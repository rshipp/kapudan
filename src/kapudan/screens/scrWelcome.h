#ifndef SCRWELCOME_H
#define SCRWELCOME_H

#include "ui_ui_scrWelcome.h"
#include "../screen.h"

#include <QWidget>

class WelcomeScreen : public QWidget, public Screen {
  public:
    WelcomeScreen(QWidget * parent = nullptr);
  private:
    Ui_welcomeWidget ui;


};


#endif /* end of include guard: SCRWELCOME_H */
