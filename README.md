# Простое приложение для ведения заметок
Этот скрипт на Python реализует простое приложение для ведения заметок, где пользователи могут добавлять, читать, редактировать и удалять заметки. Приложение использует объектно-ориентированный подход с двумя классами: Note и NoteManager.

## Функциональность
* **Добавление заметки:** Пользователи могут добавить новую заметку, предоставив заголовок и текст заметки. Каждой заметке присваивается уникальный идентификатор и временная метка.

* **Чтение заметок:** Пользователи могут просматривать все заметки или фильтровать заметки по указанной дате.

* **Редактирование заметки:** Пользователи могут редактировать конкретную заметку, указав её идентификатор, новый заголовок и новый текст.

* **Удаление заметки:** Пользователи могут удалить заметку, предоставив её идентификатор.

* **Сохранение заметок:** Приложение сохраняет заметки в JSON-файл (notes.json), обеспечивая сохранение данных между сеансами.

## Использование
Запустите скрипт и введите команды:

* **add:** Добавить новую заметку.
* **read:** Просмотреть существующие заметки (возможно с фильтрацией по дате).

* **edit:** Редактировать заметку, предоставив её идентификатор, новый заголовок и новый текст.
* **delete:** Удалить заметку, предоставив её идентификатор.
exit: Выйти из приложения.

### Пример

* Введите команду (add/read/edit/delete/exit): **"add"**
* Введите заголовок заметки: **"Встреча"**
* Введите тело заметки: **"Обсудить обновления проекта""**
* **"Заметка успешно сохранена"**

* Введите команду (add/read/edit/delete/exit): **"read"**
* Введите фильтр по дате (YYYY-MM-DD): **"2022-01-22"**
**1. Встреча - 2022-01-22 12:30:45
Обсудить обновления проекта**
***
* Введите команду (add/read/edit/delete/exit): **""edit""**

* Введите ID заметки для редактирования: **"1"**
* Введите новый заголовок заметки: **"Обновленная встреча"**
* Введите новое тело заметки: **"Обсудить пересмотренные цели проекта"**
* **"Заметка успешно отредактирована"**
***
* Введите команду (add/read/edit/delete/exit): **""exit""**