from math import sqrt


def percent_calc(ops_str):
    operand1, operand2 = ops_str.split('%')
    percent = float(operand1) * 100 / float(operand2)
    return round(percent, 2)


def sqrt_calc(ops_str):
    operand = float(ops_str[1:])
    sq_routine = sqrt(operand)
    return round(sq_routine, 2)