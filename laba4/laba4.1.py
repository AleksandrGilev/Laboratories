def n_el_g(b, q, n):
    return b * q ** n-1

def summa_n_el(b, q, n):
    if q == 1:
        return n * b
    else:
        return (b * (1 - q ** n)) / (1 - q)

while 1:
    try:
        b = int(input('Введите первый элемент:'))
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break

while 1:
    try:
        q = int(input('Введите знаменатель:'))
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break

while 1:
    try:
        n = int(input('Введите количество элементов:'))
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break

print(n, ' элемент геометрической прогрессии равен:', n_el_g(b, q, n))
print('сумма', n, 'членов геометрической прогрессии равна:', summa_n_el(b, q, n))
