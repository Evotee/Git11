import sys
import random

from PyQt5 import uic
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitld.ui', self)
    def paintEvent(self):
        qp = QPainter()
        qp.begin(self)
        self.paint2(qp)

    def paint(self):
        self.repaint()

    def paint2(self, qp):
        a = random.randint(20, 100)
        qp.setBrush(QColor('yellow'))
        qp.drawEllipse(QPointF(200, 200), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
