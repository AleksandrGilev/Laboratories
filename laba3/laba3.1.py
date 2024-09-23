from math import *

grade = input('grade=')

while True:
    if grade.isdigit():
        grade = float(grade)
        print('sin =', sin(grade), 'rad')
        print('cos =', cos(grade), 'rad')
        print('tan =', tan(grade), 'rad')
        break
    else:
        print('mistake')
        grade = input('grade=')
