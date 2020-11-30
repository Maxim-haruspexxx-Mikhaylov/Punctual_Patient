import datetime
import sys
import csv
from PyQt5.QtGui import QPixmap, QImage, QColor, QTransform, qRgb, QFont, QKeySequence, QKeyEvent
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QFileDialog, QAction, QWidget, \
    QTableWidgetItem, QAbstractItemView
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtCore import Qt, QTimer
import time


class Doctor(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Doctor_main_design.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Doctor()
    win.show()
    sys.exit(app.exec_())
