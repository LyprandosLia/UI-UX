from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

# Info window for displaying information about locations
class InfoWindow(QDialog):
    def __init__(self, title, info_text, bg_image=None):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(300, 200, 800, 600)
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
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: white;")
        layout.addWidget(label)

        back_button = QPushButton("Πίσω στον χάρτη")
        back_button.clicked.connect(self.close)
        layout.addWidget(back_button)

    def resizeEvent(self, event):
        if hasattr(self, "bg_label"):
            self.bg_label.resize(self.size())
        super().resizeEvent(event)
