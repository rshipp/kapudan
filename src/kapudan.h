#include <QMainWindow>
#include "ui_ui_kapudan.h"

#include "screens.h"

#include <vector>

class KapudanMainWindow : public QWidget
{
      Q_OBJECT
      public:
         explicit KapudanMainWindow(QWidget *parent = 0);
         ~KapudanMainWindow() {}

      private:
         Ui_kapudan ui;
         void forward();
         void back();
};
