def process_stacks(queues):
    stack_list = [queue.split(', ') for queue in queues]

    exit_str = []
    while any(stack for stack in stack_list):
        for stack in stack_list:
            if stack:
                exit_str.append(stack.pop(0))

    return ', '.join(exit_str)


try:
    with open('input.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

except FileNotFoundError:
    print('Ошибка наличия файла!')
    exit()
lines = [line.strip() for line in lines]
exit = process_stacks(lines)

print(exit)  # А1, Б1, В1, А2, Б2, Б3
