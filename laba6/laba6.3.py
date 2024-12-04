line_1 = input("Введите первую строку: ")
line_2 = input("Введите вторую строку: ")

last_el = line_1.rfind(line_2)

if last_el != -1:
    line_1 = line_1[:last_el].replace(line_2, "") + line_1[last_el:]

print(f"первая строка {line_1}")

# abcabcabc
# ab
# ccabc
