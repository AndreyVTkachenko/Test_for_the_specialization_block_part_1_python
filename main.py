import json

# Функция для загрузки заметок из файла
def load_notes():
    try:
        with open('notes.json', 'r') as file:
            my_notes = json.load(file)
    except FileNotFoundError:
        my_notes = []
    return my_notes


# Функция для сохранения заметок в файл
def save_notes(my_notes):
    with open('notes.json', 'w') as file:
        json.dump(my_notes, file, indent=4)

# Загрузка заметок при запуске приложения
notes = load_notes()

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