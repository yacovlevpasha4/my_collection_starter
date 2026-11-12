import sqlite3

# 1. Создаем (или подключаемся к) файлу базы данных
conn = sqlite3.connect('collection.db')
cursor = conn.cursor()

# 2. Создаем таблицу 'items', если её еще не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        year INTEGER,
        genre TEXT,
        image_url TEXT,
        description TEXT
    )
''')

# 3. Добавляем пару тестовых записей, чтобы сразу было что показать
cursor.execute("INSERT INTO items (title, year, genre, image_url, description) VALUES ('Тестовый фильм', 2024, 'Драма', 'https://via.placeholder.com/300', 'Описание для теста')")

# 4. Сохраняем изменения и закрываем файл
conn.commit()
conn.close()

print("База данных collection.db успешно создана!")