# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon #для иконки окошка
from PyQt5.QtCore import QCoreApplication #для кнопки выхода


class LLWin(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI() 
            
    def initUI(self):
        self.resize(500, 350)
        self.center() #Устанавливает положение окна по центру с помощью метода, описанного ниже

        self.setWindowTitle('Длинная линия')
        self.setWindowIcon(QIcon('WindowIcon1.png'))

        Rn = QLabel('Rн = ')
        Xn = QLabel('Xн = ')
       
        RnEdit = QLineEdit()
        XnEdit = QLineEdit()

        Zn = QLabel('Zн = Rн + jXн')
        

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(Rn, 1, 0)
        grid.addWidget(RnEdit, 1, 1)

        grid.addWidget(Xn, 2, 0)
        grid.addWidget(XnEdit, 2, 1)
        
        grid.addWidget(Zn, 3, 0)

        # review = QLabel('Review')
        # reviewEdit = QTextEdit()
        # grid.addWidget(review, 3, 0)
        # grid.addWidget(reviewEdit, 3, 1, 5, 1)

        qbtn = QPushButton('Выход', self)
        qbtn.clicked.connect(self.closeEvent)
        qbtn.resize(qbtn.sizeHint())

        grid.addWidget(qbtn, 5, 3)

        self.setLayout(grid)

        self.show()

    # Метод центрирования окна (из библиотеки QDesktopWidget)
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

#Создаются объекты application и LLWindow. Запускается основной цикл.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows') # Пока не понятно, на что влияет (Доступные стили зависят от вашей платформы, но обычно они включают в себя «Fusion», «Windows», «WindowsVista» (только для Windows) и «Macintosh» (только для Mac).)
    ex = LLWin()
    sys.exit(app.exec_())