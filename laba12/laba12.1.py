import random
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def sorting_time(sort_function, arr):
    total_time = 0
    for i in range(100):
        random.shuffle(arr)
        start_time = time.time()
        sort_function(arr.copy())
        total_time += time.time() - start_time
    return total_time / 100


array_size = 100
random_array = [random.randint(0, 1000) for _ in range(array_size)]

bubble_sort_time = sorting_time(bubble_sort, random_array)
standard_sort_time = sorting_time(sorted, random_array)

print(f"Среднее время сортировки методом пузырька {bubble_sort_time:.6f} секунд")
print(f"Среднее время сортировки стандартным методом {standard_sort_time:.6f} секунд")
