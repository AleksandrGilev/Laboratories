def n_el_g(b, q, n):
    return b * q ** n-1

def summa_n_el(b, q, n):
    if q == 1:
        return n * b
    else:
        return (b * (1 - q ** n)) / (1 - q)

b = input('Введите первый элемент:')
while True:
    if b.isdigit() and int(b) != 0:
        b = int(b)
        break
    else:
        print('mistake')
        b = input('Введите первый элемент:')

q = input('Введите знаменатель:')
while True:
    if q.isdigit() and int(q) != 0:
        q = int(q)
        break
    else:
        print('mistake')
        q = input('Введите знаменатель:')

n = input('Введите количество элементов:')
while True:
    if n.isdigit():
        n = int(n)
        break
    else:
        print('mistake')
        n = input('Введите количество элементов:')

print(n, ' элемент геометрической прогрессии равен:', n_el_g(b, q, n))
print('сумма', n, 'членов геометрической прогрессии равна:', summa_n_el(b, q, n))
