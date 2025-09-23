from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel
import sys
# audio imports
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QUrl
import os

from shop_window import ShopWindow
from map_window import MapWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Αρχική Σελίδα")
        self.setMinimumSize(QSize(400, 300))
        self.setGeometry(200, 200, 1000, 600)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # Background
        self.bg_label = QLabel(centralWidget)
        self.bg_label.setPixmap(QPixmap("images/castle.jpg"))
        self.bg_label.setScaledContents(True)
        self.bg_label.setGeometry(0, 0, self.width(), self.height())

        # Buttons
        self.shop_button = QPushButton("Κατάστημα Αναμνηστικών", centralWidget)
        self.shop_button.setFixedSize(250, 40)
        self.shop_button.setStyleSheet("""
            background-color: rgba(0, 0, 0, 200);
            color: white;
            font-weight: bold;
            border-radius: 5px;
        """)
        self.shop_button.clicked.connect(self.open_shop)

        self.enter_button = QPushButton("Είσοδος στην Καστροπολιτεία", centralWidget)
        self.enter_button.setFixedSize(250, 40)
        self.enter_button.setStyleSheet("""
            background-color: rgba(255, 0, 0, 200);
            color: white;
            font-weight: bold;
            border-radius: 5px;
        """)
        self.enter_button.clicked.connect(self.open_second_window)

        self.update_button_positions()
        

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        self.second_window = MapWindow(self)

    def play_sound(self, filename, loop=False):
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "sounds", filename)
        url = QUrl.fromLocalFile(file_path)
        self.player.setSource(url)
        self.player.play()
        if loop:
            self.player.setLoops(QMediaPlayer.Infinite)

    def stop_sound(self):
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.stop()

    def update_button_positions(self):
        margin = 20
        spacing = 10
        self.enter_button.move(
            (self.width() - self.enter_button.width()) // 2,
            self.height() - self.enter_button.height() - margin
        )
        self.shop_button.move(
            (self.width() - self.shop_button.width()) // 2,
            self.height() - self.enter_button.height() - self.shop_button.height() - margin - spacing
        )

    def on_resize(self, event):
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        self.update_button_positions()

    def open_second_window(self):
        self.stop_sound()
        self.second_window.show()
        self.hide()

    def open_shop(self):
        self.stop_sound()
        shop = ShopWindow()
        shop.exec()
        self.play_sound("entrance.mp3", loop=True)

    def showEvent(self, event):
        super().showEvent(event)
        self.play_sound("entrance.mp3", loop=True)

    def closeEvent(self, event):
        self.stop_sound()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
