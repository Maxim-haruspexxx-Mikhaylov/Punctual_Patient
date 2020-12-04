import toga
from toga.style import *
from toga.style.pack import *


class Window(toga.App):
    def __init__(self):
        super().__init__(app_id, name)

    def startup(self):
        self.main_box = toga.Box()
        self.box1 = toga.Box()
        self.box2 = toga.Box()
        self.box3 = toga.Box()
        self.box4 = toga.Box()

        self.main_window = toga.MainWindow(title='Пациент')
        self.main_window.content = self.main_box
        self.main_window.show()

        self.number = '2401'

        self.label1 = toga.Label(self.number)
        self.label1.style.width = 30
        self.label1.style.font_size = 5
        self.label1.style.padding_top = 30
        self.label1.style.padding_right = 175
        self.label1.style.padding_left = 175
        self.label1.style.update(alignment=CENTER)

        self.label2 = toga.Label('Ожидаемое время приёма - 10:00')
        self.label2.style.width = 200
        self.label2.style.font_size = 5
        self.label2.style.padding_top = 30
        self.label2.style.padding_left = 100
        self.label2.style.padding_right = 100
        self.label2.style.update(background_color='green')

        self.label2.style.update(alignment=CENTER)

        self.label2.style.flex = 1

        button1 = toga.Button('Встать в очередь', on_press=Window.get_number)
        button1.style.width = 300
        button1.style.height = 60
        button1.style.padding_top = 30
        button1.style.padding_left = 40
        button1.style.padding_right = 50
        button1.style.padding_bottom = 5
        button1.style.flex = 1

        button2 = toga.Button('Выйти из очереди', on_press=Window.get_number)
        button2.style.width = 300
        button2.style.height = 60
        button2.style.padding_top = 5
        button2.style.padding_left = 40
        button2.style.padding_right = 50
        button2.style.padding_bottom = 40
        button2.style.flex = 1

        self.box1.add(self.label1)
        self.main_box.add(self.box1)
        self.box2.add(self.label2)
        self.main_box.add(self.box2)
        self.box3.add(button1)
        self.main_box.add(self.box3)
        self.box4.add(button2)
        self.main_box.add(self.box4)

        self.main_box.style.update(direction=COLUMN)

        return self.main_box

    def get_number(self):
        print('2401')
        self.number = '2401'
#        Window.show_number(self, self.number)

#    def show_number(self, num):


def main():
    return toga.App('Patient', 'org.beeware.patient', startup=Window.startup)


if __name__ == '__main__':
    main().main_loop()






