import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QTabWidget,
                             QPushButton, QButtonGroup, QVBoxLayout, QLineEdit,
                             QMenuBar, QMenu, QAction, QMessageBox, QLabel,
                             QHBoxLayout, QRadioButton, QCheckBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QRect
from main_menu import Ui_MainWindow
from tab_design import Ui_Form
from radio_form import Ui_Form as RF
from check_box_form import Ui_Form as CHBF
from make_test import Ui_MainWindow as MT
from show_test import Ui_Form as QP
from PyQt5.QtWidgets import QFileDialog as QFD
from json import loads
from win32n64r import crypt


class UnderTest(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.setIcon(QIcon("show_test_icon.png"))
        self.pushButton.setIconSize(QSize(150,150))
        self.pushButton.clicked.connect(self.show_test)
        self.pushButton_2.setIcon(QIcon("make_test_icon.png"))
        self.pushButton_2.setIconSize(QSize(150,150))
        self.pushButton_2.clicked.connect(self.make_test)

    def show_test(self):
        under_test.close()
        self.test = ShowTest()
        self.test.show()

    def make_test(self):
        under_test.close()
        self.new_test = MakeTest()
        self.new_test.show()

class MakeTest(QMainWindow, MT):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        try:
            self.info = [{}]
            self.data = [{}]

            self.i = 0

            self.act_open.triggered.connect(self.open)
            self.act_run.triggered.connect(self.run)
            self.act_save.triggered.connect(self.save)
            self.act_saveAs.triggered.connect(self.saveAs)
            self.act_close.triggered.connect(self.close)

            self.act_add_question.triggered.connect(lambda: self.new_tab(menuCall=True))
            self.act_del_question.triggered.connect(self.close_tab)
            self.act_add_ans.triggered.connect(lambda: self.add_line(self.tab.currentIndex()))
            
            tp = self.info[0]['page'] = TabPage()
            self.info[0]['var_btn'] = tp.add_var
            self.info[0]['vbox'] = tp.verticalLayout_2
            self.info[0]['ans_lines'] = []
            self.info[0]['del_btns'] = []
            self.info[0]['ans_type'] = 0
            self.info[0]['ans_group'] = QButtonGroup()
            self.info[0]['RBG'] = tp.RBG
            self.info[0]['RBG'].buttonClicked.connect(self.ans_type)
            self.info[0]['page'].setStyleSheet('tab: black;')
            self.tab.addTab(tp, '1')
            self.add_line(0)
            self.tab.addTab(QWidget(), '+')
        
            self.info[0]['var_btn'].clicked.connect(lambda: self.add_line(self.tab.currentIndex()))
            self.tab.currentChanged.connect(self.new_tab)

        except Exception as e:
            print('initUI', e)

    def test(self, pn):
        # Для тестов
        print(pn)

    def new_tab(self, smth=False, menuCall = False):
        try:
            if self.tab.currentIndex() == self.i + 1 or menuCall:
                pass
            else:
                return None
            self.i += 1

            self.info.append({})
            self.data.append({})
            # Вкладка таблицы
            tp = self.info[self.i]['page'] = TabPage()
            # Кнопка "Добавить вариант" (ответа)
            self.info[self.i]['var_btn'] = tp.add_var
            # Layout с вариантами ответов
            self.info[self.i]['vbox'] = tp.verticalLayout_2
            # Список вариантов ответов 
            self.info[self.i]['ans_lines'] = []
            # Список кнопок, удаляющих варианты ответов
            self.info[self.i]['del_btns'] = []
            # Выбранный тип ответов
            self.info[self.i]['ans_type'] = 0
            # Группа радио-кнопок для вариантов ответов
            self.info[self.i]['ans_group'] = QButtonGroup()
            # Группа радио-кнопок для выбора типа ответов
            self.info[self.i]['RBG'] = tp.RBG
            self.info[self.i]['RBG'].buttonClicked.connect(self.ans_type)
            self.tab.insertTab(self.i, tp, str(self.i + 1))
            self.add_line(self.i)
            
            self.info[self.i]['var_btn'].clicked.connect(lambda: self.add_line(self.tab.currentIndex()))
            
            self.tab.setCurrentIndex(self.i)
        except Exception as e:
            print('new_tab', e)

    def ans_type(self, btn):
        # Смена типа ответов
        try:
            pn = self.tab.currentIndex()
            for i in reversed(range(self.info[pn]['vbox'].count())):
                self.info[pn]['vbox'].itemAt(i).widget().deleteLater()
            self.info[pn]['ans_lines'] = []
            self.info[pn]['del_btns'] = []
            self.info[pn]['ans_group'] = QButtonGroup()
            if btn.text() == 'Один правильный вариант':
                self.info[pn]['ans_type'] = 0
            elif btn.text() == 'Несколько правильных вариантов':
                self.info[pn]['ans_type'] = 1
            else:
                self.info[pn]['ans_type'] = 2
            self.info[pn]['var_btn'].show()
            self.add_line(pn)
            
        except Exception as e:
            print('ans_type', e)

    def add_line(self, pn):
        # Добавление вариата ответа
        try:
            if self.info[pn]['ans_type'] == 0:
                self.info[self.i]['var_btn'].show()
                linetype, lt = RadioForm(), True
            elif self.info[pn]['ans_type'] == 1:
                self.info[self.i]['var_btn'].show()
                linetype, lt =  CheckBoxForm(), True
            else:
                self.info[self.i]['var_btn'].hide()
                linetype, lt =  QLineEdit(), False

            if len(self.info[pn]['ans_lines']) == 10:
                return None
            elif len(self.info[pn]['ans_lines']) == 1 and not lt:
                return None

            self.info[pn]['ans_lines'].append(linetype)
            self.info[pn]['vbox'].addWidget(self.info[pn]['ans_lines'][-1])

            if lt:
                self.info[pn]['del_btns'].append(self.info[pn]['ans_lines'][-1].delete_btn)
                self.info[pn]['del_btns'][-1].clicked.connect(lambda: self.del_line(pn, len(self.info[pn]['del_btns']) - 1))

                if len(self.info[pn]['del_btns']) == 10:
                    self.info[pn]['var_btn'].hide()
                elif len(self.info[pn]['del_btns']) != 1:
                    self.info[pn]['del_btns'][0].setEnabled(True)
                else:
                    self.info[pn]['del_btns'][0].setEnabled(False)
                if type(self.info[pn]['ans_lines'][0]) == type(RadioForm()):
                    self.info[pn]['ans_group'].addButton(self.info[pn]['ans_lines'][-1].radioButton)
            else:
                self.info[pn]['ans_lines'][0].setPlaceholderText('Введите правильный ответ...')
        except Exception as e:
            print('add_line', e)

    def del_line(self, pn, ln):
        # Удаление варианта ответа
        try:
            self.info[pn]['vbox'].removeWidget(self.info[pn]['ans_lines'][ln])
            self.info[pn]['ans_lines'][ln].deleteLater()
            self.info[pn]['ans_lines'].pop(ln)
            self.info[pn]['del_btns'].pop(ln)
            if len(self.info[pn]['ans_lines']) == 9:
                self.info[pn]['var_btn'].show()
            elif len(self.info[pn]['ans_lines']) == 1:
                self.info[pn]['del_btns'][0].setEnabled(False)
        except Exception as e:
            print('del_line', e)

    def run(self):
        QMessageBox.information(self, "Стройка кода", "К сожалению, эта функция ещё не добавлена")

    def open(self):
        # Открытие файла
        fileName = QFD.getOpenFileName(self, "Открыть файл", "", 'Files (*.*)')[0]
        if fileName:
            self.fileName =fileName
            '''
            self.fn = fileName
            self.opd = open(fileName, 'r+')
            self.text = self.opd.read()
            self.NotePlace.setPlainText(self.text)
            self.fileSave.setEnabled(True)
            self.opd.close()
            self.setWindowTitle(self.fn.split('/')[-1] + self.wt)
            self.tch = False'''

    def save(self):
        try:
            for pn in range(len(self.info)):
                self.data[pn]['question'] = self.info[pn]['page'].plainTextEdit.toPlainText()
                self.data[pn]['type'] = self.info[pn]['ans_type']
                if self.data[pn]['type'] == 0:
                    btns = self.info[pn]['ans_group'].buttons()
                    self.data[pn]['vars'] = []
                    for j in range(len(btns)):
                        self.data[pn]['vars'].append(self.info[pn]['ans_lines'][j].ans.text())
                        if btns[j].isChecked():
                            self.data[pn]['rightAnswers'] = j
                elif self.data[pn]['type'] == 1:
                    self.data[pn]['vars'] = []
                    self.data[pn]['rightAnswers'] = []
                    for j in range(len(self.info[pn]['ans_lines'])):
                        self.data[pn]['vars'].append(self.info[pn]['ans_lines'][j].ans.text())
                        if self.info[pn]['ans_lines'][j].checkBox.isChecked():
                            self.data[pn]['rightAnswers'].append(j)
                else:
                    self.data[pn]['vars'] = ['']
                    self.data[pn]['rightAnswers'] = self.info[pn]['ans_lines'][0].text()
            print(self.data)
        except Exception as e:
            print('save', e)

    def saveAs(self):
        # Сохранение файла с указанием названия
        fileName = QFD.getSaveFileName(self, "Сохранить файл", "", 'Files (*.*)')[0]
        if fileName:
            self.fileName = fileName
            '''
            if "." not in fileName:
                fileName += ".txt"
            self.fn = fileName
            self.opd = open(fileName, 'w+')
            self.text = self.NotePlace.toPlainText()
            self.opd.write(self.text)
            self.opd.close()
            self.setWindowTitle(self.fn.split('/')[-1] + self.wt)
            self.tch = False
            '''

    def close_tab(self):
        QMessageBox.information(self, "Стройка кода", "К сожалению, эта функция ещё не добавлена")
        


class TabPage(QWidget, Ui_Form):
    # Вкладка таблицы
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class RadioForm(QWidget, RF):
    # Ответ с радио-кнопкой
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class CheckBoxForm(QWidget, CHBF):
    # Ответ с чекбоксом
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class QuestPage(QWidget, QP):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class ShowTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        try:
            self.info = []
            self.data = loads(crypt(open('test.UT', encoding='UTF-16').read()))
            self.tab = QTabWidget()
            self.setCentralWidget(self.tab)
            self.set_tab()

            self.end_btn = QPushButton('Завершить работу', self)
            self.end_btn.clicked.connect(self.finish_test)

            self.tab.addTab(self.end_btn, 'Завершить работу')
        except Exception as e:
            print(e)
        

    def set_tab(self):
        for i in range(len(self.data)):
            self.info.append({})
            self.info[i]['page'] = QuestPage()
            
            self.info[i]['page'].back_btn.clicked.connect(self.switch)
            self.info[i]['page'].fwd_btn.clicked.connect(self.switch)
            
            self.info[i]['page'].question.setPlainText(self.data[i]['question'])

            n = len(self.data[i]['vars'])
            if self.data[i]['type'] == 0:
                self.info[i]['btns'] = []
                for j in range(n):
                    hbox = QHBoxLayout()
                    rb = QRadioButton()
                    self.info[i]['btns'].append(rb)
                    hbox.addWidget(rb)
                    label = QLabel(self.data[i]['vars'][j])
                    hbox.addWidget(label)
                    hbox.addStretch()
                    if j == n - 1 and j % 2 == 0:
                        self.info[i]['page'].verticalLayout_1.addLayout(hbox)
                    else:
                        if j % 2 == 0:
                            self.info[i]['page'].verticalLayout_2.addLayout(hbox)
                        else:
                            self.info[i]['page'].verticalLayout_3.addLayout(hbox)
            elif self.data[i]['type'] == 1:
                self.info[i]['btns'] = []
                for j in range(n):
                    hbox = QHBoxLayout()
                    chb = QCheckBox()
                    self.info[i]['btns'].append(chb)
                    hbox.addWidget(chb)
                    label = QLabel(self.data[i]['vars'][j])
                    hbox.addWidget(label)
                    hbox.addStretch()
                    if j == n - 1 and j % 2 == 0:
                        self.info[i]['page'].verticalLayout_1.addLayout(hbox)
                    else:
                        if j % 2 == 0:
                            self.info[i]['page'].verticalLayout_2.addLayout(hbox)
                        else:
                            self.info[i]['page'].verticalLayout_3.addLayout(hbox)
            else:
                self.info[i]['page'].verticalLayout_1.addWidget(QLineEdit())
                
            self.tab.addTab(self.info[i]['page'], str(i + 1))

    def switch(self):
        if self.sender().text() == 'Назад':
            self.tab.setCurrentIndex(self.tab.currentIndex() - 1)
        else:
            self.tab.setCurrentIndex(self.tab.currentIndex() + 1)

    def finish_test(self):
        try:
            for i in range(len(self.info)):
                if self.data[i]['type'] == 0:
                    for j in self.info[i]['btns']:
                        if self.info[i]['btns'][j].isChecked:
                            if j == int(self.data[i]['rightAnswers']):
                                print('OK')
                            else:
                                print('FUCK YOU')
        except Exception as e:
            print(e)


app = QApplication(sys.argv)
under_test = UnderTest()
under_test.show()
sys.exit(app.exec_())
