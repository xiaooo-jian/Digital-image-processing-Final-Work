import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QDesktopWidget, QLabel, QLineEdit, QFormLayout)
from qtpy import QtCore


class Example(QWidget):

    def __init__(self):
        self.card = {"王": 2, "2": 4, "A": 4, "K": 4, "Q": 4, "J": 4, "10": 4, "9": 4, "8": 4, "7": 4, "6": 4, "5": 4,
                     "4": 4, "3": 4}
        super().__init__()

        self.initUI()

    def center(self):
        # 获得窗口
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        start = QPushButton("开始")
        screen = QPushButton("截取")

        start.clicked.connect(self.start)
        screen.clicked.connect(self.screenshot)

        button_box = QHBoxLayout()
        button_box.addStretch(1)
        button_box.addWidget(start)
        button_box.addWidget(screen)

        vbox = QVBoxLayout()
        card = QLabel("牌型： 王 | 2 | A | K | Q | J | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 ")
        number = QLabel(self.getcard())

        vbox.addWidget(card)
        vbox.addWidget(number)
        vbox.addStretch(1)
        vbox.addLayout(button_box)

        self.setLayout(vbox)
        self.resize(570, 100)
        self.setWindowTitle('记牌器')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.center()
        self.show()

    def start(self):
        self.card = {"王": 2, "2": 4, "A": 4, "K": 4, "Q": 4, "J": 4, "10": 4, "9": 4, "8": 4, "7": 4, "6": 4, "5": 4,
                     "4": 4, "3": 4}

        print("start")

    def screenshot(self):
        self.card = {"王": 2, "2": 2, "A": 4, "K": 4, "Q": 4, "J": 4, "10": 4, "9": 4, "8": 4, "7": 4, "6": 4, "5": 4,
                     "4": 4, "3": 2}
        QApplication.processEvents()
        print("screen")

    def getcard(self):
        return "数量：  {} | {} | {} | {} | {} | {} |  {} | {} | {} | {} | {} | {} | {} | {} ".format(
            self.card['王'], self.card["2"], self.card["A"], self.card["K"], self.card["Q"], self.card["J"],
            self.card["10"],self.card["9"], self.card["8"], self.card["7"], self.card["6"], self.card["5"],
            self.card["4"], self.card["3"])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
