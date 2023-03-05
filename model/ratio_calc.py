def ratio_calc(operands):
    operand1, sign, operand2 = operands
    operand1 = float(operand1)
    operand2 = float(operand2)
    if sign == '*':
        return round(operand1 * operand2, 2)
    if sign == '/':
        return round(operand1 / operand2, 2)
    if sign == '+':
        return round(operand1 + operand2, 2)
    if sign == '-':
        return round(operand1 - operand2, 2)