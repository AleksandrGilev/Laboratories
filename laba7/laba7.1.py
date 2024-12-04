def check(vector):
    try:
        vector = list(map(float, vector))
    except ValueError:
        return False
    return True


vector_1 = list(map(float, input("Введите элементы первого вектора через пробел: ").split()))
vector_2 = list(map(float, input("Введите элементы второго вектора через пробел: ").split()))

while not check(vector_1) and not check(vector_2):
    check(vector_1)
    check(vector_2)

if len(vector_1) != len(vector_2):
    print("Вектора должны быть одинаковой размерности")
else:
    sk_pr = 0
    for i in range(len(vector_1)):
        sk_pr += vector_1[i] * vector_2[i]

    print(sk_pr)
