def n_el(first_el, count, diff):
    if count == 1:
        return first_el
    return n_el(first_el, count - 1, diff) + diff


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
        count = int(input('Введите количество элементов:'))
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break
while 1:
    try:
        diff = int(input('Введите разность прогрессии:'))
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break

print(diff, '-й элемент арифметической прогрессии равен: ', n_el(first_el, count, diff), sep='')
