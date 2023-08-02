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

