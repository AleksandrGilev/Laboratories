a = input('a=')
while True:
    if a.isdigit() and int(a) > 0:
        a = int(a)
        break
    else:
        print('mistake')
        a = input('a=')

b = input('b=')
while True:
    if b.isdigit() and int(b) > 0:
        b = int(b)
        break
    else:
        print('mistake')
        b = input('b=')

c = input('c=')
while True:
    if c.isdigit() and int(c) > 0:
        c = int(c)
        break
    else:
        print('mistake')
        c = input('c=')

if a + b > c and a + c > b and b + c > a:
    if (a ** 2 + b ** 2) ** 0.5 == c or (a ** 2 + c ** 2) ** 0.5 == b or (b ** 2 + c ** 2) ** 0.5 == a:
        print('прямоугольный')
    elif (a ** 2 + b ** 2) < c ** 2 or (a ** 2 + c ** 2) < b ** 2 or (b ** 2 + c ** 2) < a ** 2:
        print('тупоугольный')
    else:
        print('остроугольный')
else:
    print('impossible')
