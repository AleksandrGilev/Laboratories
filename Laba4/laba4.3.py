dec_ch = input('Введите десятичное число:')
while True:
    if dec_ch.isdigit():
        dec_ch = int(dec_ch)
        break
    else:
        print('mistake')
        dec_ch = input('Введите десятичное число:')

print(dec_ch, 'в двоичной системе счисления равно', bin(dec_ch)[2:])