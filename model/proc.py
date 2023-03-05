# 4*(5+1)-(9+2/4)+2*(40-5+6-7)
# (20+3j)+(5+4j)

import re

from complex_calc import complex_calc
from log_rw import write_log, read_log
from percent_sqrt_calc import percent_calc, sqrt_calc
from ratio_calc import ratio_calc

line_str = ''
log_str = ''
line_lst = []
sign_lst = []
SIGN_TYPE = ['*', '/', '+', '-']
switch_counter = 0


def line_input():
    global line_str, log_str
    # check = True
    # while check:
    #     try:
    #         line_str = (input('Для выхода введите Q. Введите выражение: '))
    #         check = False
    #     except ValueError:
    #         print('\033[31mНеверный ввод!\033[0m')
    log_str = line_str + ' = '
    sign_input()


def sign_input():
    global sign_lst, line_lst, SIGN_TYPE
    sign_lst = list(filter(lambda x: x in SIGN_TYPE, line_str))
    operands_lst = list(re.split('[-+*/]', line_str))
    line_lst = [x for y in zip(operands_lst, sign_lst) for x in y]
    line_lst.append(operands_lst[-1])
    print(f'\033[032mLine input: {line_lst}\033[0m')
    switch()
    return line_str


def switch():
    global switch_counter, line_lst, line_str
    if 'Q' in ''.join(line_str):
        exit()
    elif ')' in line_str and 'j' not in line_str:
        print('\033[31mНеверный ввод!\033[0m')
        line_input()
    elif 'j' in line_str:
        switch_counter = 1
        send_operands(line_str)
    elif '%' in ''.join(line_str):
        switch_counter = 2
        send_operands(line_str)
    elif re.match(r'sqrt', line_str):
        switch_counter = 3
        send_operands(line_str)
    elif re.findall('[0-9.]', line_str):
        switch_counter = 4
        for i in range(len(sign_lst)):
            operations_priority()
    else:
        print('\033[31mНеверный ввод!\033[0m')
        line_input()


def send_operands(pared_operands):
    global switch_counter, line_str, log_str, log_res
    if switch_counter == 1:
        res = complex_calc(complex_ops_list_create())
        print(f'\033[033mResult: {res}\033[0m')
        write_log(log_str, res)
        read_log()
        reset_vars()
    if switch_counter == 2:
        res = (percent_calc(line_str))
        print(f'\033[033mResult: {res}\033[0m')
        write_log(log_str, res)
        read_log()
        reset_vars()
    if switch_counter == 3:
        res = sqrt_calc(line_str)
        print(f'\033[033mResult: {res}\033[0m')
        write_log(log_str, res)
        read_log()
        reset_vars()
    if switch_counter == 4:
        return ratio_calc(pared_operands)


def brake_sign_list_create():
    global sign_lst, line_str
    ds_lst = list(re.split('\(.*?\)', line_str))
    ds_str = ''.join(ds_lst)
    sign_lst = list(re.findall('[-+*/]', ds_str))


def complex_ops_list_create():
    global sign_lst, line_str
    complex_lst = []
    pattern = re.compile(r'\([-\d+*/j]+\)')
    pos = 0
    while True:
        match = pattern.search(line_str, pos)
        if not match:
            if re.search(r'\)[+*/-]\(', line_str):
                break
        s = match.start()
        e = match.end()
        complex_lst.append(line_str[s:e])
        pos = e
    brake_sign_list_create()
    complex_lst.insert(1, *sign_lst)
    return complex_lst


def replace_operands(operands):
    global line_lst, sign_lst, switch_counter
    switch_counter = 4
    operand1, sign, operand2 = operands
    line_lst.pop(line_lst.index(sign) - 1)
    line_lst.insert(line_lst.index(sign), send_operands(operands))
    line_lst.pop(line_lst.index(sign) + 1)
    line_lst.pop(line_lst.index(sign))
    sign_lst.pop(sign_lst.index(sign))
    if len(sign_lst) == 0:
        print(f'\033[033mResult: {line_lst}\033[0m')
        write_log(log_str, *line_lst)


def curr_operation(sign):
    global line_lst
    op_index = line_lst.index(sign)
    pared_operands = [line_lst[op_index - 1], line_lst[op_index], line_lst[op_index + 1]]
    replace_operands(pared_operands)
    return pared_operands


def operations_priority():
    while len(sign_lst) > 0:
        for sign in sign_lst:
            if sign == '*':
                return curr_operation(sign)
            elif sign == '/':
                return curr_operation(sign)
        for sign in sign_lst:
            if sign == '+':
                return curr_operation(sign)
            elif sign == '-':
                return curr_operation(sign)


def reset_vars():
    global line_str, line_lst, sign_lst, switch_counter

    line_str = ''
    line_lst.clear()
    sign_lst.clear()
    switch_counter = 0


def calc_start(args):
    global line_str
    line_str = args
    line_input()
