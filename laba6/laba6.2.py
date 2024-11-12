line = input("Введите строку: ")

line = line.strip()
line = line[0].upper() + line[1:].lower()
if line.endswith(('!','?')):
    line = line [:-1]
if line.endswith('...'):
    line = line [:-2]
if not line.endswith('.'):
    line += '.'

print(line)