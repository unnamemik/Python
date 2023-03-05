def complex_calc(operands):
    operand1, sign, operand2 = operands
    operand1 = complex(operand1)
    operand2 = complex(operand2)
    if sign == '*':
        return operand1 * operand2
    if sign == '/':
        return operand1 / operand2
    if sign == '+':
        return operand1 + operand2
    if sign == '-':
        return operand1 - operand2