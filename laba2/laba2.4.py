import sys
from functools import lru_cache

sys.set_int_max_str_digits(1000000)
sys.setrecursionlimit(10000000)


@lru_cache(None)
def fac(num):
    result = 1
    if num == 0:
        return result
    else:
        for i in range(1, num + 1):
            result *= i
        return result


num = input('Введите число:')

while True:
    if num.isdigit():
        num = int(num)
        break
    else:
        print('mistake')
        num = input('Введите число:')

print(f"Факториал {num} равен {fac(num)}")
