N = input('Введите первое число:')
M = input('Введите второе число:')

while True:
    if N.isdigit() and M.isdigit():
        N = int(N)
        M = int(M)
        if len(str(abs(N))) > len(str(abs(M))):
            print('Больше цифр в первом числе')
        elif len(str(abs(N))) < len(str(abs(M))):
            print('Больше цифр в первом числе')
        else:
            print('Количество цифр равны')
        break
    else:
        print('mistake')
        N = input('Введите первое число:')
        M = input('Введите второе число:')
