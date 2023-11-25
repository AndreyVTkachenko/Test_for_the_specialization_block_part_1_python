# Основной цикл программы
while True:
    print("\nМеню:")
    print("1. Добавить заметку")
    print("2. Показать все заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

    choice = input("Введите команду (1-5): ")

    if choice == "1":
        add_note()
    elif choice == "2":
        display_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        print("До новых встреч!")
        break
    else:
        print("Неверная команда. Попробуйте еще раз.")