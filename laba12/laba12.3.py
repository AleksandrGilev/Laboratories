with open('data.txt', 'r', encoding='utf-8') as file:
    people = []
    for line in file:
        surname, birth_year = line.strip().split()
        people.append((surname, int(birth_year)))


def sort_key(person):
    return person[0], person[1]


sorted_people = sorted(people, key=sort_key)

for person in sorted_people:
    print(person)
