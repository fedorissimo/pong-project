from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QPlainTextEdit, QVBoxLayout, QCheckBox, \
    QMainWindow, QComboBox
from pong2 import Ui_MainWindow
import sys
import os


class PongInterface(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.col1 = 'black'
        self.col2 = 'black'
        self.fps = 60
        self.pushButton.clicked.connect(self.start)

    def start(self):
        self.col1 = self.comboBox.currentText()
        self.col2 = self.comboBox_2.currentText()
        self.fps = self.spinBox.text()
        writer = open('settings.txt', 'w')
        writer.write(self.col1 + '\n' + self.col2 + '\n' + self.fps)
        writer.close()
        os.startfile(r'mainpong.py')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PongInterface()
    win.show()
    sys.exit(app.exec())
