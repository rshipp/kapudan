#ifndef SCRFOLDER_H_1V3KFXNB
#define SCRFOLDER_H_1V3KFXNB

#include "ui_ui_scrFolder.h"
#include "../screen.h"

#include <QWidget>

class FolderScreen : public QWidget, public Screen {
  public:
    FolderScreen(QWidget * parent = nullptr);
  private:
    Ui_folderWidget ui;
};

#endif /* end of include guard: SCRFOLDER_H_1V3KFXNB */
