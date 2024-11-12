N = input('Введите меньший номер билета:')
M = input('Введите больший номер билета:')
cnt = 0

while True:
    if len(N) == 6 and len(M) == 6:
        for i in range(int(N), int(M) + 1):
            if (i // 10 ** 5 + i % 10 * 5 // 10 * 4 + i % 10 ** 5 % 10 ** 4 // 10 ** 3) == (
                    i % 10 + i % 100 // 10 + i % 10 ** 3 // 100):
                cnt += 1
        break
    else:
        print('mistake')
        N = input('Введите меньший номер билета:')
        M = input('Введите больший номер билета:')

print('Количество билетов:', cnt)
    