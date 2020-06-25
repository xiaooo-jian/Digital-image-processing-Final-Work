import sys

import PyWinMouse as mouse
from PyQt5.QtCore import Qt, QCoreApplication, QTimer
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QDesktopWidget, QLabel)
from qtpy import QtCore
import MainFunction as mf


class Window(QWidget):

    def __init__(self):
        self.card = {"王": 2, "2": 4, "A": 4, "K": 4, "Q": 4, "J": 4, "10": 4, "9": 4, "8": 4, "7": 4, "6": 4, "5": 4,
                     "4": 4, "3": 4}
        super().__init__()
        self.setWindowTitle('记牌器')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.center()

        start = QPushButton("开始")
        screen = QPushButton("截取")
        quits = QPushButton("退出")

        start.clicked.connect(self.start)
        screen.clicked.connect(self.screenshot)
        quits.clicked.connect(QCoreApplication.instance().quit)

        button_box = QHBoxLayout()
        button_box.addStretch(1)

        button_box.addWidget(start)
        button_box.addWidget(screen)
        button_box.addWidget(quits)

        self.vbox = QVBoxLayout()
        card = QLabel("牌型： 王 | 2 | A | K | Q | J | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 ")
        self.number = QLabel(self.getcard())

        self.vbox.addWidget(card)
        self.vbox.addWidget(self.number)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.vbox.addLayout(button_box)
        self.setLayout(self.vbox)
        self.resize(570, 100)

    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handleDisplay(self):
        self.number.setText(self.getcard())
        QApplication.processEvents()

    def start(self):
        self.card = mf.HandCardRegnziion()
        self.handleDisplay()
        print("start")

    def screenshot(self):
        self.card = mf.OutCardRegnziion(self.card)
        self.handleDisplay()
        print("screen")

    def getcard(self):
        return "数量：  {} | {} | {} | {} | {} | {} |  {} | {} | {} | {} | {} | {} | {} | {} ".format(
            self.card['王'], self.card["2"], self.card["A"], self.card["K"], self.card["Q"], self.card["J"],
            self.card["10"], self.card["9"], self.card["8"], self.card["7"], self.card["6"], self.card["5"],
            self.card["4"], self.card["3"])


    # 因为边框去掉了，为了能拖动，只能重写一下鼠标事件了
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            e.accept()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False

    def mouseMoveEvent(self, e):
        if Qt.LeftButton and self.m_drag:
            self.move(e.globalPos() - self.m_DragPosition)
            e.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wd = Window()
    wd.show()
    sys.exit(app.exec_())
