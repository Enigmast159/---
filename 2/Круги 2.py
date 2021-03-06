from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_Form
from random import randrange
import sys


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.key = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.key = True
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        r = randrange(1, 150)
        x = randrange(1, 420)
        y = randrange(1, 450)
        if self.key:
            qp.drawEllipse(x, y, r, r)
        self.key = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())