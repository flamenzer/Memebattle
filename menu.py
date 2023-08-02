from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QFont, QPainter, QBrush, QColor, QPen
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Биржа мемов")
        self.setWindowState(Qt.WindowFullScreen)  # Open the menu in fullscreen
        
        # Set the background image for the main window
        background_image = QLabel(self)
        pixmap = QPixmap("meme1.jpg")  # Replace "cyberpunk_background.jpg" with the path to your image
        background_image.setPixmap(pixmap)
        background_image.setGeometry(0, 0, self.width(), self.height())
        background_image.setScaledContents(True)
        
        # Create the buttons for "Играть", "Настройки", and "Выход"
        play_button = QPushButton("Играть", self)
        settings_button = QPushButton("Настройки", self)
        exit_button = QPushButton("Выход", self)
        
        # Set the font and style for the buttons
        font = QFont("Arial", 20)
        play_button.setFont(font)
        settings_button.setFont(font)
        exit_button.setFont(font)
        play_button.setStyleSheet("background-color: #00ff00; color: #000000; border: 2px solid #000000;")
        settings_button.setStyleSheet("background-color: #00ff00; color: #000000; border: 2px solid #000000;")
        exit_button.setStyleSheet("background-color: #00ff00; color: #000000; border: 2px solid #000000;")
        
        # Set the positions and sizes of the buttons
        button_width = 200
        button_height = 50
        x = int((self.width() - button_width) / 2)
        y = int((self.height() - button_height * 3 - 20) / 2)
        play_button.setGeometry(x, y, button_width, button_height)
        settings_button.setGeometry(x, y + button_height + 10, button_width, button_height)
        exit_button.setGeometry(x, y + button_height * 2 + 20, button_width, button_height)
        
        # Connect the buttons to their respective functions
        play_button.clicked.connect(self.play_game)
        settings_button.clicked.connect(self.open_settings)
        exit_button.clicked.connect(self.close)
        # Set the hover effect for the buttons
        play_button.setStyleSheet("QPushButton:hover {background-color: #008000;}")
        settings_button.setStyleSheet("QPushButton:hover {background-color: #008000;}")
        exit_button.setStyleSheet("QPushButton:hover {background-color: #008000;}")
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        painter.drawRect(self.rect())
        
    def play_game(self):
        # Implement the logic for starting the game here
        pass

    def open_settings(self):
        # Implement the logic for opening the settings here
        pass

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
