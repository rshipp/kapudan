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

    virtual void shown(){};
    virtual void execute(){};
    virtual void backCheck(){};

    virtual ~Screen() = delete;
};


#endif /* end of include guard: SCREEN_H */
