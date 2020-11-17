from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randrange
import sys


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.key = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.key = True

    def paintEvent(self, event):
        if self.key:
            qp = QPainter(self)
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            r = randrange(1, 150)
            x = randrange(1, 420)
            y = randrange(1, 450)
            qp.drawEllipse(x, y, r, r)
            self.key = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())