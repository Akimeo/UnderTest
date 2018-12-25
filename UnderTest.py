import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTabWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from main_menu import Ui_MainWindow
from tab_design import Ui_Form
from radio_form import Ui_Form as RF
from check_box_form import Ui_Form as CHBF


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
        try:
            self.tab = QTabWidget(self)
            self.setCentralWidget(self.tab)

            self.info = [{}]
            
            tp = self.info[0]['page'] = TabPage()
            self.info[0]['var_btn'] = tp.returnButton()
            self.info[0]['vbox'] = tp.returnVbox()
            self.info[0]['len_vbox'] = 0
            self.info[0]['ans_lines'] = []
            self.info[0]['del_btns'] = []
            self.tab.addTab(tp, '1')
        
            self.new_tab_btn = QPushButton('Новый вопрос', self)
            self.new_tab_btn.clicked.connect(self.new_tab)
            self.tab.addTab(self.new_tab_btn, '...')
        
            self.info[0]['var_btn'].clicked.connect(lambda: self.add_line(0))
            self.i = 0
        except Exception as e:
            print(e)
        # self.tab.currentChanged.connect(self.test)

    def test(self):
        print(self.i)

    def new_tab(self):
        try:
            self.i += 1

            self.info.append({})
            tp = self.info[self.i]['page'] = TabPage()
            self.info[self.i]['var_btn'] = tp.returnButton()
            self.info[self.i]['vbox'] = tp.returnVbox()
            self.info[self.i]['len_vbox'] = 0
            self.info[self.i]['ans_lines'] = []
            self.info[self.i]['del_btns'] = []
            self.tab.insertTab(self.i, tp, str(self.i + 1))

            self.info[self.i]['var_btn'].clicked.connect(lambda: self.add_line(self.i))
            
            self.tab.setCurrentIndex(self.i)
        except Exception as e:
            print('new_tab', e)

    def add_line(self, pn):
        try:
            self.info[pn]['ans_lines'].append(RadioForm())
            self.info[pn]['vbox'].addWidget(self.info[pn]['ans_lines'][-1])
            self.info[pn]['del_btns'].append(self.info[pn]['ans_lines'][-1].return_delete_btn())
            self.info[pn]['del_btns'][-1].clicked.connect(lambda: self.del_line(pn, len(self.info[pn]['del_btns']) - 1))
        except Exception as e:
            print('add_line', e)

    def del_line(self, pn, ln):
        try:
            self.info[pn]['vbox'].removeWidget(self.info[pn]['ans_lines'][ln])
            self.info[pn]['ans_lines'][ln].deleteLater()
            self.info[pn]['ans_lines'].pop(ln)
            self.info[pn]['del_btns'].pop(ln)
        except Exception as e:
            print('del_line', e)

class TabPage(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def returnButton(self):
        return self.add_var

    def returnVbox(self):
        return self.verticalLayout_2


class RadioForm(QWidget, RF):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def return_delete_btn(self):
        return self.delete_btn


class CheckBoxForm(QWidget, CHBF):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    

app = QApplication(sys.argv)
under_test = UnderTest()
under_test.show()
sys.exit(app.exec_())
