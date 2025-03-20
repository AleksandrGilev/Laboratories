def create_table_of_contents(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        lines = input_file.readlines()
        
    contents = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('Глава') or line.startswith('Chapter'):
            chapter_number = line
            if i + 1 < len(lines):
                chapter_title = lines[i + 1].strip()
                contents.append(f"{chapter_number} - {chapter_title}")
                i += 2
            else:
                i += 1
        else:
            i += 1
    
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write("Оглавление:\n")
        for entry in contents:
            output_file.write(f"{entry}\n")


try:
    create_table_of_contents('text.txt', 'chapter.txt')
except FileNotFoundError:
    print('Ошибка наличия файла!')
    exit()
