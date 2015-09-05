#include "progress_pie.h"
#include <QPaintEvent>
#include <QPainter>
#include <QColor>

ProgressPie::ProgressPie(int totalPiece, QWidget* parent) :QWidget(parent) {
  this->setGeometry(0, 0, 100, 40);
  step = 360 / (totalPiece + 1);
}

void ProgressPie::paintEvent(QPaintEvent * event) {
  QPainter painter {};
  painter.begin(this);
  painter.setRenderHint(QPainter::Antialiasing);
  // pen sets the edge color of the circles
  painter.setPen(QColor(20, 20, 20, 0));

  painter.setBrush(QBrush(QColor(255, 255, 255, 220)));
  auto x = 13;
  auto y = 6;
  auto r = 23;
  auto rect = QRect(x, y, r, r);

  painter.drawEllipse(rect);

  painter.setBrush(QBrush(QColor(20, 20, 20, 100)));

  auto startAngle = 90 * 16;
  auto spanAngle = -((this->currentPiece * this->step) * 16);

  painter.drawPie(rect, startAngle, spanAngle);

  painter.end();
}

void ProgressPie::updatePie(int currentIndex) {
  currentPiece = currentIndex + 1;
  this->update();
}
