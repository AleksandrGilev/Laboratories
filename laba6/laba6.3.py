line_1 = input("Введите первую строку: ")
line_2 = input("Введите вторую строку: ")

line_1 = line_1 + line_2[:-1]
line_2 = line_2[-1:]

print(f"Первая строка {line_1}")
print(f"Вторая строка {line_2}")