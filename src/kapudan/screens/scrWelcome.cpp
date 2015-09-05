#include "scrWelcome.h"

WelcomeScreen::WelcomeScreen(QWidget *parent) : QWidget(parent),
    Screen("Welcome", "Welcome to ", ":help:", QIcon {} ) {
      ui.setupUi(this);
    }
