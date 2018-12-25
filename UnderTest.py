import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTabWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from main_menu import Ui_MainWindow
from tab_design import Ui_Form


class UnderTest(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.setIcon(QIcon("show_test_icon.png"))
        self.pushButton.setIconSize(QSize(150,150))
        self.pushButton_2.setIcon(QIcon("make_test_icon.png"))
        self.pushButton_2.setIconSize(QSize(150,150))
        self.pushButton_2.clicked.connect(self.make_test)

    def make_test(self):
        under_test.close()
        self.new_test = MakeTest()
        self.new_test.show()

class MakeTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tab = QTabWidget(self)
        self.setCentralWidget(self.tab)
        self.tab.addTab(Tab(), 'Вопрос 1')
        self.new_tab_btn = QPushButton('Новый вопрос', self)
        self.new_tab_btn.clicked.connect(self.new_tab)
        self.tab.addTab(self.new_tab_btn, '...')
        self.i = 1

    def new_tab(self):
        self.tab.insertTab(self.i, Tab(), str(self.i + 1))
        self.i += 1

class Tab(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    

app = QApplication(sys.argv)
under_test = UnderTest()
under_test.show()
sys.exit(app.exec_())
