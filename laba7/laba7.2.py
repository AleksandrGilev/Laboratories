def chek(a):
    try:
        a = int(a)
    except ValueError:
        return False
    return True


K = int(input("Введите количество столбцов первой и строк второй матрицы: "))
M = int(input("Введите количество строк первой матрицы: "))
N = int(input("Введите количество столбцов второй матрицы: "))

while not chek(K) and not chek(M) and not chek(N):
    chek(K)
    chek(M)
    chek(N)

matrix_1 = []
for m in range(M):
    for k in range(K):
        new = list(map(float, input(f"Введите строку {m + 1} и столбец {k + 1} первой матрицы: ").split()))
        matrix_1.append(new)

matrix_2 = []
for k in range(K):
    for n in range(N):
        new = list(map(float, input(f"Введите строку {k + 1} и столбец {n + 1} второй матрицы: ").split()))
        matrix_2.append(new)

result = [[0 for _ in range(N)] for _ in range(M)]

for m in range(M):
    for n in range(N):
        for k in range(K):
            result[m][n] += matrix_1[m][k] * matrix_2[k][n]

for new in result:
    print(" ".join(map(str, new)))
