from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QWidget, \
    QLabel, \
    QDialog, QFrame, QGridLayout, QScrollArea
from PySide6.QtCore import QSize, Signal, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel
# audio imports
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
import os

# Info window for displaying information about locations
class InfoWindow(QDialog):
    def __init__(self, title, info_text, bg_image=None):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(350, 350, 400, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)

        if bg_image:
            self.bg_label = QLabel(self)
            pixmap = QPixmap(bg_image)
            self.bg_label.setPixmap(pixmap)
            self.bg_label.setScaledContents(True)
            self.bg_label.lower()

        label = QLabel(info_text, self)
        label.setWordWrap(True)
        label.setStyleSheet("color: white;")
        layout.addWidget(label)

        back_button = QPushButton("Πίσω στον χάρτη")
        back_button.clicked.connect(self.close)
        layout.addWidget(back_button)

    def resizeEvent(self, event):
        if hasattr(self, "bg_label"):
            self.bg_label.resize(self.size())
        super().resizeEvent(event)

class SecondWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.setWindowTitle("Καστροπολιτεία")
        self.setMinimumSize(QSize(400, 300))
        self.setGeometry(250, 250, 1000, 600)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # Background walls
        self.bg_label = QLabel(centralWidget)
        self.bg_label.setPixmap(QPixmap("images/castle_walls.jpg"))
        self.bg_label.setScaledContents(True)
        self.bg_label.setGeometry(0, 0, 1000, 600)
        self.bg_label.lower()

        self.back_button = QPushButton("← Πίσω", centralWidget)
        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(50, 50, 50, 180);
                color: white;
                font-weight: bold;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: rgba(70, 70, 70, 200);
            }
        """)
        self.back_button.move(20, 20)
        self.back_button.clicked.connect(self.go_back)
        self.back_button.raise_()

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        # for background music (map.mp3)
        self.bg_player = QMediaPlayer()
        self.bg_audio_output = QAudioOutput()
        self.bg_player.setAudioOutput(self.bg_audio_output)

        # Map
        map_label = QLabel(centralWidget)
        map_pixmap = QPixmap("images/map.png")
        map_label.setPixmap(map_pixmap)
        map_label.setScaledContents(True)
        map_label.setFixedSize(800, 400)
        map_label.move((self.width() - map_label.width()) // 2, 100)

        # Castle Button
        castle_button = QPushButton("Κάστρο", map_label)
        castle_button.setGeometry(130, 75, 80, 80)
        castle_button.setFixedSize(70, 70)
        castle_button.setStyleSheet("""
            QPushButton {
                border-radius: 40px;  
                background-color: brown; 
                color: white;
                font-weight: bold;
                border: 2px solid #2980b9;
            }
            QPushButton:hover {
                background-color: red;
            }
        """)
        castle_button.clicked.connect(self.show_castle_info)

        # Square Button
        square_button = QPushButton("Πλατεία", map_label)
        button_size = 70
        square_button.setFixedSize(button_size, button_size)
        map_width = map_label.width()
        map_height = map_label.height()
        offset = 25
        square_button.move(
            (map_width - button_size) // 2 - offset,
            (map_height - button_size) // 2
        )

        square_button.setStyleSheet(f"""
            QPushButton {{
                border-radius: {button_size // 2}px;  
                background-color: green; 
                color: white;
                font-weight: bold;
                border: 2px solid #2980b9;
            }}
            QPushButton:hover {{
                background-color: limegreen;
            }}
        """)
        square_button.clicked.connect(self.square)

    # Castle functions
    def show_castle_info(self):
        self.stop_background()
        self.play_sound("castle.mp3")
        title = "Πληροφορίες Κάστρου"
        info_text = " Εδώ βρίσκεται το κάστρο που ζει ο βασιλιάς. Το κάστρο περιβάλλεται από ψηλά τείχη και έχει μια μεγάλη αυλή στο κέντρο. Στο εσωτερικό, υπάρχουν πολλά δωμάτια όπως η αίθουσα του θρόνου, η τραπεζαρία και οι χώροι διαμονής για τη βασιλική οικογένεια."
        info_window = InfoWindow(title, info_text, "images/corridor.jpg")
        info_window.finished.connect(self.stop_sound)
        info_window.finished.connect(self.play_background)
        info_window.exec()

    def show_square_info(self, current, previous):
        if not current:
            return
        text = current.text()
        if "Παζάρι" in text:
            self.info_label.setText("Ένα παραμύθι για το παζάρι...")
            self.play_sound("bazaar.mp3")
        elif "Πανηγύρι" in text:
            self.info_label.setText("Το μεγάλο πανηγύρι με μουσική και χορό!")
            self.play_sound("festival.mp3")
        elif "Χορωδία" in text:
            self.info_label.setText("Η χορωδία τραγουδά παραδοσιακά τραγούδια.")
            self.play_sound("choir.mp3")

    def square(self):
        self.stop_background()
        info_window = QDialog()
        info_window.setWindowTitle("Καλωσήρθατε στην κεντρική πλατεία!")
        info_window.resize(800, 600)

        main_layout = QVBoxLayout()  # Κύριο κάθετο layout

        # Εικόνα πάνω
        image_label = QLabel()
        pixmap = QPixmap("images/square.jpg")
        pixmap = pixmap.scaled(1000, 700, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(image_label)

        bottom_layout = QHBoxLayout()

        list_widget = QListWidget()
        list_widget.addItems(["Παζάρι", "Πανηγύρι", "Χορωδία"])
        bottom_layout.addWidget(list_widget)
        self.info_label = QLabel("Διάλεξε μια δραστηριότητα")
        self.info_label.setWordWrap(True)
        bottom_layout.addWidget(self.info_label)

        main_layout.addLayout(bottom_layout)
        back_button = QPushButton("Πίσω στον χάρτη")
        back_button.clicked.connect(info_window.close)
        main_layout.addWidget(back_button)

        info_window.setLayout(main_layout)

        list_widget.currentItemChanged.connect(self.show_square_info)

        info_window.finished.connect(self.stop_sound)
        info_window.finished.connect(self.play_background)

        info_window.exec()

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

    def resizeEvent(self, event):
        self.bg_label.resize(self.size())
        self.back_button.raise_()
        super().resizeEvent(event)

    def play_background(self):
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "sounds", "map.mp3")
        url = QUrl.fromLocalFile(file_path)
        self.bg_player.setSource(url)
        self.bg_player.play()
        self.bg_player.setLoops(QMediaPlayer.Infinite)

    def stop_background(self):
        if self.bg_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.bg_player.stop()

    def go_back(self):
        self.stop_sound()
        self.stop_background()
        self.hide()
        self.main_window.show()

    def showEvent(self, event):
        super().showEvent(event)
        self.play_background()

    def closeEvent(self, event):
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.stop()
        event.accept()