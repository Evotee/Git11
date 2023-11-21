import sys
import random

from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor


class Suprematism1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Суперматизм')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.paint2(qp)

    def paint(self):
        self.repaint()

    def paint2(self, qp):
        a = random.randint(20, 100)
        c1 = random.randint(0, 255)
        c2 = random.randint(0, 255)
        c = random.randint(0, 255)
        qp.setBrush(QColor(c, c1, c2))
        qp.drawEllipse(QPointF(200, 200), a, a)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication1(sys.argv)
    ex = Suprematism1()
    ex.show()
    sys.excepthook = except_hook
    print()
    sys.exit(app.exec())
