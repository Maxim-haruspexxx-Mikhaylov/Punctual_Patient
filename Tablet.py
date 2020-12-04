import datetime as dt
import sys
import csv
import sqlite3
from PyQt5.QtGui import QPixmap, QImage, QColor, QTransform, qRgb, QFont
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QFileDialog, QAction, QWidget, \
    QTableWidgetItem, QAbstractItemView
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtCore import Qt, QTimer, QTime
import time
import Main_Doctor as md


class Tablet(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Stationary_tablet_design.ui', self)
        self.con = sqlite3.connect("Appointments.db")
        self.cur = self.con.cursor()
        self.cabinet_num = '24'

        self.query = 'SELECT Number, Time FROM apps'
        self.button_get_in_queue.clicked.connect(self.make_appointment)

        self.patient_num = 1
        self.average_time = 600
        self.open_table()

        self.clock = QTimer()
        self.clock.timeout.connect(self.update_time)
        self.clock.start(1)

    def update_time(self):
        self.current_time = QTime.currentTime()
        time_on_display = self.current_time.toString('hh:mm')
        self.label_clock.setText(time_on_display)

    def update_patients_num(self):
        self.label_patients_num.setNum(self.patients_num)

    def make_appointment(self):
        if self.patient_num // 10 == 0:
            num_for_table = '0' + str(self.patient_num)
        else:
            num_for_table = str(self.patient_num)
        self.time_for_app += self.average_time // 60
        if self.time_for_app % 60 // 10:
            app_time = f'{self.time_for_app // 60}:{self.time_for_app % 60}'
        else:
            app_time = f'{self.time_for_app // 60}:{"0" + str(self.time_for_app % 60)}'
            print('ok')
        self.add_appointment(num_for_table, app_time)

    def add_appointment(self, num_for_table, time_for_patient):
        self.cur.execute('INSERT INTO apps VALUES(?, ?)', (self.cabinet_num + num_for_table, time_for_patient))
        self.open_table()

    def open_table(self):
        res = self.con.cursor().execute(self.query).fetchall()
        self.table_view.setColumnCount(2)
        self.table_view.setRowCount(0)
        self.table_view.setHorizontalHeaderLabels(['Номер', 'Время'])
        for i, row in enumerate(res[1:]):
            self.table_view.setRowCount(
                self.table_view.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table_view.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.table_view.resizeColumnsToContents()
        self.table_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Tablet()
    win.setFixedSize(789, 475)
    win.show()
    sys.exit(app.exec_())