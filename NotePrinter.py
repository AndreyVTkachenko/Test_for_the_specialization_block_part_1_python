import datetime


class NotePrinter:
    @staticmethod
    def display_notes(notes):
        """
        Функция для отображения всех заметок
        :param notes: все заметки
        :return: отображение всех заметок
        """
        if not notes:
            print("Нет доступных заметок.")
        else:
            for note in notes:
                print(f"ID: {note['id']}")
                print(f"Заголовок: {note['title']}")
                print(f"Тело: {note['body']}")
                print(f"Дата/время: {note['timestamp']}")
                print()

    @staticmethod
    def display_specific_note(note):
        """
        Функция для отображения определенной заметки по ID
        :param note: заметка
        :return: отображение заметки в соответствии с ID
        """
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Тело: {note['body']}")
        print(f"Дата/время: {note['timestamp']}")

    @classmethod
    def filter_notes_by_date(cls, notes):
        """
        Функция для выборки заметок по дате
        :param notes: заметки
        :return: отображение всех заметок с определённой датой
        """
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
            cls.display_notes(filtered_notes)
