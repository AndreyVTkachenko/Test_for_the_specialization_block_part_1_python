import datetime


class NoteEditor:
    @staticmethod
    def add_note(notes):
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
        print("Заметка успешно сохранена.")

    @staticmethod
    def delete_note(notes):
        note_id = int(input("Введите ID заметки для удаления: "))
        for note in notes:
            if note['id'] == note_id:
                notes.remove(note)
                print("Заметка успешно удалена.")
                return
        print("Заметка с указанным ID не найдена.")

    @staticmethod
    def edit_note(notes):
        note_id = int(input("Введите ID заметки для редактирования: "))
        for note in notes:
            if note['id'] == note_id:
                title = input("Введите новый заголовок заметки: ")
                body = input("Введите новое тело заметки: ")
                note['title'] = title
                note['body'] = body
                note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("Заметка успешно отредактирована.")
                return
        print("Заметка с указанным ID не найдена.")
