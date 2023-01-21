from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QPlainTextEdit, QVBoxLayout, QCheckBox, \
    QMainWindow, QComboBox
from pong2 import Ui_MainWindow
import sys


class PongInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.col1 = 'black'
        self.col2 = 'black'
        self.fps = 60
        self.pushButton.clicked.connect(self.start)

    def start(self):
        self.col1 = self.comboBox.text()
        self.col2 = self.comboBox_2.text()
        self.fps = int(self.spinBox.text())
        print('a')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PongInterface()
    win.show()
    sys.exit(app.exec())
