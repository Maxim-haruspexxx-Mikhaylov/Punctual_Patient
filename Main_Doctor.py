import sys
import csv
from PyQt5.QtGui import QPixmap, QImage, QColor, QTransform, qRgb, QFont, QKeySequence, QKeyEvent
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QFileDialog, QAction, QWidget, \
    QTableWidgetItem, QAbstractItemView
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtCore import Qt, QTimer, QTime
import time


class Doctor(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Doctor_main_design.ui', self)

        self.open_table()

        self.clock = QTimer(self)
        self.clock.timeout.connect(self.time_update)
        self.clock.start(1000)

        self.time_app = 0
        self.time_app_interval = 1000
        self.time_app = QTimer()
        self.time_update()
        self.time_app.setInterval(self.time_app_interval)
        self.time_app.timeout.connect(self.update_uptime)

    def time_update(self):
        current_time = QTime.currentTime()
        time_on_display = current_time.toString('hh:mm')
        self.label_clock.setText(time_on_display)

    def update_uptime(self):
        self.time += 1
        self.set_timer(self.time)

    def set_timer(self, num):
        self.time_app = num
        self.label_timer_app.setText(time.strftime('%M:%S', time.gmtime(self.time_app)))

    def open_table(self):
        with open('appointments_eng.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            title = next(reader)
            self.table_widget.setColumnCount(3)
            self.table_widget.setHorizontalHeaderLabels(title)
            self.table_widget.setRowCount(0)
            for i, row in enumerate(reader):
                self.table_widget.setRowCount(
                    self.table_widget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.table_widget.setItem(
                        i, j, QTableWidgetItem(elem))
        self.table_widget.resizeColumnsToContents()
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Doctor()
    win.setFixedSize(730, 861)
    win.show()
    sys.exit(app.exec_())
