def find_nod(first_number, second_number):
    if first_number > second_number:
        small = second_number
    else:
        small = first_number
    for i in range(1, small + 1):
        if first_number % i == 0 and second_number % i == 0:
            n_o_d = i
    return n_o_d


try:
    first_number = int(input('Введите первое число:'))
except ValueError:
    print('Неправильно введено первое число')
    exit()

try:
    second_number = int(input('Введите второе число:'))
except ValueError:
    print('Неправильно введено второе число')
    exit()

print('НОД для чисел', first_number, 'и', second_number, 'равен', find_nod(first_number, second_number))
