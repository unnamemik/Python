from datetime import datetime


def write_log(res):
    if 'sqrt' in res:
        res = res.replace('sqrt', '√')
    with open('../calc_log.log', 'a') as calc_log:
        curr_time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        calc_log.write(f'{curr_time}:   {res}\n')


def read_log():
    with open('../calc_log.log', 'r') as calc_log:
        line_out = ''
        for line in calc_log:
            line_out += line + '\n'
        print(line_out)
        return line_out
