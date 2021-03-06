# -*- coding: utf-8 -*-

# Инструкция по созданию https://pythonworld.ru/gui/pyqt5-firstprograms.html
# Ещё одно руководство https://pythonist-ru.turbopages.org/pythonist.ru/s/rukovodstvo-po-pyqt5/

# Импорты. Основные виджеты расположены в PyQt5.QtWidgets
import sys
from PyQt5.QtWidgets import * #Чтобы не париться)
#from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
#from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication)
from PyQt5.QtGui import QIcon #для иконки окошка
from PyQt5.QtCore import QCoreApplication #для кнопки выхода

# Класс QtWidgets.QDesktopWidget предоставляет информацию о компьютере пользователя, в том числе о размерах экрана.

"""
#Процедурный подход (для примера)
if __name__ == '__main__':

    app = QApplication(sys.argv) #Каждое приложение PyQt5 должно создать объект приложения (экземпляр QApplication). Параметр sys.argv это список аргументов командной строки.

    w = QWidget() #Виджет QWidget это базовый класс для всех объектов интерфейса пользователя в PyQt5. 
        #Мы предоставляем конструктор по умолчанию для QWidget. Конструктор по умолчанию не имеет родителя. Виджет без родителей называется окно.

    w.resize(500, 350) #Метод resize() изменяет размеры виджета.

    w.move(800, 150) #Метод move() двигает виджет на экране на координату x, y.

    w.setWindowTitle('Длинная линия') #Здесь мы задаём заголовок нашего окна.

    w.show() #Метод show() отображает виджет на экране. 
        #Виджет сначала создаётся в памяти, и только потом (с помощью метода show) показывается на экране.

    sys.exit(app.exec_()) #Наконец, мы попадаем в основной цикл приложения. Обработка событий начинается с этой точки. 
        #Основной цикл получает события от оконной системы и распределяет их по виджетам приложения. 
        #Основной цикл заканчивается, если мы вызываем метод exit() или главный виджет уничтожен. 
        #Метод sys.exit() гарантирует чистый выход. Вы будете проинформированы, как завершилось приложение.
        #Метод exec_ () имеет подчеркивание. Это происходит потому, что exec является ключевым словом в python 2.
"""

class Example(QWidget):

    def __init__(self):
        super().__init__()
            #Здесь мы создаем новый класс Example. Класс Example наследуется от класса QWidget. 
            #Это означает, что мы вызываем два конструктора: первый для класса Example и второй для родительского класса. 
            #Функция super() возвращает родительский объект Example с классом, и мы вызываем его конструктор.
        self.initUI() 
            
     #Создание GUI делегируется методу initUI().
    def initUI(self):
        #Все три метода унаследованы от класса QWidget:
        #self.setGeometry(800, 150, 500, 350) 
                #Метод setGeometry() делает две вещи: помещает окно на экране и устанавливает его размер. 
                #Первые два параметра х и у - это позиция окна. 
                #Третий - ширина, и четвертый - высота окна. На самом деле, он сочетает в себе методы resize() и move() в одном методе.
        self.resize(500, 350)
        self.center() #Устанавливает положение окна по центру с помощью метода, описанного ниже

        self.setWindowTitle('Длинная линия') #Метод устанавливает заголовок приложения. 
        self.setWindowIcon(QIcon('WindowIcon1.png'))#Чтобы установить иконку, создаём объект QIcon. QIcon получает путь к нашей иконке для отображения.

        qbtn = QPushButton('Выход', self)
        qbtn.clicked.connect(self.closeEvent)  #Выход сразу: qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())

        self.show()

    # Метод центрирования окна (из библиотеки QDesktopWidget)
    def center(self):
        qr = self.frameGeometry() #Мы получаем прямоугольник, определяющий геометрию главного окна. Это включает в себя любые рамки окна.
        cp = QDesktopWidget().availableGeometry().center() #Мы получаем разрешение экрана нашего монитора. И с этим разрешением, мы получаем центральную точку.
        qr.moveCenter(cp) #Наш прямоугольник уже имеет ширину и высоту. Теперь мы установили центр прямоугольника в центре экрана. Размер прямоугольника не изменяется.
        self.move(qr.topLeft()) #Мы двигаем верхний левый угол окна приложения в верхний левый угол прямоугольника qr, таким образом, центрируя окно на нашем экране.

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 


#Создаются объекты application и Example. Запускается основной цикл.
if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Windows') # Пока не понятно, на что влияет (Доступные стили зависят от вашей платформы, но обычно они включают в себя «Fusion», «Windows», «WindowsVista» (только для Windows) и «Macintosh» (только для Mac).)
    ex = Example()
    sys.exit(app.exec_())