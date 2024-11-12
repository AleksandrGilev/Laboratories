while 1:
    try:
        first_num = int(input("Введите первое число: "))
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break

while 1:
    try:
        second_num = int(input("Введите второе число: "))
    except ValueError:
        print("Введено неверное значение")
        continue
    else:
        break

set_first_num = set(str(first_num))
set_second_num = set(str(second_num))

print(f"Числа, которые встречаются в обоих наборах: {set_first_num.intersection(set_second_num)}")