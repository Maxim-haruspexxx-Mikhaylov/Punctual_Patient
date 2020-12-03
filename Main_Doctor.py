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

        self.app_started = False
        self.app_stopped = False

        self.patients_num = 0
        self.update_patients_num()

        self.clock = QTimer()
        self.clock.timeout.connect(self.update_time)
        self.clock.start(1)

        self.time_app = 0
        self.time_interval = 1000
        self.timer_up = QTimer()
        self.timer_up.setInterval(self.time_interval)
        self.timer_up.timeout.connect(self.update_uptime)
        self.button_start_finish.clicked.connect(self.appointment_clicked)

        self.average_time = 600
        self.all_time = 600
        self.expected_time = self.average_time
        self.update_average_time()
        self.update_expected_time()

        self.extension_time = 300
        self.button_extend_app.clicked.connect(self.extend_expected_time)

        self.leaving_time = 180
        self.button_leave.clicked.connect(self.leave)

    def update_uptime(self):
        self.time_app += 1
        self.label_timer_app.setText(time.strftime('%M:%S', time.gmtime(self.time_app)))

    def update_time(self):
        current_time = QTime.currentTime()
        time_on_display = current_time.toString('hh:mm')
        self.label_clock.setText(time_on_display)

    def update_patients_num(self):
        self.label_patients_num.setNum(self.patients_num)

    def add_to_average_time(self):
        self.all_time += self.time_app
        self.average_time = self.all_time // (self.patients_num + 1)
        print(self.average_time)
        self.update_average_time()

    def update_average_time(self):
        if self.average_time % 60:
            self.label_average_time.setText(f'{self.average_time // 60} мин {self.average_time % 60} сек')
        else:
            self.label_average_time.setText(f'{self.average_time // 60} мин')

    def update_expected_time(self):
        self.label_expected_time.setText(time.strftime('%M:%S', time.gmtime(self.expected_time)))

    def extend_expected_time(self):
        self.expected_time += self.extension_time
        self.update_expected_time()

    def appointment_clicked(self):
        if self.app_started:
            self.finish_appointment()
        else:
            self.start_appointment()

    def start_appointment(self):
        self.button_start_finish.setText('Завершить приём')
        self.timer_up.start()
        self.app_started = True

    def finish_appointment(self):
        self.timer_up.stop()
        self.patients_num += 1
        self.add_to_average_time()
        self.time_app = 0
        self.label_timer_app.setText(time.strftime('%M:%S', time.gmtime(self.time_app)))
        self.update_patients_num()
        self.expected_time = self.average_time
        self.update_expected_time()
        self.button_start_finish.setText('Начать следующий приём')
        self.app_started = False

    def leave(self):
        if self.app_stopped:
            self.timer_up.start()
            self.app_stopped = False
            self.app_started = True
            self.button_leave.setText('Отлучиться (3 мин)')
        elif self.app_started:
            self.timer_up.stop()
            self.app_stopped = True
            self.app_started = False
            self.button_leave.setText('Вернуться к работе')

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
