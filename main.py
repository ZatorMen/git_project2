import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow


class Circle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUi()

    def initUi(self):
        self.pushButton.clicked.connect(self.repaint)

    def paintEvent(self, event):
        r = random.randint(20, 150)
        qp = QPainter()
        qp.begin(self)
        color = QColor(255, 255, 0)
        qp.setBrush(color)
        qp.drawEllipse(125, 150, r, r)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())
