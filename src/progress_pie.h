#ifndef PROGRESS_PIE_H
#define PROGRESS_PIE_H

#include <QWidget>

class QPaintEvent;

class ProgressPie : QWidget
{
public:
  ProgressPie (int totalPiece, QWidget* parent);
  void paintEvent(QPaintEvent * event) override;
  void updatePie(int currentIndex);

private:
  int currentPiece = 1;
  double step = 1;
};

#endif /* end of include guard: PROGRESS_PIE_H */
