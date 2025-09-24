from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
import sys


class CookWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ο Μάγειρας της Καστροπολιτείας")
        self.setMinimumSize(400, 400)

        # layout
        layout = QVBoxLayout()

        # Εικόνα 
        self.cook_label = QLabel()
        pixmap = QPixmap("chef.png") 
        if not pixmap.isNull():
            self.cook_label.setPixmap(pixmap.scaledToWidth(200))
            self.cook_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.cook_label)

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

        # Κατσαρόλα
        self.pot_button = QPushButton("Κατσαρόλα")
        self.pot_button.clicked.connect(self.show_food)
        layout.addWidget(self.pot_button)

        # φαγητό που μαγειρεύεται
        self.food_label = QLabel("Η κατσαρόλα είναι άδεια...")
        layout.addWidget(self.food_label)

        self.setLayout(layout)

        # MediaPlayer για ήχο
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

    def tell_story(self):
        story = (
            "Είμαι ο μάγειρας της καστροπολιτείας εδώ και τριάντα χρόνια. "
            "Μαγειρεύω καθημερινά για τον βασιλιά, τους φρουρούς και τους ανθρώπους του κάστρου. "
            "Στην κουζίνα μου συνδυάζω βότανα, κρέας και δημητριακά, "
            "για να γεμίσω το τραπέζι με μυρωδιές και γεύσεις."
        )
        self.story_label.setText(story)

    def play_audio(self):
       # αρχείο ήχου
        url = QUrl.fromLocalFile("chef_voice.mp3")
        self.player.setSource(url)
        self.player.play()

    def show_food(self):
        self.food_label.setText("Στην κατσαρόλα βράζει μια ζεστή σούπα με φακές και μυρωδικά!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CookWindow()
    window.show()
    sys.exit(app.exec())
