#ifndef SCREEN_H
#define SCREEN_H

#include <QString>
#include <QIcon>

class  Screen {
  public:
    QString title;
    QString desc;
    QString help;
    QIcon icon;

    Screen(QString title, QString desc, QString help, QIcon icon) {
      this->title = title;
      this->desc = desc;
      this->help = help;
      this->icon = icon;
    }
    virtual void shown(){};
    virtual void execute(){};
    virtual void backCheck(){};

    virtual ~Screen() {};
};


#endif /* end of include guard: SCREEN_H */
