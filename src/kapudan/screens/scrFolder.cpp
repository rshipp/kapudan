#include "scrFolder.h"

FolderScreen::FolderScreen(QWidget *parent) :QWidget(parent),
  Screen("Folders", "Create folders in the home directory", ":help:", QIcon {}) {
    ui.setupUi(this);
  }
