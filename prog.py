import sys
import sqlite3
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QComboBox, QLineEdit, QApplication
from PyQt5.QtGui import *


class Hello_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # тут мы создаем окно
        self.setStyleSheet("background-color: rgb(255, 204, 255);")
        self.setGeometry(700, 200, 400, 400)
        self.setWindowTitle('tututu')

        self.text = QLabel(self)
        self.text.setText("""Ингридиенты для блюд""")
        self.text.move(90, 80)
        # добавляем красивый шрифт, размер шрифта
        self.text.setFont(QFont('Times', 12))

        # тут создаем кнопочку
        self.button = QPushButton('Начать!', self)
        # задаем размер и координату
        self.button.resize(200, 150)
        self.button.move(100, 200)
        # добавляем красивый шрифт, размер шрифта
        self.button.setFont(QFont('Times', 12))
        self.button.setStyleSheet('background: rgb(191, 141, 255);')
        # связываем 1 окно со 2
        self.button.clicked.connect(self.show_window_2)

    def show_window_2(self):
        self.w = Window_2()
        self.w.show()


class Window_2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: rgb(255, 204, 255);")
        self.setGeometry(700, 200, 400, 400)
        self.setWindowTitle('tututu')

        self.combo = QComboBox(self)
        self.combo.addItem('суп')
        self.combo.addItem('торт')
        self.combo.addItem('соус')
        self.combo.addItem('напиток')
        self.combo.move(100, 90)
        self.combo.resize(100, 50)

        self.text = QLabel(self)
        self.text.setText("""Что хотите приготовить?""")
        self.text.move(50, 50)
        # добавляем красивый шрифт, размер шрифта
        self.text.setFont(QFont('Times', 12))

        self.btn = QPushButton('Поиск', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(210, 97)
        # добавляем красивый шрифт, размер шрифта
        self.btn.setFont(QFont('Arial', 8))
        self.btn.setStyleSheet('background: rgb(191, 141, 255);')


# проверяющая функция
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Hello_Window()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
