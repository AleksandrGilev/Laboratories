N = input('Введите первое число:')
M = input('Введите второе число:')

while True:
    if N.isdigit() or (N[0] == '-' and N[1:].isdigit()) and M.isdigit() or (M[0] == '-' and y[1:].isdigit()):
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
