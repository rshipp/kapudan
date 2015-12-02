#include "scrFolder.h"
#include <QStandardPaths>
#include <QFileInfo>
#include <QPushButton>

FolderScreen::FolderScreen(QWidget *parent) :QWidget(parent),
  Screen("Folders", "Create folders in the home directory", ":help:", QIcon {}) {
    ui.setupUi(this);

    folderSelected[Download] = true;
    folderSelected[Documents] = true;
    folderSelected[Video] = true;
    folderSelected[Music] = true;
    folderSelected[Picture] = true;

    folder2location[Download] = QStandardPaths::standardLocations(QStandardPaths::DownloadLocation).first();
    folder2location[Documents] = QStandardPaths::standardLocations(QStandardPaths::DocumentsLocation).first();
    folder2location[Video] = QStandardPaths::standardLocations(QStandardPaths::MoviesLocation).first();
    folder2location[Music] = QStandardPaths::standardLocations(QStandardPaths::MusicLocation).first();
    folder2location[Picture] = QStandardPaths::standardLocations(QStandardPaths::PicturesLocation).first();

    QObject::connect(ui.documentsFolderButton, &QPushButton::toggled, [this](bool newState){
        folderSelected[Documents] = newState;
        updateText();
    });

  }

void FolderScreen::updateText() {
    static QString header {
        "<html><head><meta name=\"qrichtext\" content=\"1\" />"
        "<style type=\"text/css\">p, li { white-space: pre-wrap; }</style></head>"
        "<body style=\" font-family:'DejaVu Sans'; font-size:9pt; font-weight:400; font-style:normal;\">"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;"
        "-qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">"
    };
    static QString footer {
        "</span></p></body></html>"
    };

    auto text = header;
    auto any_selected = false;
    for (auto folder_selection: folderSelected) {
        any_selected |= folder_selection.second;
        if (folder_selection.second) {
            text += QFileInfo(folder2location[folder_selection.first]).baseName();
        }
    }
    if (!any_selected) {
        text += "None";
    }
    text += footer;
    ui.textEdit->setText(text);
}
