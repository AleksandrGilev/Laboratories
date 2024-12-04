line_1 = input("Введите первую строку: ")
line_2 = input("Введите вторую строку: ")

set_line_1 = set(line_1)
set_line_2 = set(line_2)

only_1 = set_line_1 - set_line_2
    
if not only_1:
    print("Таких символов нет")
else:
    print(f"Уникальные символы {list(only_1)}")

