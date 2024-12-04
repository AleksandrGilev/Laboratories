def n_el(b, q, n):
    if n == 1:
        return b
    return n_el(b, q, n - 1) * q


def summa_n_el(b, q, n):
    if n == 1:
        return b
    else:
        return summa_n_el(b, q, n - 1) + b * q ** (n - 1)


while 1:
    try:
        b = int(input('Введите первый элемент: '))
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break

while 1:
    try:
        q = int(input('Введите знаменатель: '))
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break

while 1:
    try:
        n = int(input('Введите количество элементов: '))
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break

print(n, 'элемент геометрической прогрессии равен: ', n_el(b, q, n))
print('сумма', n, 'членов геометрической прогрессии равна:', summa_n_el(b, q, n))
