str = input('Введите строку: ')
stack = []

for i in str:
    stack.append(i)

inverted_str = ''
while stack:
    inverted_str += stack.pop()

print(f'Перевернутая строка: {inverted_str}')
