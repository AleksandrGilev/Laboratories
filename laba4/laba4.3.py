while 1:
    try:
        dec_ch = int(input('Введите десятичное число:'))
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break


print(dec_ch, 'в двоичной системе счисления равно', bin(dec_ch)[2:])