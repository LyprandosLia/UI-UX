from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
import sys


class ScarecrowWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Το Σκιάχτρο του Κάστρου")
        self.setMinimumSize(400, 400)

        # layout
        layout = QVBoxLayout()

        # Εικόνα
        self.scarecrow_label = QLabel()
        pixmap = QPixmap("scarecrow.png")  
        if not pixmap.isNull():
            self.scarecrow_label.setPixmap(pixmap.scaledToWidth(200))
            self.scarecrow_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.scarecrow_label)

        # Κουμπί αφήγησης
        self.story_button = QPushButton("Διάβασε την ιστορία μου")
        self.story_button.clicked.connect(self.tell_story)
        layout.addWidget(self.story_button)

        # κείμενο αφήγησης
        self.story_label = QLabel("")
        self.story_label.setWordWrap(True)
        layout.addWidget(self.story_label)

        # αναπαραγωγή φωνής
        self.audio_button = QPushButton("Άκουσε τη φωνή μου")
        self.audio_button.clicked.connect(self.play_audio)
        layout.addWidget(self.audio_button)

        self.setLayout(layout)

        # Media player για ήχο
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

    def tell_story(self):
        story = (
            "Είμαι το σκιάχτρο. "
            "Βρίσκομαι σε αυτό το κάστρο πολύ πριν τον βασιλιά..."
        )
        self.story_label.setText(story)

    def play_audio(self):
        #αρχείο ήχου 
        url = QUrl.fromLocalFile("scarecrow_voice.mp3")
        self.player.setSource(url)
        self.player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScarecrowWindow()
    window.show()
    sys.exit(app.exec())
