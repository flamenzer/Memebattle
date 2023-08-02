# main.py
# Импортируем необходимые библиотеки
import sys
from PyQt5.QtWidgets import QApplication
from gui import GUI
from game import Game

# Создаем экземпляр приложения
app = QApplication(sys.argv)

# Создаем экземпляр класса GUI
gui = GUI()

# Создаем экземпляр класса Game
game = Game(gui)

# Передаем экземпляр класса Game в класс GUI
gui.set_game(game)

# Показываем главное окно приложения
gui.show()

# Запускаем цикл обработки событий приложения
sys.exit(app.exec_())
