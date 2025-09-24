from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
import sys
import random

class GuardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ο Φρουρός του Κάστρου")
        self.setMinimumSize(400, 400)


        layout = QVBoxLayout()


        self.guard_label = QLabel()
        pixmap = QPixmap("characters/guard/guard.png")
        if not pixmap.isNull():
            self.guard_label.setPixmap(pixmap.scaledToWidth(200))
            self.guard_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.guard_label)


        self.story_button = QPushButton("Διάβασε την ιστορία μου")
        self.story_button.clicked.connect(self.tell_story)
        layout.addWidget(self.story_button)


        self.audio_button = QPushButton("Άκουσε τη φωνή μου")
        self.audio_button.clicked.connect(self.play_audio)
        layout.addWidget(self.audio_button)


        self.story_label = QLabel("")
        self.story_label.setWordWrap(True)
        layout.addWidget(self.story_label)


        activity_layout = QHBoxLayout()
        self.helmet_button = QPushButton("Κράνος")
        self.sword_button = QPushButton("Σπαθί")
        self.shield_button = QPushButton("Ασπίδα")

        self.helmet_button.clicked.connect(lambda: self.select_item("Κράνος"))
        self.sword_button.clicked.connect(lambda: self.select_item("Σπαθί"))
        self.shield_button.clicked.connect(lambda: self.select_item("Ασπίδα"))

        activity_layout.addWidget(self.helmet_button)
        activity_layout.addWidget(self.sword_button)
        activity_layout.addWidget(self.shield_button)

        layout.addLayout(activity_layout)


        self.activity_label = QLabel("Επίλεξε τον εξοπλισμό μου!")
        layout.addWidget(self.activity_label)

        self.setLayout(layout)


        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self._here = Path(__file__).resolve().parent

        self.audio_files = [
            self._here / "guard_voice1.mp3",
            self._here / "guard_voice2.mp3",
        ]


    def tell_story(self):
        story = (
            "Είμαι ο φρουρός του κάστρου. Κάθε νύχτα περιπολώ το οχυρό "
            "για να προστατεύσω τον διοικητή και τον λαό. "
            "Με την πανοπλία μου και την πίστη μου, είμαι έτοιμος να "
            "αποκρούσω κάθε εισβολέα."
        )
        self.story_label.setText(story)

    def play_audio(self):
        try:
            self.player.stop()
        except Exception:
            pass

        audio_path = random.choice(self.audio_files)

        if not audio_path.exists():
            print(f"[GuardWindow] Δεν βρέθηκε: {audio_path}")
            return

        self.player.setSource(QUrl.fromLocalFile(str(audio_path)))


        try:
            self.audio_output.setVolume(0.8)
        except Exception:
            pass

        self.player.play()

    def select_item(self, item):
        self.activity_label.setText(f"Μου έδωσες: {item}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GuardWindow()
    window.show()
    sys.exit(app.exec())
