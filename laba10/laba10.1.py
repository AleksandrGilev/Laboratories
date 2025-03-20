def palidrome(text):
    chars = list(text)

    stack = []

    mid = len(chars) // 2

    for i in range(mid):
        stack.append(chars[i])

    if len(chars) % 2 == 1:
        start_index = mid + 1
    else:
        start_index = mid

    for i in range(start_index, len(chars)):
        if chars[i] != stack.pop():
            return False
    return True


text = input('Введите текст: ')
if len(text) < 3:
    print("Текст должен быть больше 3")
    exit()

if palidrome(text):
    print('Текст является палиндромом')
else:
    print('Текст не является палиндромом')
