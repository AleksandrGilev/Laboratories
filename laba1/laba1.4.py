x = input('x=')
while True:
    if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
        x = int(x)
        break
    else:
        print('mistake')
        x = input('x=')

y = input('y=')
while True:
    if y.isdigit() or (y[0] == '-' and y[1:].isdigit()):
        y = int(y)
        break
    else:
        print('mistake')
        y = input('y=')

z = input('z=')
while True:
    if z.isdigit() or (z[0] == '-' and z[1:].isdigit()):
        z = int()
        break
    else:
        print('mistake')
        z = input('z=')

xy = (x ** 2 + y ** 2) ** 0.5
xyz = (xy ** 2 + z ** 2) ** 0.5

print('Длина', xyz)
