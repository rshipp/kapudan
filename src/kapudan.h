#include <QMainWindow>
#include "ui_ui_kapudan.h"

class KapudanMainWindow : public QMainWindow
{
      Q_OBJECT
      public:
         explicit KapudanMainWindow(QWidget *parent = 0);
         ~KapudanMainWindow() {};

      private:
         Ui_kapudan ui;
};
