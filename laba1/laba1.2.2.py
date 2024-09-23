a = input('a=')
b = input('b=')

while True:
    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        a = b + a
        b = a - b
        a = a - b
        break
    else:
        print('mistake')
        a = input('a=')
        b = input('b=')

print('a=', a, 'b=', b)
