rus_eng_dict = {
    'привет': 'hello',
    'мир': 'world',
    'компьютер': 'computer',
    'программа': 'program',
    'язык': 'language',
    'python': 'python',
    'кот': 'cat',
    'собака': 'dog',
    'дом': 'house',
    'книга': 'book'
}

text = input('Введите текст на русском языке: ').lower()

words = text.split()

translated_words = []
for word in words:
    translated_word = rus_eng_dict.get(word, word)
    translated_words.append(translated_word)

translated_text = ' '.join(translated_words)

print('Переведенный текст:', translated_text)
