from PyQT5.QTCore import QT
from PyQT5.Widgets import (
    QApplication,QWidget,
    QHBoxLayout,QVBoxLayout,
    QGroupBox,QRadioButton,
    QPushButton,QLabel,QListWidget,QLineEdit)

from instr import *
class FinalWin(QWidget)
    def __init__(self):

        super().__init__()

        self.initUI()
        self.set_appear()

    def initUI(self):
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)


        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, aligment = QT.AlignCenter)
        self.layout_line.addWidget(self.workh_text, aligment = QT.AlignCenter)
        self.setLayout(self.layout_line)
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)