def dec_to_bin(dec_ch):
    if dec_ch == 0:
        return 0
    else:
        return dec_to_bin(dec_ch // 2) * 10 + dec_ch % 2

while 1:
    try:
        dec_ch = int(input('Введите десятичное число:'))
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break

print(f'{dec_ch} в двоичной системе счисления равно {dec_to_bin(dec_ch)}')
