def remove_elements_from_end(vector, count):
    # Проверка корректности входных данных
    if not isinstance(vector, list) or not all(isinstance(x, (int, float)) for x in vector):
        raise ValueError("Вектор должен быть списком чисел.")
    if not isinstance(count, int) or count < 0:
        raise ValueError("Количество должно быть неотрицательным целым числом.")

    # Удаление элементов
    new_vector = vector[:-count] if count <= len(vector) else []

    return new_vector


def read_vector_from_file(file_path):
    with open(file_path, 'r') as file:
        vector = [float(num) for num in file.read().split()]
    return vector


def write_vector_to_file(vector, file_path):
    with open(file_path, 'w') as file:
        file.write(' '.join(map(str, vector)))


# Пример использования
input_file = 'input_1.txt'
output_file = 'output_1.txt'
while True:
    try:
        n = int(input("Введите количество элементов для удаления: "))
    except ValueError:
        print("Введите корректное число.")
        continue
    if n < 0:
        print("Введите положительное число.")
        continue
    break
try:
    vector = read_vector_from_file(input_file)
except FileNotFoundError:
    print('Ошибка наличия файла!')
    exit()
new_vector = remove_elements_from_end(vector, n)

print("Новый вектор: ", new_vector)
write_vector_to_file(new_vector, output_file)
