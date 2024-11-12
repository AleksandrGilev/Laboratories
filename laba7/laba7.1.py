while 1:
    try:
        vector_1 = list(map(float, input("Введите элементы первого вектора через пробел: ").split()))
    except ValueError:
        print("Ошибка в вводе")
        continue
    else:
        break

while 1:
    try:
        vector_2 = list(map(float, input("Введите элементы второго вектора через пробел: ").split()))
    except ValueError:
        print("Ошибка в вводе")
        continue
    else:
        break

if len(vector_1) != len(vector_2):
    print("Вектора должны быть одинаковой размерности")
else:
    sk_pr = 0
    for i in range(len(vector_1)):
        sk_pr += vector_1[i] * vector_2[i]

    print(sk_pr)