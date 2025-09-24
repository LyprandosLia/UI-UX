from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox, QHBoxLayout
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

        # layout
        layout = QVBoxLayout()

        # Εικόνα 
        self.guard_label = QLabel()
        pixmap = QPixmap("guard.png")  # αντικατάστησε με την εικόνα σου
        if not pixmap.isNull():
            self.guard_label.setPixmap(pixmap.scaledToWidth(200))
            self.guard_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.guard_label)

        # αφήγηση
        self.story_button = QPushButton("Διάβασε την ιστορία μου")
        self.story_button.clicked.connect(self.tell_story)
        layout.addWidget(self.story_button)

        # αναπαραγωγή ήχου
        self.audio_button = QPushButton("Άκουσε τη φωνή μου")
        self.audio_button.clicked.connect(self.play_audio)
        layout.addWidget(self.audio_button)

        # κείμενο αφήγησης
        self.story_label = QLabel("")
        self.story_label.setWordWrap(True)
        layout.addWidget(self.story_label)

        # Κράνος, Σπαθί, Ασπίδα
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

        # feedback
        self.activity_label = QLabel("Επίλεξε τον εξοπλισμό μου!")
        layout.addWidget(self.activity_label)

        self.setLayout(layout)

        # αναπαραγωγή ήχου
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

    	 # Λίστα αρχείων ήχου
        self.audio_files = ["guard_voice1.mp3", "guard_voice2.mp3"]

    def tell_story(self):
        story = (
            "Είμαι ο φρουρός του κάστρου. Κάθε νύχτα περιπολώ τα τείχη "
            "για να προστατεύσω τον διοικητή και τον λαό. "
            "Με την πανοπλία μου και την πίστη μου, είμαι έτοιμος να "
            "αποκρούσω κάθε εισβολέα."
        )
        self.story_label.setText(story)

    def play_audio(self):
        # Επιλέγει τυχαίο αρχείο από τη λίστα
        audio_file = random.choice(self.audio_files)
        url = QUrl.fromLocalFile(audio_file)
        self.player.setSource(url)
        self.player.play()

    def select_item(self, item):
        self.activity_label.setText(f"Μου έδωσες: {item}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GuardWindow()
    window.show()
    sys.exit(app.exec())
