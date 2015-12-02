#ifndef SCRFOLDER_H_1V3KFXNB
#define SCRFOLDER_H_1V3KFXNB

#include "ui_ui_scrFolder.h"
#include "../screen.h"

#include <QWidget>
#include <QString>
#include <map>

class FolderScreen : public QWidget, public Screen {
  public:
    FolderScreen(QWidget * parent = nullptr);
  private:
    Ui_folderWidget ui;

    enum FolderType {
        Download,
        Documents,
        Video,
        Music,
        Picture
    };

    std::map<FolderType, bool> folderSelected {};
    std::map<FolderType, QString> folder2location {};

    void updateText();


};

#endif /* end of include guard: SCRFOLDER_H_1V3KFXNB */
