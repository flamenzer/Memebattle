# Импортируем необходимые библиотеки
import socket
import threading

# Создаем класс Server
class Server:

    # Определяем конструктор класса
    def __init__(self, game):
        # Сохраняем ссылку на экземпляр класса Game
        self.game = game

        # Создаем атрибут для хранения сокета сервера
        self.server_socket = None

        # Создаем атрибут для хранения списка сокетов клиентов
        self.client_sockets = []

        # Создаем атрибут для хранения словаря с именами клиентов
        self.client_names = {}

        # Создаем атрибут для хранения словаря с голосами клиентов
        self.client_votes = {}

    # Создаем метод для запуска сервера
    def start(self, ip, port):
        # Пытаемся создать и привязать сокет сервера
        try:
            # Создаем сокет сервера с указанными параметрами
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Привязываем сокет сервера к указанному IP-адресу и порту
            self.server_socket.bind((ip, port))

            # Выводим сообщение об успешном запуске сервера
            print(f"Server started on {ip}:{port}")

            # Вызываем метод класса Server для ожидания подключений клиентов
            self.accept_clients()

        # Обрабатываем исключение в случае ошибки создания или привязки сокета сервера
        except socket.error as e:
            # Выводим сообщение об ошибке
            print(f"Error starting server: {e}")

    # Создаем метод для ожидания подключений клиентов
    def accept_clients(self):
        # Переводим сокет сервера в режим прослушивания
        self.server_socket.listen()

        # Создаем бесконечный цикл для принятия подключений клиентов
        while True:
            # Принимаем подключение клиента и получаем его сокет и адрес
            client_socket, client_address = self.server_socket.accept()

            # Выводим сообщение о подключении клиента
            print(f"Client connected from {client_address}")

            # Добавляем сокет клиента в список сокетов клиентов
            self.client_sockets.append(client_socket)

# Продолжение кода для модуля network.py

            # Создаем отдельный поток для общения с клиентом
            client_thread = threading.Thread(target=self.communicate_client, args=(client_socket,))

            # Запускаем поток
            client_thread.start()

    # Создаем метод для общения с клиентом
    def communicate_client(self, client_socket):
        # Создаем бесконечный цикл для получения и отправки сообщений клиенту
        while True:
            # Пытаемся получить сообщение от клиента
            try:
                # Получаем сообщение от клиента в виде байтов
                message = client_socket.recv(1024)

                # Преобразуем сообщение из байтов в строку
                message = message.decode()

                # Выводим сообщение от клиента
                print(f"Message from client: {message}")

                # Вызываем метод класса Server для обработки сообщения от клиента
                self.handle_client_message(client_socket, message)

            # Обрабатываем исключение в случае ошибки получения сообщения от клиента
            except socket.error as e:
                # Выводим сообщение об ошибке
                print(f"Error communicating with client: {e}")

                # Вызываем метод класса Server для отключения клиента
                self.disconnect_client(client_socket)

                # Прерываем цикл
                break

    # Создаем метод для обработки сообщения от клиента
    def handle_client_message(self, client_socket, message):
        # Разделяем сообщение на команду и аргументы
        command, *args = message.split()

        # Проверяем, что команда равна "name"
        if command == "name":
            # Получаем имя клиента из аргументов
            name = args[0]

            # Сохраняем имя клиента в словаре с именами клиентов по ключу сокета клиента
            self.client_names[client_socket] = name

            # Выводим сообщение о получении имени клиента
            print(f"Client name received: {name}")

# Продолжение кода для модуля network.py

        # Проверяем, что команда равна "start"
        elif command == "start":
            # Проверяем, что количество клиентов равно количеству игроков в игре
            if len(self.client_sockets) == self.game.player_count:
                # Вызываем метод класса Server для начала игры
                self.start_game()

            # Иначе
            else:
                # Выводим сообщение о недостаточном количестве клиентов
                print(f"Not enough clients to start the game")

        # Проверяем, что команда равна "vote"
        elif command == "vote":
            # Получаем индекс мема, за который проголосовал клиент, из аргументов
            index = args[0]

            # Преобразуем индекс в целое число
            index = int(index)

            # Сохраняем голос клиента в словаре с голосами клиентов по ключу сокета клиента
            self.client_votes[client_socket] = index

            # Выводим сообщение о получении голоса клиента
            print(f"Client vote received: {index}")

            # Вызываем метод класса Server для подсчета голосов и очков
            self.count_votes()

        # Проверяем, что команда равна "exit"
        elif command == "exit":
            # Вызываем метод класса Server для отключения клиента
            self.disconnect_client(client_socket)

    # Создаем метод для начала игры
    def start_game(self):
        # Выводим сообщение о начале игры
        print(f"Game started")

        # Вызываем метод класса Game для инициализации колод мемов и ситуаций
        self.game.init_decks()

        # Вызываем метод класса Game для раздачи мемов и ситуаций игрокам
        self.game.deal_cards()

        # Создаем цикл для отправки мемов и ситуаций всем клиентам
        for i in range(self.game.player_count):
            # Получаем сокет клиента по индексу из списка сокетов клиентов
            client_socket = self.client_sockets[i]

            # Получаем мем игрока по индексу из списка мемов игрока
            meme = self.game.player_memes[i]

            # Получаем ситуацию игрока по индексу из списка ситуаций игрока
            situation = self.game.player_situations[i]

