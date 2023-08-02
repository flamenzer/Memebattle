# Импортируем необходимые библиотеки
import random
from database import Database
from network import Server, Client

# Создаем класс Game
class Game:

    # Определяем конструктор класса
    def __init__(self, gui):
        # Сохраняем ссылку на экземпляр класса GUI
        self.gui = gui

        # Создаем экземпляр класса Database
        self.database = Database()

        # Создаем экземпляр класса Server
        self.server = Server(self)

        # Создаем экземпляр класса Client
        self.client = Client(self)

        # Создаем атрибут для хранения количества игроков в игре
        self.player_count = 5

        # Создаем атрибут для хранения количества очков для победы в игре
        self.win_score = 10

        # Создаем атрибут для хранения колоды мемов
        self.meme_deck = []

        # Создаем атрибут для хранения колоды ситуаций
        self.situation_deck = []

        # Создаем атрибут для хранения мемов игрока
        self.player_memes = []

        # Создаем атрибут для хранения ситуаций игрока
        self.player_situations = []

        # Создаем атрибут для хранения общего мема
        self.common_meme = None

        # Создаем атрибут для хранения общей ситуации
        self.common_situation = None

        # Создаем атрибут для хранения выбранного мема игрока
        self.selected_player_meme = None

        # Создаем атрибут для хранения выбранной ситуации игрока
        self.selected_player_situation = None

# Продолжение кода для модуля game.py

    # Создаем метод для подключения к серверу
    def connect_server(self, ip, port):
        # Вызываем метод класса Client для подключения к серверу с указанным IP-адресом и портом
        self.client.connect(ip, port)

    # Создаем метод для начала игры
    def start_game(self):
        # Проверяем, что клиент подключен к серверу
        if self.client.connected:
            # Вызываем метод класса Client для отправки сообщения о начале игры
            self.client.send_message("start")

    # Создаем метод для выхода из игры
    def exit_game(self):
        # Проверяем, что клиент подключен к серверу
        if self.client.connected:
            # Вызываем метод класса Client для отправки сообщения о выходе из игры
            self.client.send_message("exit")

            # Вызываем метод класса Client для отключения от сервера
            self.client.disconnect()

        # Закрываем приложение
        self.gui.close()

    # Создаем метод для инициализации колод мемов и ситуаций
    def init_decks(self):
        # Получаем список всех мемов из базы данных
        memes = self.database.get_memes()

        # Перемешиваем список мемов
        random.shuffle(memes)

        # Копируем список мемов в колоду мемов
        self.meme_deck = memes.copy()

        # Получаем список всех ситуаций из базы данных
        situations = self.database.get_situations()

        # Перемешиваем список ситуаций
        random.shuffle(situations)

        # Копируем список ситуаций в колоду ситуаций
        self.situation_deck = situations.copy()

# Продолжение кода для модуля game.py

    # Создаем метод для раздачи мемов и ситуаций игрокам
    def deal_cards(self):
        # Проверяем, что колода мемов не пуста
        if self.meme_deck:
            # Создаем цикл для раздачи 7 мемов каждому игроку
            for i in range(7):
                # Извлекаем первый мем из колоды мемов
                meme = self.meme_deck.pop(0)

                # Добавляем мем в список мемов игрока
                self.player_memes.append(meme)

                # Вызываем метод класса GUI для обновления изображения мема игрока
                self.gui.update_player_meme(i, meme)

        # Проверяем, что колода ситуаций не пуста
        if self.situation_deck:
            # Создаем цикл для раздачи 7 ситуаций каждому игроку
            for i in range(7):
                # Извлекаем первую ситуацию из колоды ситуаций
                situation = self.situation_deck.pop(0)

                # Добавляем ситуацию в список ситуаций игрока
                self.player_situations.append(situation)

                # Вызываем метод класса GUI для обновления текста ситуации игрока
                self.gui.update_player_situation(i, situation)

    # Создаем метод для выбора мема игрока
    def select_player_meme(self, index):
        # Проверяем, что индекс мема в допустимом диапазоне
        if 0 <= index < len(self.player_memes):
            # Получаем мем по индексу из списка мемов игрока
            meme = self.player_memes[index]

            # Сохраняем выбранный мем в атрибуте класса
            self.selected_player_meme = meme

            # Вызываем метод класса GUI для выделения выбранного мема игрока
            self.gui.highlight_player_meme(index)

# Продолжение кода для модуля game.py

    # Создаем метод для выбора ситуации игрока
    def select_player_situation(self, index):
        # Проверяем, что индекс ситуации в допустимом диапазоне
        if 0 <= index < len(self.player_situations):
            # Получаем ситуацию по индексу из списка ситуаций игрока
            situation = self.player_situations[index]

            # Сохраняем выбранную ситуацию в атрибуте класса
            self.selected_player_situation = situation

            # Вызываем метод класса GUI для выделения выбранной ситуации игрока
            self.gui.highlight_player_situation(index)

    # Создаем метод для выбора общего мема
    def select_common_meme(self):
        # Проверяем, что колода мемов не пуста
        if self.meme_deck:
            # Извлекаем первый мем из колоды мемов
            meme = self.meme_deck.pop(0)

            # Сохраняем выбранный мем в атрибуте класса
            self.common_meme = meme

            # Вызываем метод класса GUI для обновления изображения общего мема
            self.gui.update_common_meme(meme)

    # Создаем метод для выбора общей ситуации
    def select_common_situation(self):
        # Проверяем, что колода ситуаций не пуста
        if self.situation_deck:
            # Извлекаем первую ситуацию из колоды ситуаций
            situation = self.situation_deck.pop(0)

            # Сохраняем выбранную ситуацию в атрибуте класса
            self.common_situation = situation

            # Вызываем метод класса GUI для обновления текста общей ситуации
            self.gui.update_common_situation(situation)

# Продолжение кода для модуля game.py

    # Создаем метод для выбора ситуации игрока
    def select_player_situation(self, index):
        # Проверяем, что индекс ситуации в допустимом диапазоне
        if 0 <= index < len(self.player_situations):
            # Получаем ситуацию по индексу из списка ситуаций игрока
            situation = self.player_situations[index]

            # Сохраняем выбранную ситуацию в атрибуте класса
            self.selected_player_situation = situation

            # Вызываем метод класса GUI для выделения выбранной ситуации игрока
            self.gui.highlight_player_situation(index)

    # Создаем метод для выбора общего мема
    def select_common_meme(self):
        # Проверяем, что колода мемов не пуста
        if self.meme_deck:
            # Извлекаем первый мем из колоды мемов
            meme = self.meme_deck.pop(0)

            # Сохраняем выбранный мем в атрибуте класса
            self.common_meme = meme

            # Вызываем метод класса GUI для обновления изображения общего мема
            self.gui.update_common_meme(meme)

    # Создаем метод для выбора общей ситуации
    def select_common_situation(self):
        # Проверяем, что колода ситуаций не пуста
        if self.situation_deck:
            # Извлекаем первую ситуацию из колоды ситуаций
            situation = self.situation_deck.pop(0)

            # Сохраняем выбранную ситуацию в атрибуте класса
            self.common_situation = situation

            # Вызываем метод класса GUI для обновления текста общей ситуации
            self.gui.update_common_situation(situation)

