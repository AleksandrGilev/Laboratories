sum_num = input('Введите сумму чисел:')

while True:
    if sum_num.isdigit():
        sum_num = int(sum_num)
        break
    else:
        print('mistake')
        sum_num = input('Введите сумму чисел:')

if sum_num > 0 and sum_num < 28:
    for i in range(100, 1000):
        if sum_num == (i % 10 + i % 100 // 10 + i % 10 ** 3 // 100):
            print(i)
else:
    print('Нет чисел')