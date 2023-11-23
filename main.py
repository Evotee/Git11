import sys
import random

from PyQt5 import uic
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.a = False
        self.pushButton.clicked.connect(self.paint)
    def paintEvent(self, event):
        if self.a is True:
           qp = QPainter()
           qp.begin(self)
           self.paint2(qp)
           qp.end()
        self.a = False

    def paint(self):
        self.a = True
        self.repaint()

    def paint2(self, qp):
        a = random.randint(20, 100)
        qp.setBrush(QColor(255, 207, 64))
        qp.drawEllipse(QPointF(300, 200), a, a)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

