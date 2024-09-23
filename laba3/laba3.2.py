def find_nod(first_number, second_number):
    if first_number > second_number:
        small = second_number
    else:
        small = first_number
    for i in range(1, small + 1):
        if first_number % i == 0 and second_number % i == 0:
            n_o_d = i
    return n_o_d


first_number = input('Введите первое число:')

while True:
    if first_number.isdigit():
        first_number = int(first_number)
        break
    else:
        print('Неправильно введено первое число')
        first_number = input('Введите первое число:')

second_number = input('Введите второе число:')

while True:
    if second_number.isdigit():
        second_number = int(second_number)
        break
    else:
        print('Неправильно введено второе число')
        second_number = input('Введите второе число')

print('НОД для чисел', first_number, 'и', second_number, 'равен', find_nod(first_number, second_number))
