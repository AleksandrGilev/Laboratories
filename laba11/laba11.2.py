def filter_sentences(input_file, output_file, min_word_count):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Разбиваем текст на предложения
    import re
    sentences = re.split(r'(?<=[.!?]) +', text)

    # Фильтруем предложения по количеству слов
    filtered_sentences = [sentence for sentence in sentences if len(sentence.split()) > min_word_count]

    # Записываем отфильтрованные предложения в новый файл
    with open(output_file, 'w', encoding='utf-8') as file:
        for sentence in filtered_sentences:
            file.write(sentence + '\n')


while True:
    try:
        n = int(input("Введите количество слов в предложении: "))
    except ValueError:
        print("Введите корректное число.")
        continue
    if n < 0:
        print("Введите положительное число.")
        continue
    break

try:
    filter_sentences('input_2.txt', 'output_2.txt', n)
except FileNotFoundError:
    print('Ошибка наличия файла!')
    exit()
