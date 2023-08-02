# Импортируем необходимые библиотеки
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLabel, QPushButton, QGroupBox, QVBoxLayout, QHBoxLayout, QInputDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

# Создаем класс GUI, наследуемый от класса QMainWindow
class GUI(QMainWindow):

    # Определяем конструктор класса
    def __init__(self):
        # Вызываем конструктор родительского класса
        super().__init__()

        # Устанавливаем заголовок окна
        self.setWindowTitle("Meme Battle")

        # Устанавливаем размер окна
        self.resize(800, 600)

        # Создаем центральный виджет
        self.central_widget = QWidget()

        # Создаем сеточный компоновщик для центрального виджета
        self.grid_layout = QGridLayout()

        # Добавляем центральный виджет в окно
        self.setCentralWidget(self.central_widget)

        # Добавляем сеточный компоновщик к центральному виджету
        self.central_widget.setLayout(self.grid_layout)

        # Создаем виджеты для отображения мемов и ситуаций
        self.create_meme_widgets()

        # Создаем виджеты для отображения голосов и очков
        self.create_score_widgets()

        # Создаем виджеты для управления игрой
        self.create_control_widgets()

    # Создаем метод для создания виджетов для отображения мемов и ситуаций
    def create_meme_widgets(self):
        # Создаем групповой виджет для мемов игрока
        self.player_meme_group = QGroupBox("Your memes")

        # Создаем вертикальный компоновщик для группового виджета
        self.player_meme_layout = QVBoxLayout()

        # Добавляем групповой виджет в сеточный компоновщик
        self.grid_layout.addWidget(self.player_meme_group, 0, 0)

        # Добавляем вертикальный компоновщик к групповому виджету
        self.player_meme_group.setLayout(self.player_meme_layout)

        # Создаем список для хранения меток с изображениями мемов игрока
        self.player_meme_labels = []

        # Создаем цикл для создания 7 меток с изображениями мемов игрока
        for i in range(7):
            # Создаем метку с изображением мема игрока
            player_meme_label = QLabel()

            # Устанавливаем размер метки
            player_meme_label.setFixedSize(100, 100)

            # Устанавливаем выравнивание метки по центру
            player_meme_label.setAlignment(Qt.AlignCenter)

            # Добавляем метку в список
            self.player_meme_labels.append(player_meme_label)

            # Добавляем метку в вертикальный компоновщик
            self.player_meme_layout.addWidget(player_meme_label)

            # Связываем событие нажатия на метку с методом выбора мема игрока
            player_meme_label.mousePressEvent = lambda event, index=i: self.select_player_meme(index)

        # Создаем групповой виджет для общего мема
        self.common_meme_group = QGroupBox("Common meme")

        # Создаем горизонтальный компоновщик для группового виджета
        self.common_meme_layout = QHBoxLayout()

        # Добавляем групповой виджет в сеточный компоновщик
        self.grid_layout.addWidget(self.common_meme_group, 0, 1)

        # Добавляем горизонтальный компоновщик к групповому виджету
        self.common_meme_group.setLayout(self.common_meme_layout)

        # Создаем метку с изображением общего мема
        self.common_meme_label = QLabel()

        # Продолжение кода для модуля gui.py

        # Устанавливаем размер метки
        self.common_meme_label.setFixedSize(300, 300)

        # Устанавливаем выравнивание метки по центру
        self.common_meme_label.setAlignment(Qt.AlignCenter)

        # Добавляем метку в горизонтальный компоновщик
        self.common_meme_layout.addWidget(self.common_meme_label)

        # Связываем событие нажатия на метку с методом выбора общего мема
        self.common_meme_label.mousePressEvent = lambda event: self.select_common_meme()

        # Создаем групповой виджет для ситуаций игрока
        self.player_situation_group = QGroupBox("Your situations")

        # Создаем вертикальный компоновщик для группового виджета
        self.player_situation_layout = QVBoxLayout()

        # Добавляем групповой виджет в сеточный компоновщик
        self.grid_layout.addWidget(self.player_situation_group, 0, 2)

        # Добавляем вертикальный компоновщик к групповому виджету
        self.player_situation_group.setLayout(self.player_situation_layout)

        # Создаем список для хранения меток с текстами ситуаций игрока
        self.player_situation_labels = []

        # Создаем цикл для создания 7 меток с текстами ситуаций игрока
        for i in range(7):
            # Создаем метку с текстом ситуации игрока
            player_situation_label = QLabel()

            # Устанавливаем размер метки
            player_situation_label.setFixedSize(100, 100)

            # Устанавливаем выравнивание метки по центру
            player_situation_label.setAlignment(Qt.AlignCenter)

            # Устанавливаем перенос текста по словам
            player_situation_label.setWordWrap(True)

            # Добавляем метку в список
            self.player_situation_labels.append(player_situation_label)

            # Добавляем метку в вертикальный компоновщик
            self.player_situation_layout.addWidget(player_situation_label)

            # Связываем событие нажатия на метку с методом выбора ситуации игрока
            player_situation_label.mousePressEvent = lambda event, index=i: self.select_player_situation(index)

        # Создаем групповой виджет для общей ситуации
        self.common_situation_group = QGroupBox("Common situation")

        # Создаем горизонтальный компоновщик для группового виджета
        self.common_situation_layout = QHBoxLayout()

        # Добавляем групповой виджет в сеточный компоновщик
        self.grid_layout.addWidget(self.common_situation_group, 1, 1)

        # Добавляем горизонтальный компоновщик к групповому виджету
        self.common_situation_group.setLayout(self.common_situation_layout)

        # Создаем метку с текстом общей ситуации
        self.common_situation_label = QLabel()