# Продолжение кода для модуля network.py

            # Создаем сообщение с мемом и ситуацией игрока
            message = f"meme {i} {meme}\nsituation {i} {situation}"

            # Вызываем метод класса Server для отправки сообщения клиенту
            self.send_message(client_socket, message)

    # Создаем метод для подсчета голосов и очков
    def count_votes(self):
        # Проверяем, что количество голосов равно количеству клиентов
        if len(self.client_votes) == len(self.client_sockets):
            # Создаем словарь для хранения количества голосов за каждый мем
            meme_votes = {}

            # Создаем цикл для подсчета голосов за каждый мем
            for index in self.client_votes.values():
                # Проверяем, что индекс мема в допустимом диапазоне
                if 0 <= index < self.game.player_count:
                    # Увеличиваем количество голосов за мем по индексу на единицу
                    meme_votes[index] = meme_votes.get(index, 0) + 1

            # Находим максимальное количество голосов среди всех мемов
            max_votes = max(meme_votes.values())

            # Создаем список для хранения индексов мемов с максимальным количеством голосов
            max_meme_indexes = []

            # Создаем цикл для нахождения индексов мемов с максимальным количеством голосов
            for index, votes in meme_votes.items():
                # Проверяем, что количество голосов равно максимальному
                if votes == max_votes:
                    # Добавляем индекс в список
                    max_meme_indexes.append(index)

            # Выбираем случайный индекс из списка мемов с максимальным количеством голосов
            winner_index = random.choice(max_meme_indexes)

            # Выводим сообщение о победителе раунда
            print(f"Round winner: {winner_index}")

# Продолжение кода для модуля network.py

    # Создаем метод для отправки сообщения всем клиентам
    def send_message_all(self, message):
        # Создаем цикл для отправки сообщения каждому клиенту
        for client_socket in self.client_sockets:
            # Вызываем метод класса Server для отправки сообщения конкретному клиенту
            self.send_message(client_socket, message)

    # Создаем метод для отправки сообщения конкретному клиенту
    def send_message(self, client_socket, message):
        # Пытаемся отправить сообщение клиенту
        try:
            # Преобразуем сообщение из строки в байты
            message = message.encode()

            # Отправляем сообщение клиенту
            client_socket.send(message)

            # Выводим сообщение, отправленное клиенту
            print(f"Message sent to client: {message}")

        # Обрабатываем исключение в случае ошибки отправки сообщения клиенту
        except socket.error as e:
            # Выводим сообщение об ошибке
            print(f"Error sending message to client: {e}")

    # Создаем метод для отключения клиента
    def disconnect_client(self, client_socket):
        # Пытаемся отключить клиента
        try:
            # Закрываем сокет клиента
            client_socket.close()

            # Удаляем сокет клиента из списка сокетов клиентов
            self.client_sockets.remove(client_socket)

            # Удаляем имя клиента из словаря с именами клиентов
            del self.client_names[client_socket]

            # Удаляем голос клиента из словаря с голосами клиентов
            del self.client_votes[client_socket]

            # Выводим сообщение об отключении клиента
            print(f"Client disconnected")

        # Обрабатываем исключение в случае ошибки отключения клиента
        except socket.error as e:
            # Выводим сообщение об ошибке
            print(f"Error disconnecting client: {e}")

    # Создаем метод для закрытия сокета сервера
    def close(self):
        # Пытаемся закрыть сокет сервера
        try:
            # Закрываем сокет сервера
            self.server_socket.close()

            # Выводим сообщение о закрытии сервера
            print(f"Server closed")

        # Обрабатываем исключение в случае ошибки закрытия сокета сервера
        except socket.error as e:
            # Выводим сообщение об ошибке
            print(f"Error closing server: {e}")

# Продолжение кода для модуля network.py

