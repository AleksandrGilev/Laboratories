books_dict = {}

while True:
    print("\nМеню:\n1. Добавить книгу\n2. Найти книгу\n3. Показать все книги\n4. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        author = input("Введите автора: ")
        book = input("Введите название книги: ")

        if author in books_dict:
            if book in books_dict[author]:
                print(f"Книга '{book}' автора '{author}' уже существует.")
            else:
                books_dict[author].append(book)
        else:
            books_dict[author] = [book]
            print(f"Книга '{book}' автора '{author}' добавлена.")

    elif choice == "2":
        author = input("Введите автора: ")

        if author in books_dict:
            print(f"Книги автора '{author}': {books_dict[author]}")
        else:
            print(f"Книги автора '{author}' не найдены.")

    elif choice == "3":
        print(books_dict)

    elif choice == "4":
        print("Программа завершена. До свидания!")
        break

    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")
