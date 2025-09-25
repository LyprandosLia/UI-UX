from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
import sys
import os
from helper_functions.collection_button import create_collection_button

class ScarecrowWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Το Σκιάχτρο του Κάστρου")
        self.setMinimumSize(400, 400)

        layout = QVBoxLayout()

        self.scarecrow_label = QLabel()
        pixmap = QPixmap("characters/scarecrow/scarecrow.png")
        if not pixmap.isNull():
            self.scarecrow_label.setPixmap(pixmap.scaledToWidth(200))
            self.scarecrow_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.scarecrow_label)

        self.story_button = QPushButton("Διάβασε την ιστορία μου")
        self.story_button.clicked.connect(self.tell_story)
        layout.addWidget(self.story_button)

        self.story_label = QLabel("")
        self.story_label.setWordWrap(True)
        layout.addWidget(self.story_label)

        self.audio_button = QPushButton("Μίλησέ μου")
        self.audio_button.clicked.connect(self.play_audio)
        layout.addWidget(self.audio_button)

        self.setLayout(layout)

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

    def tell_story(self):
        self.story = (
            "Είμαι το σκιάχτρο. "
            "Βρίσκομαι σε αυτό το κάστρο πολύ πριν τον βασιλιά..."
        )
        self.story_label.setText(self.story)

        if not hasattr(self, 'collect_button'):
            self.collect_button = create_collection_button(self, "Το Σκιάχτρο του Κάστρου", self.story)
            h_layout = QHBoxLayout()
            h_layout.addStretch()
            h_layout.addWidget(self.collect_button)
            self.layout().addLayout(h_layout)

    def play_audio(self):
        base = os.path.dirname(__file__)
        audio_path = os.path.join(base,"scarecrow_voice.mp3")
        url = QUrl.fromLocalFile(os.path.abspath(audio_path))
        self.player.setSource(url)
        self.player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScarecrowWindow()
    window.show()
    sys.exit(app.exec())
