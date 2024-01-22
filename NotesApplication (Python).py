import json
import datetime

class Note:
    def __init__(self, note_id, title, body, timestamp):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp

class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        note = Note(note_id, title, body, timestamp)
        self.notes.append(note)
        self.save_notes()

    def read_notes(self, date_filter=None):
        if date_filter:
            filtered_notes = [note for note in self.notes if note.timestamp.startswith(date_filter)]
            return filtered_notes
        return self.notes

    def edit_note(self, note_id, new_title, new_body):
        note = next((note for note in self.notes if note.note_id == note_id), None)
        if note:
            note.title = new_title
            note.body = new_body
            note.timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.save_notes()
            return True
        return False

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.note_id != note_id]
        self.save_notes()

    def save_notes(self):
        with open('notes.json', 'w') as file:
            notes_data = [{'id': note.note_id, 'title': note.title, 'body': note.body, 'timestamp': note.timestamp}
                          for note in self.notes]
            json.dump(notes_data, file)

def main():
    note_manager = NoteManager()

    while True:
        command = input("Введите команду (add/read/edit/delete/exit): ").lower()

        if command == 'add':
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            note_manager.add_note(title, body)
            print("Заметка успешно сохранена")

        elif command == 'read':
            date_filter = input("Введите фильтр по дате (YYYY-MM-DD): ")
            notes = note_manager.read_notes(date_filter)
            for note in notes:
                print(f"{note.note_id}. {note.title} - {note.timestamp}\n{note.body}\n")

        elif command == 'edit':
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новое тело заметки: ")
            success = note_manager.edit_note(note_id, new_title, new_body)
            if success:
                print("Заметка успешно отредактирована")
            else:
                print("Заметка с указанным ID не найдена")

        elif command == 'delete':
            note_id = int(input("Введите ID заметки для удаления: "))
            note_manager.delete_note(note_id)
            print("Заметка успешно удалена")

        elif command == 'exit':
            break

        else:
            print("Неверная команда. Пожалуйста, повторите ввод.")

if __name__ == "__main__":
    main()
