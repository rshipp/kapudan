#ifndef MENU_H
#define MENU_H

#include "QString"
#include "QList"
#include <QLabel>

struct Menu {
  Menu(QStringList titles,  QLabel* label) {
    this->titles = titles;
    this->label = label;
  }

  QStringList titles;
  QLabel* label;

  auto bold = "font-weight:bold";
  auto normal = "font-weight:normal";
  auto defaultFontSize = 10;
  auto position = 0;
  auto menuText = "";
  auto menuNode = " <span style='font-size:%spt; %s'>%s</span> ";
  auto seperatorL = "<span style='font-size:11pt'><img src=':/raw/pixmap/menu-arrow-left.png'></span>";
  auto seperatorR = "<span style='font-size:11pt'><img src=':/raw/pixmap/menu-arrow-right.png'></span>";
};

#endif /* end of include guard: MENU_H */
