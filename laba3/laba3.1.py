from math import *

try:
    grade = int(input('grade='))
except ValueError:
    print('Введено неверное значение')
    exit()


print('sin =', sin(grade), 'rad')
print('cos =', cos(grade), 'rad')
print('tan =', tan(grade), 'rad')
