import datetime
import json


# Функция для загрузки заметок из файла
def load_notes():
    try:
        with open('notes.json', 'r', encoding='utf-8') as file:
            my_notes = json.load(file)
    except FileNotFoundError:
        my_notes = []
    return my_notes


# Функция для сохранения заметок в файл
def save_notes(my_notes):
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(my_notes, file, indent=4, ensure_ascii=False)


# Загрузка заметок при запуске приложения
notes = load_notes()


# Функция для добавления новой заметки
def add_note():
    if notes:
        last_id = notes[-1]['id']
    else:
        last_id = 0

    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    note = {
        'id': last_id + 1,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена.")


# Функция для удаления заметки
def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным ID не найдена.")


# Функция для редактирования заметки
def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            note['title'] = title
            note['body'] = body
            note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")


# Функция для отображения всех заметок
def display_notes():
    if not notes:
        print("Нет доступных заметок.")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело: {note['body']}")
            print(f"Дата/время: {note['timestamp']}")
            print()


# Функция для выборки заметок по дате
def filter_notes_by_date():
    date_str = input("Введите дату в формате YYYY-MM-DD: ")
    try:
        target_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Неверный формат даты. Попробуйте еще раз.")
        return

    filtered_notes = [note for note in notes if
                      datetime.datetime.strptime(note['timestamp'], "%Y-%m-%d %H:%M:%S").date() == target_date]

    if not filtered_notes:
        print("Заметок на указанную дату нет.")
    else:
        for note in filtered_notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело: {note['body']}")
            print(f"Дата/время: {note['timestamp']}")
            print()


# Функция для отображения определенной заметки по ID
def display_specific_note():
    note_id = int(input("Введите ID заметки для отображения: "))
    for note in notes:
        if note['id'] == note_id:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Тело: {note['body']}")
            print(f"Дата/время: {note['timestamp']}")
            return
    print("Заметка с указанным ID не найдена.")


# Основной цикл программы
while True:
    print("\nМеню:")
    print("1. Добавить заметку")
    print("2. Показать все заметки")
    print("3. Выборка заметок по дате")
    print("4. Показать определенную заметку по ID")
    print("5. Редактировать заметку")
    print("6. Удалить заметку")
    print("0. Выйти")

    choice = input("Введите команду (1-5): ")

    if choice == "1":
        add_note()
    elif choice == "2":
        display_notes()
    elif choice == "3":
        filter_notes_by_date()
    elif choice == "4":
        display_specific_note()
    elif choice == "5":
        edit_note()
    elif choice == "6":
        delete_note()
    elif choice == "0":
        print("До новых встреч!")
        break
    else:
        print("Неверная команда. Попробуйте еще раз.")
