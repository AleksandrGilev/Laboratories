participants = {
    'Иванов': 20,
    'Сидоров': 68,
    'Петров': 26,
    'Смирнов': 68,
}

while True:
    print("\nТекущий словарь:")
    for key, value in participants.items():
        print(f"{key}: {value}")

    key = input("\nВведите новый ключ (или 'выход' для завершения): ")

    if key.lower() == 'выход':
        break

    if key in participants:
        print("Такой ключ уже существует!")
        continue
    while 1:
        try:
            value = int(input("Введите значение: "))
        except ValueError:
            print("Введено неверное значение")
        else:
            break
    participants[key] = value
    print("Данные успешно добавлены!")

average_score = sum(participants.values()) / len(participants)

min_score = min(participants.values())
max_score = max(participants.values())

print(f"\nСредний балл: {average_score:.2f}")

print("Участники с баллом выше среднего:")
for name, score in participants.items():
    if score > average_score:
        print(f"{name}: {score}")

print("\nУчастники с минимальным баллом:")
for name, score in participants.items():
    if score == min_score:
        print(f"{name}: {score}")

print("\nУчастники с максимальным баллом:")
for name, score in participants.items():
    if score == max_score:
        print(f"{name}: {score}")