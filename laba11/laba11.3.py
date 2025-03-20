import random


def read_phrases(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    phrases = []
    for line in lines:
        stripped_line = line.strip()
        split_line = stripped_line.split('; ')
        phrases.append(split_line)
    return phrases


def generate_sentences(phrases, num_sentences):
    sentences = []
    for _ in range(num_sentences):
        selected_phrases = []
        for i in range(4):
            random_phrase = random.choice(phrases[i])
            selected_phrases.append(random_phrase)
        sentence = ' '.join(selected_phrases)
        sentences.append(sentence)
    return sentences


def write_sentences(file_path, sentences):
    with open(file_path, 'a', encoding='utf-8') as file:
        for i in sentences:
            file.write(i + '\n')
        file.write('\n')


phrases = read_phrases('Phrases.txt')

while True:
    try:
        count_sentences = int(input('Сколько предложений сгенерировать? '))
        sentences = generate_sentences(phrases, count_sentences)

        continue_generation = input('Продолжить генерацию текста? (Да/Нет) ').strip().lower()
        if continue_generation == 'нет':
            break
    except ValueError:
        print('Некорректный ввод!')
    except FileNotFoundError:
        print('Ошибка наличия файла!')

write_sentences('Result.txt', sentences)
