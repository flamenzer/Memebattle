# Импортируем необходимые библиотеки
import sqlite3

# Создаем класс Database
class Database:

    # Определяем конструктор класса
    def __init__(self):
        # Создаем атрибут для хранения имени файла базы данных
        self.db_file = "memes.db"

        # Создаем атрибут для хранения подключения к базе данных
        self.connection = None

        # Создаем атрибут для хранения курсора базы данных
        self.cursor = None

        # Вызываем метод класса Database для подключения к базе данных
        self.connect()

    # Создаем метод для подключения к базе данных
    def connect(self):
        # Пытаемся подключиться к базе данных с указанным именем файла
        try:
            # Создаем подключение к базе данных
            self.connection = sqlite3.connect(self.db_file)

            # Создаем курсор базы данных
            self.cursor = self.connection.cursor()

            # Выводим сообщение об успешном подключении
            print(f"Connected to database {self.db_file}")

        # Обрабатываем исключение в случае ошибки подключения
        except sqlite3.Error as e:
            # Выводим сообщение об ошибке
            print(f"Error connecting to database {self.db_file}: {e}")

    # Создаем метод для получения списка всех мемов из базы данных
    def get_memes(self):
        # Пытаемся выполнить запрос к базе данных
        try:
            # Выполняем запрос для выбора всех мемов из таблицы memes
            self.cursor.execute("SELECT * FROM memes")

            # Получаем результат запроса в виде списка кортежей
            result = self.cursor.fetchall()

            # Преобразуем список кортежей в список строк с именами файлов мемов
            memes = [row[1] for row in result]

            # Возвращаем список мемов
            return memes

        # Обрабатываем исключение в случае ошибки запроса
        except sqlite3.Error as e:
            # Выводим сообщение об ошибке
            print(f"Error getting memes from database: {e}")

            # Возвращаем пустой список
            return []

# Продолжение кода для модуля database.py

    # Создаем метод для получения списка всех ситуаций из базы данных
    def get_situations(self):
        # Пытаемся выполнить запрос к базе данных
        try:
            # Выполняем запрос для выбора всех ситуаций из таблицы situations
            self.cursor.execute("SELECT * FROM situations")

            # Получаем результат запроса в виде списка кортежей
            result = self.cursor.fetchall()

            # Преобразуем список кортежей в список строк с текстами ситуаций
            situations = [row[1] for row in result]

            # Возвращаем список ситуаций
            return situations

        # Обрабатываем исключение в случае ошибки запроса
        except sqlite3.Error as e:
            # Выводим сообщение об ошибке
            print(f"Error getting situations from database: {e}")

            # Возвращаем пустой список
            return []