# Продолжение кода для модуля gui.py

        # Устанавливаем размер метки
        self.common_situation_label.setFixedSize(300, 100)

        # Устанавливаем выравнивание метки по центру
        self.common_situation_label.setAlignment(Qt.AlignCenter)

        # Устанавливаем перенос текста по словам
        self.common_situation_label.setWordWrap(True)

        # Добавляем метку в горизонтальный компоновщик
        self.common_situation_layout.addWidget(self.common_situation_label)

        # Связываем событие нажатия на метку с методом выбора общей ситуации
        self.common_situation_label.mousePressEvent = lambda event: self.select_common_situation()

    # Создаем метод для создания виджетов для отображения голосов и очков
    def create_score_widgets(self):
        # Создаем групповой виджет для голосов игроков
        self.player_vote_group = QGroupBox("Your votes")

        # Создаем вертикальный компоновщик для группового виджета
        self.player_vote_layout = QVBoxLayout()

        # Добавляем групповой виджет в сеточный компоновщик
        self.grid_layout.addWidget(self.player_vote_group, 2, 0)

        # Добавляем вертикальный компоновщик к групповому виджету
        self.player_vote_group.setLayout(self.player_vote_layout)

        # Создаем список для хранения кнопок с голосами игроков
        self.player_vote_buttons = []

        # Создаем цикл для создания 5 кнопок с голосами игроков
        for i in range(5):
            # Создаем кнопку с голосом игрока
            player_vote_button = QPushButton()

            # Устанавливаем размер кнопки
            player_vote_button.setFixedSize(100, 100)

            # Устанавливаем шрифт кнопки
            player_vote_button.setFont(QFont("Arial", 16))

            # Добавляем кнопку в список
            self.player_vote_buttons.append(player_vote_button)

            # Добавляем кнопку в вертикальный компоновщик
            self.player_vote_layout.addWidget(player_vote_button)

            # Связываем событие нажатия на кнопку с методом голосования за мем игрока
            player_vote_button.clicked.connect(lambda checked, index=i: self.vote_player_meme(index))

        # Создаем групповой виджет для очков игроков
        self.player_score_group = QGroupBox("Your score")

        # Создаем вертикальный компоновщик для группового виджета
        self.player_score_layout = QVBoxLayout()

        # Добавляем групповой виджет в сеточный компоновщик
        self.grid_layout.addWidget(self.player_score_group, 2, 2)

        # Добавляем вертикальный компоновщик к групповому виджету
        self.player_score_group.setLayout(self.player_score_layout)

