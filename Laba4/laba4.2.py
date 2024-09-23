def n_el(first_el, count, diff):
    return first_el + diff * (count - 1)

first_el = input('Введите первый элемент:')
while True:
    if first_el.isdigit():
        first_el = int(first_el)
        break
    else:
        print('mistake')
        first_el = input('Введите первый элемент:')

count = input('Введите количество элементов:')
while True:
    if count.isdigit() and int(count) > 0:
        count = int(count)
        break
    else:
        print('mistake')
        count = input('Введите количество элементов:')

diff = input('Введите разность прогрессии:')
while True:
    if diff.isdigit():
        diff = int(diff)
        break
    else:
        print('mistake')
        diff = input('Введите разность прогрессии:')

print(diff, '-й элемент арифметической прогрессии равен: ', n_el(first_el, count, diff), sep='')