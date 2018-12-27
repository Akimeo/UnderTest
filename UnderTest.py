import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QTabWidget,
                             QPushButton, QButtonGroup, QVBoxLayout, QLineEdit,
                             QMenuBar, QMenu, QAction, QMessageBox, QTabBar)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QRect
from main_menu import Ui_MainWindow
from tab_design import Ui_Form
from radio_form import Ui_Form as RF
from check_box_form import Ui_Form as CHBF
from make_test import Ui_MainWindow as MT
from PyQt5.QtWidgets import QFileDialog as QFD
from win32n64r import crypt


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

class MakeTest(QMainWindow, MT):
    def __init__(self):
        super().__init__()
        # self.resize(850, 550)
        self.setupUi(self)
        self.main()

    def main(self):
        try:
            self.info = [{}]
            self.data = [{}]
            self.tab_bar = QTabBar()
            self.tab.setTabBar(self.tab_bar)

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
            self.info[0]['ans_lines'][0].radioButton.setChecked(True)
        
            self.info[0]['var_btn'].clicked.connect(lambda: self.add_line(self.tab.currentIndex()))
            self.tab.currentChanged.connect(self.new_tab)

        except Exception as e:
            print('main', e)

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
            #Добавыление вкладки в таблицу
            self.tab.insertTab(self.i, tp, str(self.i + 1))
            #Добавление первой строки ответа
            self.add_line(self.i)

            self.info[self.i]['ans_lines'][0].radioButton.setChecked(True)
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
            # Представление типа как числа
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


                if self.info[pn]['ans_type'] == 0:
                    self.info[pn]['ans_group'].addButton(self.info[pn]['ans_lines'][-1].radioButton)

                    if len(self.info[pn]['ans_lines']) == 1:
                        self.info[0]['ans_lines'][0].radioButton.setChecked(True)

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

            if self.info[pn]['ans_type'] == 0:
                for n in self.info[pn]['ans_group'].buttons()[:-1]:
                    if n.isChecked():
                        return None
                self.info[pn]['ans_lines'][0].radioButton.setChecked(True)

        except Exception as e:
            print('del_line', e)

    def run(self):
        QMessageBox.information(self, "Стройка кода", "К сожалению, эта функция ещё не добавлена")

    def open(self):
        # Открытие файла
        fileName = QFD.getOpenFileName(self, "Открыть файл", "", 'Files (*.*)')[0]
        if fileName:
            self.fileName = fileName
            self.act_save.setEnabled(True)

    def save(self):
        self.file = open(self.fileName, 'w+', encoding = 'UTF-16')
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
            self.file.write(crypt(str(self.data).replace('\'', '"')))
            self.file.close()

        except Exception as e:
            print('save', e)

    def saveAs(self):
        fileName = QFD.getSaveFileName(self, "Сохранить файл", "", 'UnderTest files (*.UT)')[0]
        if fileName:
            self.fileName = fileName
            spl = fileName.split('.')
            if spl[-1] != 'UT':
                self.fileName = '.'.join(spl[:-1]) + '.UT'
            self.act_save.setEnabled(True)
            self.save()

    def close_tab(self):
        pn = self.tab.currentIndex()
        self.tab.removeTab(pn)
        self.info.pop(pn)
        for i in range(self.i):
            self.tab_bar.setTabText(i, str(i + 1))
        self.i -= 1
        self.tab.setCurrentIndex(pn-1 if pn > 0 else 0)


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


app = QApplication(sys.argv)
under_test = UnderTest()
under_test.show()
sys.exit(app.exec_())
