def n_el(first_el, count, diff):
    return first_el + diff * (count - 1)

while 1:
    try:
        first_el = int(input('Введите первый элемент:'))
    except  ValueError:
        print("Введено неверное значение")
        continue
    else:
        break
while 1:
    try:
        count = input('Введите количество элементов:')
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break
while 1:
    try:
        diff = input('Введите разность прогрессии:')
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break


print(diff, '-й элемент арифметической прогрессии равен: ', n_el(first_el, count, diff), sep='')