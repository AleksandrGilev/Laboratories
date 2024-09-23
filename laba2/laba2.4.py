num = input('Введите число:')

while True:
    if num.isdigit():
        num = int(num)
        break
    else:
        print('mistake')
        num = input('Введите число:')

if num == 0:
    print('Факториал равен', 1)
else:
    for i in range(1, num):
        num *= i
    print('Факториал равен', num)
