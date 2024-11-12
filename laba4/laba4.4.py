from math import *


def nok(ch_f, ch_s):
    return (ch_f * ch_s) // gcd(ch_f, ch_s)


while 1:
    try:
        ch_f = int(input('Введите первое число:'))
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break

while 1:
    try:
        ch_s = input('Введите второе число:')
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break

print('Наименьшее общее кратное равно', nok(ch_f, ch_s))
