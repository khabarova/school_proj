import sys
import sqlite3
from PyQt5.QtWidgets import *
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
        self.text.setText("""Справочник ингредиентов для блюд""")
        self.text.move(40, 80)
        # добавляем красивый шрифт, размер шрифта
        self.text.setFont(QFont('Times', 12))

        # создаем кнопочку
        self.button = QPushButton('Начать!', self)
        # задаем размер и координату
        self.button.resize(200, 150)
        self.button.move(100, 200)
        self.button.setFont(QFont('Times', 12))
        self.button.setStyleSheet('background: rgb(191, 141, 255);')
        # связываем 1 окно со 2
        self.button.clicked.connect(self.show_window_2)

    def show_window_2(self):
        self.w = Window_2()
        self.w.show()
        self.close()


class Window_2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: rgb(255, 204, 255);")
        self.setGeometry(700, 200, 770, 600)
        self.setWindowTitle('tututu')

        self.but1 = QPushButton('Суп', self)
        self.but1.resize(self.but1.sizeHint())
        self.but1.move(500, 40)
        self.but1.setFont(QFont('Times', 8))
        self.but1.setStyleSheet('background: rgb(191, 141, 255);')
        self.but1.clicked.connect(self.app1)

        self.but2 = QPushButton('Торт', self)
        self.but2.resize(self.but2.sizeHint())
        self.but2.move(500, 80)
        self.but2.setFont(QFont('Times', 8))
        self.but2.setStyleSheet('background: rgb(191, 141, 255);')
        self.but2.clicked.connect(self.app2)

        self.but3 = QPushButton('Соус', self)
        self.but3.resize(self.but3.sizeHint())
        self.but3.move(600, 40)
        self.but3.setFont(QFont('Times', 8))
        self.but3.setStyleSheet('background: rgb(191, 141, 255);')
        self.but3.clicked.connect(self.app3)

        self.but4 = QPushButton('Напиток', self)
        self.but4.resize(self.but4.sizeHint())
        self.but4.move(600, 80)
        self.but4.setFont(QFont('Times', 8))
        self.but4.setStyleSheet('background: rgb(191, 141, 255);')
        self.but4.clicked.connect(self.app4)

        self.text = QLabel(self)
        self.text.setText("""Что хотите приготовить?""")
        self.text.move(50, 50)
        self.text.setFont(QFont('Times', 12))

        self.field = QPlainTextEdit(self)
        self.field.setGeometry(10, 150, 750, 400)
        self.field.setEnabled(False)

    def app1(self):
        self.field.clear()
        self.field.appendPlainText('СУП')
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        result = cur.execute(f'''SELECT dish FROM dishes WHERE what = "суп"''').fetchall()
        # добавляем результаты запроса в QComboBox, для корректного выбора поликлиники
        for j in result:
            self.field.appendPlainText('\n'.join(j))
        con.close()

    def app2(self):
        self.field.clear()
        self.field.appendPlainText('ТОРТ')
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        result = cur.execute(f'''SELECT dish FROM dishes WHERE what = "торт"''').fetchall()
        # добавляем результаты запроса в QComboBox, для корректного выбора поликлиники
        for j in result:
            self.field.appendPlainText('\n'.join(j))
        con.close()

    def app3(self):
        self.field.clear()
        self.field.appendPlainText('СОУС')
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        result = cur.execute(f'''SELECT dish FROM dishes WHERE what = "соус"''').fetchall()
        # добавляем результаты запроса в QComboBox, для корректного выбора поликлиники
        for j in result:
            self.field.appendPlainText('\n'.join(j))
        con.close()

    def app4(self):
        self.field.clear()
        self.field.appendPlainText('НАПИТОК')
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        result = cur.execute(f'''SELECT dish FROM dishes WHERE what = "напиток"''').fetchall()
        # добавляем результаты запроса в QComboBox, для корректного выбора поликлиники
        for j in result:
            self.field.appendPlainText('\n'.join(j))
        con.close()


# проверяющая функция
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Hello_Window()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
