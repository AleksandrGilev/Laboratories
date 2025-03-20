with open('input.txt', 'r', encoding='utf-8') as file:
    lines = []
    for line in file.readlines():
        lines.append(line.strip())

print(lines)


def count_a(string):
    return string.lower().count('а')


sorted_lines = sorted(lines, key=count_a, reverse=True)

for line in sorted_lines:
    print(line)
