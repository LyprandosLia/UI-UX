from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
import sys
import random

class KingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ο Βασιλιάς του Κάστρου")
        self.setMinimumSize(400, 400)

        #layout
        layout = QVBoxLayout()

        # Εικόνα
        self.king_label = QLabel()
        pixmap = QPixmap("king.png")  # αντικατέστησε με εικόνα βασιλιά
        if not pixmap.isNull():
            self.king_label.setPixmap(pixmap.scaledToWidth(200))
            self.king_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.king_label)

        # Κουμπί αφήγησης
        self.story_button = QPushButton("Διάβασε την ιστορία μου")
        self.story_button.clicked.connect(self.tell_story)
        layout.addWidget(self.story_button)

        # Label αφήγησης
        self.story_label = QLabel("")
        self.story_label.setWordWrap(True)
        layout.addWidget(self.story_label)

        # Κουμπί φωνής
        self.audio_button = QPushButton("Άκουσε τη φωνή μου")
        self.audio_button.clicked.connect(self.play_audio)
        layout.addWidget(self.audio_button)

        # Κουμπί για σπαθί
        self.sword_button = QPushButton("Σπαθί")
        self.sword_button.clicked.connect(self.show_sword_action)
        layout.addWidget(self.sword_button)

        # Label feedback για το σπαθί
        self.sword_label = QLabel("Το σπαθί του βασιλιά λάμπει στο φως...")
        layout.addWidget(self.sword_label)

        self.setLayout(layout)

        # Media player για ήχο
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

	  # Λίστα αρχείων ήχου
        self.audio_files = ["king_voice1.mp3", "king_voice2.mp3"]

    def tell_story(self):
        story = (
            "Είμαι ο βασιλιάς αυτού του κάστρου. "
            "Εδώ και τριάντα χρόνια κυβερνώ με δικαιοσύνη και σοφία. "
            "Η σχέση μου με τους φρουρούς, τους μάγειρες, τις τοξότριες "
            "είναι γεμάτη σεβασμό και εμπιστοσύνη."
        )
        self.story_label.setText(story)

    def play_audio(self):
        # Επιλέγει τυχαίο αρχείο από τη λίστα
        audio_file = random.choice(self.audio_files)
        url = QUrl.fromLocalFile(audio_file)
        self.player.setSource(url)
        self.player.play()

    def show_sword_action(self):
        self.sword_label.setText("Ο βασιλιάς σηκώνει το σπαθί του και το υψώνει με περηφάνια!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KingWindow()
    window.show()
    sys.exit(app.exec())
