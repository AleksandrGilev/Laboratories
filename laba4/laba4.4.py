def nok(ch_f, ch_s):
    if ch_f == 0 or ch_s == 0:
        return 0
    if ch_f < ch_s:
        return nok(ch_s, ch_f)
    if ch_s == 0:
        return ch_f
    if ch_f % ch_s == 0:
        return ch_f
    return nok(ch_s, ch_f % ch_s) * ch_f // ch_s

while 1:
    try:
        ch_f = int(input('Введите первое число:'))
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break

while 1:
    try:
        ch_s = int(input('Введите второе число:'))
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break

print(f'Наименьшее общее кратное равно {nok(ch_f, ch_s)}')