# Продолжение кода для модуля gui.py

        # Создаем метку с очками игрока
        self.player_score_label = QLabel()

        # Устанавливаем размер метки
        self.player_score_label.setFixedSize(100, 100)

        # Устанавливаем выравнивание метки по центру
        self.player_score_label.setAlignment(Qt.AlignCenter)

        # Устанавливаем шрифт метки
        self.player_score_label.setFont(QFont("Arial", 16))

        # Добавляем метку в вертикальный компоновщик
        self.player_score_layout.addWidget(self.player_score_label)

    # Создаем метод для создания виджетов для управления игрой
    def create_control_widgets(self):
        # Создаем групповой виджет для управления игрой
        self.control_group = QGroupBox("Game control")

        # Создаем горизонтальный компоновщик для группового виджета
        self.control_layout = QHBoxLayout()

        # Добавляем групповой виджет в сеточный компоновщик
        self.grid_layout.addWidget(self.control_group, 2, 1)

        # Добавляем горизонтальный компоновщик к групповому виджету
        self.control_group.setLayout(self.control_layout)

        # Создаем кнопку для подключения к серверу
        self.connect_button = QPushButton("Connect")

        # Устанавливаем размер кнопки
        self.connect_button.setFixedSize(100, 50)

        # Устанавливаем шрифт кнопки
        self.connect_button.setFont(QFont("Arial", 16))

        # Добавляем кнопку в горизонтальный компоновщик
        self.control_layout.addWidget(self.connect_button)

        # Связываем событие нажатия на кнопку с методом подключения к серверу
        self.connect_button.clicked.connect(self.connect_server)

        # Создаем кнопку для начала игры
        self.start_button = QPushButton("Start")

        # Устанавливаем размер кнопки
        self.start_button.setFixedSize(100, 50)

        # Устанавливаем шрифт кнопки
        self.start_button.setFont(QFont("Arial", 16))

        # Добавляем кнопку в горизонтальный компоновщик
        self.control_layout.addWidget(self.start_button)

# Продолжение кода для модуля gui.py

        # Связываем событие нажатия на кнопку с методом начала игры
        self.start_button.clicked.connect(self.start_game)

        # Создаем кнопку для выхода из игры
        self.exit_button = QPushButton("Exit")

        # Устанавливаем размер кнопки
        self.exit_button.setFixedSize(100, 50)

        # Устанавливаем шрифт кнопки
        self.exit_button.setFont(QFont("Arial", 16))

        # Добавляем кнопку в горизонтальный компоновщик
        self.control_layout.addWidget(self.exit_button)

        # Связываем событие нажатия на кнопку с методом выхода из игры
        self.exit_button.clicked.connect(self.exit_game)

    # Создаем метод для подключения к серверу
    def connect_server(self):
        # Получаем IP-адрес и порт сервера от пользователя
        address, ok = QInputDialog.getText(self, "Connect to server", "Enter IP address and port of the server (e.g. 127.0.0.1:8000)")

        # Проверяем, что пользователь ввел адрес и нажал OK
        if ok and address:
            # Разделяем адрес на IP-адрес и порт
            ip, port = address.split(":")

            # Преобразуем порт в целое число
            port = int(port)

            # Вызываем метод класса Game для подключения к серверу с указанным IP-адресом и портом
            self.game.connect_server(ip, port)

    # Создаем метод для начала игры
    def start_game(self):
        # Вызываем метод класса Game для начала игры
        self.game.start_game()

    # Создаем метод для выхода из игры
    def exit_game(self):
        # Вызываем метод класса Game для выхода из игры
        self.game.exit_game()

