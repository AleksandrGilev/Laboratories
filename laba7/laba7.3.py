def find_mode(arr):
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    max_frequency = max(frequency.values())

    modes = [num for num, freq in frequency.items() if freq == max_frequency]

    if len(modes) > 1:
        return None

    return modes[0]


arr = list(map(int, input("Введите числа через пробел: ").split()))
result = find_mode(arr)
if result is None:
    print("Мода отсутствует")
else:
    print(f"Мода массива: {result}")
