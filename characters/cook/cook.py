from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
import sys
import os

class CookWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ο Μάγειρας της Καστροπολιτείας")
        self.setMinimumSize(400, 400)


        layout = QVBoxLayout()


        self.cook_label = QLabel()
        pixmap = QPixmap("characters/cook/cook.png")
        if not pixmap.isNull():
            self.cook_label.setPixmap(pixmap.scaledToWidth(200))
            self.cook_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.cook_label)


        self.story_button = QPushButton("Διάβασε την ιστορία μου")
        self.story_button.clicked.connect(self.tell_story)
        layout.addWidget(self.story_button)


        self.audio_button = QPushButton("Άκουσε τη φωνή μου")
        self.audio_button.clicked.connect(self.play_audio)
        layout.addWidget(self.audio_button)


        self.story_label = QLabel("")
        self.story_label.setWordWrap(True)
        layout.addWidget(self.story_label)


        self.pot_button = QPushButton("Κατσαρόλα")
        self.pot_button.clicked.connect(self.show_food)
        layout.addWidget(self.pot_button)


        self.food_label = QLabel("Η κατσαρόλα είναι άδεια...")
        layout.addWidget(self.food_label)

        self.setLayout(layout)


        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(1.0)

    def tell_story(self):
        story = (
            "Είμαι ο μάγειρας της καστροπολιτείας εδώ και τριάντα χρόνια. "
            "Μαγειρεύω καθημερινά για τον βασιλιά, τους φρουρούς και τους ανθρώπους του κάστρου. "
            "Στην κουζίνα μου συνδυάζω βότανα, κρέας και δημητριακά, "
            "για να γεμίσω το τραπέζι με μυρωδιές και γεύσεις."
        )
        self.story_label.setText(story)

    def play_audio(self):
        base = os.path.dirname(__file__)
        audio_path = os.path.join(base,"cook_voice.mp3")
        url = QUrl.fromLocalFile(os.path.abspath(audio_path))
        self.player.setSource(url)
        self.player.play()

    def show_food(self):
        self.food_label.setText("Στην κατσαρόλα βράζει μια ζεστή σούπα με φακές και μυρωδικά!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CookWindow()
    window.show()
    sys.exit(app.exec())
