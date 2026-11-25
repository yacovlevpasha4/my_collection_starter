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
cursor.execute("INSERT INTO items (title, year, genre, image_url, description) VALUES ('Поднятие уровня в одиночку (Solo Leveling)', 2018, 'Экшен, Фэнтези', 'https://clck.ru/3WiGxp', 'Охотник ранга E, считавшийся слабейшим в мире, получает уникальную систему.')")
cursor.execute("INSERT INTO items (title, year, genre, image_url, description) VALUES ('Человек-бензопила (Chainsaw Man)', 2018, 'Экшен, Ужасы', 'https://clck.ru/3WiH2b', 'Дэндзи, бедный юноша, сливается со своим демоном-питомцем.')")
cursor.execute("INSERT INTO items (title, year, genre, image_url, description) VALUES ('Истинная красота (True Beauty)', 2018, 'Романтика, Повседневность', 'https://clck.ru/3WiH5C', 'Старшеклассница осваивает искусство макияжа и превращается в школьную богиню.')")
cursor.execute("INSERT INTO items (title, year, genre, image_url, description) VALUES ('Атака титанов (Attack on Titan)', 2009, 'Экшен, Драма', 'https://clck.ru/3WiH7k', 'Человечество живет за огромными стенами, защищающими их от гигантских людоедов-титанов.')")
cursor.execute("INSERT INTO items (title, year, genre, image_url, description) VALUES ('Бастард (Bastard)', 2014, 'Триллер, Психология', 'https://clck.ru/3WiHAp', 'Тихий школьник узнает страшную тайну: его уважаемый отец является серийным убийцей.')")
cursor.execute("INSERT INTO items (title, year, genre, image_url, description) VALUES ('Волейбол!! (Haikyuu!!)', 2012, 'Спорт, Повседневность', 'https://clck.ru/3WiHDQ', 'Низкорослый, но невероятно прыгучий Хината поступает в старшую школу.')")
cursor.execute("INSERT INTO items (title, year, genre, image_url, description) VALUES ('Берсерк (Berserk)', 1989, 'Тёмное фэнтези, Экшен', 'https://clck.ru/3WimzQ', 'История Гатса, Черного Мечника, который бродит по мрачному средневековому миру.')")
cursor.execute("INSERT INTO items (title, year, genre, image_url, description) VALUES ('Семья шпиона (Spy x Family)', 2019, 'Комедия, Повседневность', 'https://clck.ru/3WinC2', 'Шпион, наемная убийца и девочка-телепат случайно создают фиктивную семью.')")

# 4. Сохраняем изменения и закрываем файл
conn.commit()
conn.close()

print("База данных collection.db успешно создана!")