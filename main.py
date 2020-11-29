import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def run(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        radiys = int(randint(10, 200))
        qp.drawEllipse(QPoint(200, 200), radiys, radiys)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.run(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())