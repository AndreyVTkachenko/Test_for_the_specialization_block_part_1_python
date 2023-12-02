from NoteEditor import NoteEditor
from NotePrinter import NotePrinter
from NoteManager import NoteManager


class NoteApp:
    def __init__(self):
        """
        Создание связей между классами
        """
        self.note_manager = NoteManager()
        self.note_printer = NotePrinter()
        self.note_editor = NoteEditor()

    def run(self):
        """
        Основной цикл программы
        """
        while True:
            print("\nМеню:")
            print("1. Добавить заметку")
            print("2. Показать все заметки")
            print("3. Выборка заметок по дате")
            print("4. Показать определенную заметку по ID")
            print("5. Редактировать заметку")
            print("6. Удалить заметку")
            print("0. Выйти")

            choice = input("Введите команду (0-6): ")

            if choice == "1":
                self.note_editor.add_note(self.note_manager.notes)
                self.note_manager.save_notes()
            elif choice == "2":
                self.note_printer.display_notes(self.note_manager.notes)
            elif choice == "3":
                self.note_printer.filter_notes_by_date(self.note_manager.notes)
            elif choice == "4":
                note_id = int(input("Введите ID заметки для отображения: "))
                specific_note = next((note for note in self.note_manager.notes if note['id'] == note_id), None)
                if specific_note:
                    self.note_printer.display_specific_note(specific_note)
                else:
                    print("Заметка с указанным ID не найдена.")
            elif choice == "5":
                self.note_editor.edit_note(self.note_manager.notes)
                self.note_manager.save_notes()
            elif choice == "6":
                self.note_editor.delete_note(self.note_manager.notes)
                self.note_manager.save_notes()
            elif choice == "0":
                print("До новых встреч!")
                break
            else:
                print("Неверная команда. Попробуйте еще раз.")
                