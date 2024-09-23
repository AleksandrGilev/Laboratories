from math import *

def nok(ch_f, ch_s):
    return (ch_f * ch_s) // gcd(ch_f, ch_s)

ch_f = input('Введите первое число:')
while True:
    if ch_f.isdigit():
        ch_f = int(ch_f)
        break
    else:
        print('mistake')
        ch_f = input('Введите первое число:')

ch_s = input('Введите второе число:')
while True:
    if ch_s.isdigit():
        ch_s = int(ch_s)
        break
    else:
        print('mistake')
        ch_s = input('Введите второе число:')

print('Наименьшее общее кратное равно', nok(ch_f, ch_s))
