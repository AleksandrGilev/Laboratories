import re

line = input("Введите имя файла: ")

if re.fullmatch(r"[^\|/*?<>]+([txt]|[doc]|[docx]|[odt]|[rtf])", line):
    print(line, 'может быть именем файла')
else:
    print(line, 'не может быть именем файла')
