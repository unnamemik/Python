import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog
from model import calc_log_mod, calc as calc, calc_about_mod, log_rw
import re
from model.complex_calc import complex_calc
from model.log_rw import write_log
from model.percent_sqrt_calc import percent_calc, sqrt_calc
from model.ratio_calc import ratio_calc


class CalcLogMod(QDialog, calc_log_mod.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.textBrowser.setText(log_rw.read_log())


class CalcAboutMod(QDialog, calc_about_mod.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, calc.Ui_MainWindow):
    line_str = ''
    log_str = ''
    res_value = ''
    line_lst = []
    sign_lst = []
    SIGN_TYPE = ['*', '/', '+', '-']
    switch_counter = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_1_clear.clicked.connect(self.clear_field_func)
        self.pushButton_13_1.clicked.connect(self.keyb_1)
        self.pushButton_14_2.clicked.connect(self.keyb_2)
        self.pushButton_15_3.clicked.connect(self.keyb_3)
        self.pushButton_9_4.clicked.connect(self.keyb_4)
        self.pushButton_10_5.clicked.connect(self.keyb_5)
        self.pushButton_11_6.clicked.connect(self.keyb_6)
        self.pushButton_5_7.clicked.connect(self.keyb_7)
        self.pushButton_6_8.clicked.connect(self.keyb_8)
        self.pushButton_7_9.clicked.connect(self.keyb_9)
        self.pushButton_18_0.clicked.connect(self.keyb_0)
        self.pushButton_20_add.clicked.connect(self.keyb_add)
        self.pushButton_16_sub.clicked.connect(self.keyb_sub)
        self.pushButton_12_mult.clicked.connect(self.keyb_mult)
        self.pushButton_8_div.clicked.connect(self.keyb_div)
        self.pushButton_19.clicked.connect(self.keyb_dot)
        self.pushButton_4_x_2.clicked.connect(self.keyb_LP)
        self.pushButton_4_x_3.clicked.connect(self.keyb_RP)
        self.pushButton_4_x_4.clicked.connect(self.keyb_j)
        self.pushButton_3_sqrt.clicked.connect(self.sqrt_retype_func)
        self.pushButton_4_x.clicked.connect(self.char_delete)
        self.pushButton_21_eq.clicked.connect(self.calc_start_func)
        self.pushButton_17_logs.clicked.connect(show_log)
        self.actionAbout_2.triggered.connect(show_about)

    def sqrt_retype_func(self):
        self.textEdit.clear()
        sqrt_sign = '√'
        self.textEdit.append(sqrt_sign)

    def keyb_1(self):
        self.textEdit.insertPlainText('1')
    def keyb_2(self):
        self.textEdit.insertPlainText('2')
    def keyb_3(self):
        self.textEdit.insertPlainText('3')
    def keyb_4(self):
        self.textEdit.insertPlainText('4')
    def keyb_5(self):
        self.textEdit.insertPlainText('5')
    def keyb_6(self):
        self.textEdit.insertPlainText('6')
    def keyb_7(self):
        self.textEdit.insertPlainText('7')
    def keyb_8(self):
        self.textEdit.insertPlainText('8')
    def keyb_9(self):
        self.textEdit.insertPlainText('9')
    def keyb_0(self):
        self.textEdit.insertPlainText('0')
    def keyb_add(self):
        self.textEdit.insertPlainText('+')
    def keyb_sub(self):
        self.textEdit.insertPlainText('-')
    def keyb_mult(self):
        self.textEdit.insertPlainText('*')
    def keyb_div(self):
        self.textEdit.insertPlainText('/')
    def keyb_dot(self):
        self.textEdit.insertPlainText('.')
    def keyb_LP(self):
        self.textEdit.insertPlainText('(')
    def keyb_RP(self):
        self.textEdit.insertPlainText(')')
    def keyb_j(self):
        self.textEdit.insertPlainText('j')


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_1:
                self.textEdit.insertPlainText('1')
        if event.key() == QtCore.Qt.Key_2:
                self.textEdit.insertPlainText('2')
        if event.key() == QtCore.Qt.Key_3:
                self.textEdit.insertPlainText('3')
        if event.key() == QtCore.Qt.Key_4:
                self.textEdit.insertPlainText('4')
        if event.key() == QtCore.Qt.Key_5:
                self.textEdit.insertPlainText('5')
        if event.key() == QtCore.Qt.Key_6:
                self.textEdit.insertPlainText('6')
        if event.key() == QtCore.Qt.Key_7:
                self.textEdit.insertPlainText('7')
        if event.key() == QtCore.Qt.Key_8:
                self.textEdit.insertPlainText('8')
        if event.key() == QtCore.Qt.Key_9:
                self.textEdit.insertPlainText('9')
        if event.key() == QtCore.Qt.Key_0:
                self.textEdit.insertPlainText('0')
        if event.key() == QtCore.Qt.Key_Period:
                self.textEdit.insertPlainText('.')
        if event.key() == QtCore.Qt.Key_Plus:
                self.textEdit.insertPlainText('+')
        if event.key() == QtCore.Qt.Key_Minus:
                self.textEdit.insertPlainText('-')
        if event.key() == QtCore.Qt.Key_Asterisk:
                self.textEdit.insertPlainText('*')
        if event.key() == QtCore.Qt.Key_Slash:
                self.textEdit.insertPlainText('/')
        if event.key() == QtCore.Qt.Key_Percent:
                self.textEdit.insertPlainText('%')
        if event.key() == QtCore.Qt.Key_S:
                self.textEdit.insertPlainText('√')
        if event.key() == QtCore.Qt.Key_ParenLeft:
                self.textEdit.insertPlainText('(')
        if event.key() == QtCore.Qt.Key_ParenRight:
                self.textEdit.insertPlainText(')')
        if event.key() == QtCore.Qt.Key_J:
                self.textEdit.insertPlainText('j')
        if event.key() == QtCore.Qt.Key_C:
                self.clear_field_func()
        if event.key() == QtCore.Qt.Key_Backspace:
                self.textEdit.insertPlainText('')
        if event.key() == QtCore.Qt.Key_Enter:
                self.calc_start_func()
        event.accept()

    def calc_start_func(self):
        self.line_str = self.textEdit.toPlainText()
        print(self.line_str)
        self.line_input()

    def char_delete(self):
        type_str = self.textEdit.toPlainText()[0:-1]
        self.textEdit.setText(type_str)

    def clear_field_func(self):
        self.textEdit.clear()
        self.reset_vars()

    def line_input(self):
        check = True
        while check:
            try:
                if re.findall(r'[\d+*/j√=()-]+', self.line_str):
                    check = False
                else:
                    break
            except ValueError:
                self.textEdit.setText('Неверный ввод!')
                self.reset_vars()
                self.textEdit.clear()
        self.log_str = self.line_str
        self.sign_input()

    def sign_input(self):
        self.sign_lst = list(filter(lambda x: x in self.SIGN_TYPE, self.line_str))
        operands_lst = list(re.split('[-+*/]', self.line_str))
        self.line_lst = [x for y in zip(operands_lst, self.sign_lst) for x in y]
        self.line_lst.append(operands_lst[-1])
        print(f'\033[032mLine input: {self.line_lst}\033[0m')
        self.switch()
        return self.line_str

    def switch(self):
        if 'Q' in ''.join(self.line_str):
            exit()
        elif ')' in self.line_str and 'j' not in self.line_str:
            self.textEdit.setText('Неверный ввод!')
            self.reset_vars()
            self.textEdit.clear()
        elif 'j' in self.line_str:
            self.switch_counter = 1
            self.send_operands(self.line_str)
        elif '%' in ''.join(self.line_str):
            self.switch_counter = 2
            self.send_operands(self.line_str)
        elif re.match(r'√', self.line_str):
            self.switch_counter = 3
            self.send_operands(self.line_str)
        elif re.findall('[0-9.]', self.line_str):
            self.switch_counter = 4
            for i in range(len(self.sign_lst)):
                self.operations_priority()
        else:
            self.textEdit.setText('Неверный ввод!')
            self.reset_vars()
            self.textEdit.clear()

    def send_operands(self, pared_operands):
        if self.switch_counter == 1:
                res = complex_calc(self.complex_ops_list_create())
                res = str(res)[1:-1]
                print(f'\033[033mResult: {res}\033[0m')
                self.res_value = self.textEdit.toPlainText() + ' = ' + res + '\n'
                self.textEdit.setText(self.res_value)
                write_log(self.res_value)
                self.reset_vars()
        if self.switch_counter == 2:
                res = percent_calc(self.line_str)
                print(f'\033[033mResult sqrt: {res}\033[0m')
                self.res_value = self.textEdit.toPlainText() + ' = ' + str(res) + '\n'
                print(self.res_value)
                self.textEdit.setText(self.res_value)
                write_log(self.res_value)
        if self.switch_counter == 3:
                res = sqrt_calc(self.line_str)
                print(f'\033[033mResult sqrt: {res}\033[0m')
                self.res_value = self.textEdit.toPlainText() + ' = ' + str(res) + '\n'
                print(self.res_value)
                self.textEdit.setText(self.res_value)
                write_log(self.res_value)
        if self.switch_counter == 4:
                return ratio_calc(pared_operands)

    def brake_sign_list_create(self):
        ds_lst = list(re.split('\(.*?\)', self.line_str))
        ds_str = ''.join(ds_lst)
        self.sign_lst = list(re.findall('[-+*/]', ds_str))

    def complex_ops_list_create(self):
        complex_lst = []
        pattern = re.compile(r'\([-\d+*/j]+\)')
        pos = 0
        while True:
            match = pattern.search(self.line_str, pos)
            if not match:
                if re.search(r'\)[+*/-]\(', self.line_str):
                    break
            s = match.start()
            e = match.end()
            complex_lst.append(self.line_str[s:e])
            pos = e
        self.brake_sign_list_create()
        complex_lst.insert(1, *self.sign_lst)
        return complex_lst

    def replace_operands(self, operands):
        self.switch_counter = 4
        operand1, sign, operand2 = operands
        self.line_lst.pop(self.line_lst.index(sign) - 1)
        self.line_lst.insert(self.line_lst.index(sign), self.send_operands(operands))
        self.line_lst.pop(self.line_lst.index(sign) + 1)
        self.line_lst.pop(self.line_lst.index(sign))
        self.sign_lst.pop(self.sign_lst.index(sign))
        if len(self.sign_lst) == 0:
            print(f'\033[033mResult: {self.line_lst}\033[0m')
            self.res_value = self.textEdit.toPlainText()
            self.res_value = (self.log_str + ' = ' + str(self.line_lst[0]) + '\n')
            self.textEdit.setText(self.res_value)
            write_log(self.res_value)
            self.line_str = ''
            self.line_lst.clear()
            self.sign_lst.clear()
            self.switch_counter = 0

    def curr_operation(self, sign):
        op_index = self.line_lst.index(sign)
        pared_operands = [self.line_lst[op_index - 1], self.line_lst[op_index], self.line_lst[op_index + 1]]
        self.replace_operands(pared_operands)
        return pared_operands

    def operations_priority(self):
        while len(self.sign_lst) > 0:
            for sign in self.sign_lst:
                if sign == '*':
                    return self.curr_operation(sign)
                elif sign == '/':
                    return self.curr_operation(sign)
            for sign in self.sign_lst:
                if sign == '+':
                    return self.curr_operation(sign)
                elif sign == '-':
                    return self.curr_operation(sign)

    def reset_vars(self):
        # self.textEdit.clear()
        self.line_str = ''
        self.line_lst.clear()
        self.sign_lst.clear()
        self.switch_counter = 0


def show_log():
    clm_ = CalcLogMod()
    clm_.exec()


def show_about():
    cam_ = CalcAboutMod()
    cam_.exec()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
