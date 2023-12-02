import json


class NoteManager:
    def __init__(self):
        """
        Функция для загрузки заметок из файла
        """
        self.notes = self.load_notes()

    def load_notes(self):
        """
        Загрузка заметок при запуске приложения
        :return: заметки
        """
        try:
            with open('notes.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_notes(self):
        """
        Функция для сохранения заметок в файл
        :return: заметки
        """
        with open('notes.json', 'w', encoding='utf-8') as file:
            json.dump(self.notes, file, indent=4, ensure_ascii=False)
