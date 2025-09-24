from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
import sys


class ArcherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Η Τοξότρια του Κάστρου")
        self.setMinimumSize(400, 400)

        # layout
        layout = QVBoxLayout()

        # Εικόνα 
        self.archer_label = QLabel()
        pixmap = QPixmap("archer.png")  
        if not pixmap.isNull():
            self.archer_label.setPixmap(pixmap.scaledToWidth(200))
            self.archer_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.archer_label)

        # αφήγηση
        self.story_button = QPushButton("Διάβασε την ιστορία μου")
        self.story_button.clicked.connect(self.tell_story)
        layout.addWidget(self.story_button)

        # αναπαραγωγή ήχου
        self.audio_button = QPushButton("Άκουσε τη φωνή μου")
        self.audio_button.clicked.connect(self.play_audio)
        layout.addWidget(self.audio_button)

        # Label αφήγησης
        self.story_label = QLabel("")
        self.story_label.setWordWrap(True)
        layout.addWidget(self.story_label)

        # τόξο
        self.bow_button = QPushButton("Τόξο")
        self.bow_button.clicked.connect(self.show_bow_action)
        layout.addWidget(self.bow_button)

        # Label για το feedback του τόξου
        self.bow_label = QLabel("Το τόξο είναι έτοιμο...")
        layout.addWidget(self.bow_label)

        self.setLayout(layout)

        # MediaPlayer για ήχο
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

    def tell_story(self):
        story = (
            "Είμαι η τοξότρια του κάστρου. Εδώ και δεκαπέντε χρόνια "
            "υπηρετώ πιστά τον βασιλιά, φυλάγοντας τα τείχη μέρα και νύχτα. "
            "Με το τόξο και τα βέλη μου, προστατεύω τον λαό από κάθε απειλή."
        )
        self.story_label.setText(story)

    def play_audio(self):
        # αρχείο ήχου
        url = QUrl.fromLocalFile("archer_voice.mp3")
        self.player.setSource(url)
        self.player.play()

    def show_bow_action(self):
        self.bow_label.setText("Η τοξότρια σηκώνει το τόξο της και στοχεύει τον ορίζοντα!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArcherWindow()
    window.show()
    sys.exit(app.exec())
