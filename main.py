import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMainWindow
from PyQt6.QtCore import Qt
from PyQt6 import uic
#from PyQt6.QtGui import QGuiApplication


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui', self)
        self.pushButton.clicked.connect(self.sayHello)

    def sayHello(self):
        self.textEdit.setText('Hello Lonely Bois')


if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor
    # QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoudingPolicy)

    app = QApplication(sys.argv)
    # app.setStyleSheet('''
    #     QWidget {
    #         font-size: 30px;
    #     }
    # ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window')