# Создаем класс Client
class Client:

    # Определяем конструктор класса
    def __init__(self, game):
        # Сохраняем ссылку на экземпляр класса Game
        self.game = game

        # Создаем атрибут для хранения сокета клиента
        self.client_socket = None

        # Создаем атрибут для хранения флага подключения к серверу
        self.connected = False

    # Создаем метод для подключения к серверу
    def connect(self, ip, port):
        # Пытаемся создать и подключить сокет клиента
        try:
            # Создаем сокет клиента с указанными параметрами
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Подключаем сокет клиента к указанному IP-адресу и порту
            self.client_socket.connect((ip, port))

            # Устанавливаем флаг подключения к серверу в True
            self.connected = True

            # Выводим сообщение об успешном подключении к серверу
            print(f"Connected to server {ip}:{port}")

            # Вызываем метод класса Client для отправки имени клиента серверу
            self.send_name()

            # Вызываем метод класса Client для получения сообщений от сервера
            self.receive_messages()

        # Обрабатываем исключение в случае ошибки создания или подключения сокета клиента
        except socket.error as e:
            # Выводим сообщение об ошибке
            print(f"Error connecting to server: {e}")

    # Создаем метод для отправки имени клиента серверу
    def send_name(self):
        # Получаем имя клиента от пользователя
        name = input("Enter your name: ")

        # Создаем сообщение с именем клиента
        message = f"name {name}"

        # Вызываем метод класса Client для отправки сообщения серверу
        self.send_message(message)

# Продолжение кода для модуля network.py

    # Создаем метод для получения сообщений от сервера
    def receive_messages(self):
        # Создаем отдельный поток для получения сообщений от сервера
        receive_thread = threading.Thread(target=self.receive_loop)

        # Запускаем поток
        receive_thread.start()

    # Создаем метод для бесконечного цикла получения сообщений от сервера
    def receive_loop(self):
        # Создаем бесконечный цикл для получения сообщений от сервера
        while True:
            # Пытаемся получить сообщение от сервера
            try:
                # Получаем сообщение от сервера в виде байтов
                message = self.client_socket.recv(1024)

                # Преобразуем сообщение из байтов в строку
                message = message.decode()

                # Выводим сообщение от сервера
                print(f"Message from server: {message}")

                # Вызываем метод класса Client для обработки сообщения от сервера
                self.handle_server_message(message)

            # Обрабатываем исключение в случае ошибки получения сообщения от сервера
            except socket.error as e:
                # Выводим сообщение об ошибке
                print(f"Error receiving message from server: {e}")

                # Вызываем метод класса Client для отключения от сервера
                self.disconnect()

                # Прерываем цикл
                break

    # Создаем метод для обработки сообщения от сервера
    def handle_server_message(self, message):
        # Разделяем сообщение на команду и аргументы
        command, *args = message.split()

        # Проверяем, что команда равна "meme"
        if command == "meme":
            # Получаем индекс и изображение мема из аргументов
            index, image = args

            # Преобразуем индекс в целое число
            index = int(index)

            # Вызываем метод класса Game для обновления изображения мема игрока
            self.game.update_player_meme(index, image)

# Продолжение кода для модуля network.py

        # Проверяем, что команда равна "situation"
        elif command == "situation":
            # Получаем индекс и текст ситуации из аргументов
            index, text = args

            # Преобразуем индекс в целое число
            index = int(index)

            # Вызываем метод класса Game для обновления текста ситуации игрока
            self.game.update_player_situation(index, text)

        # Проверяем, что команда равна "start"
        elif command == "start":
            # Вызываем метод класса Game для начала игры
            self.game.start_game()

    # Создаем метод для отправки сообщения серверу
    def send_message(self, message):
        # Пытаемся отправить сообщение серверу
        try:
            # Преобразуем сообщение из строки в байты
            message = message.encode()

            # Отправляем сообщение серверу
            self.client_socket.send(message)

            # Выводим сообщение, отправленное серверу
            print(f"Message sent to server: {message}")

        # Обрабатываем исключение в случае ошибки отправки сообщения серверу
        except socket.error as e:
            # Выводим сообщение об ошибке
            print(f"Error sending message to server: {e}")

    # Создаем метод для отключения от сервера
    def disconnect(self):
        # Пытаемся отключиться от сервера
        try:
            # Закрываем сокет клиента
            self.client_socket.close()

            # Устанавливаем флаг подключения к серверу в False
            self.connected = False

            # Выводим сообщение об отключении от сервера
            print(f"Disconnected from server")

        # Обрабатываем исключение в случае ошибки отключения от сервера
        except socket.error as e:
            # Выводим сообщение об ошибке
            print(f"Error disconnecting from server: {e}")

