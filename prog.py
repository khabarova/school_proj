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
        self.setGeometry(700, 200, 800, 800)
        self.setWindowTitle('tututu')

        self.spis = ['СУП', 'ТОРТ', 'СОУС', 'НАПИТОК']
        self.ell = [QCheckBox(self) for _ in self.spis]
        for i in range(len(self.ell)):
            self.ell[i].setText(self.spis[i])
            self.ell[i].move(500, 40 * i)
            self.ell[i].setFont(QFont('Times', 8))


        self.text = QLabel(self)
        self.text.setText("""Что хотите приготовить?""")
        self.text.move(50, 50)
        self.text.setFont(QFont('Times', 12))

        self.field = QPlainTextEdit(self)
        self.field.setGeometry(10, 150, 700, 500)
        self.field.setEnabled(False)

        self.btn = QPushButton('Поиск', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(210, 97)
        # добавляем красивый шрифт, размер шрифта
        self.btn.setFont(QFont('Times', 8))
        self.btn.setStyleSheet('background: rgb(191, 141, 255);')
        self.btn.clicked.connect(self.app)

    def app(self):
        self.field.clear()
        prov = [i.text() for i in self.ell if i.isChecked()]
        prov.insert(0, "")
        for elem in prov:
            # подключения бд
            # делаем запрос в бд и выводим результат в окно виджета
            self.field.appendPlainText(f'{elem}')
            con = sqlite3.connect('base.db')
            cur = con.cursor()
            result = cur.execute(f'''SELECT dish FROM dishes WHERE what = "{elem.lower()}"''').fetchall()
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
