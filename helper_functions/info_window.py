from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QScrollArea, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class InfoWindow(QDialog):
    def __init__(self, title, info_text, bg_image=None, width=800, height=600, scrollable=False):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(300, 300, width, height)
        self.setMinimumSize(width, height)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        if bg_image:
            self.bg_label = QLabel(self)
            pixmap = QPixmap(bg_image)
            self.bg_label.setPixmap(pixmap)
            self.bg_label.setScaledContents(True)
            self.bg_label.lower()

        if scrollable:
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            content_widget = QWidget()
            self.content_layout = QVBoxLayout(content_widget)
            scroll_area.setWidget(content_widget)
            main_layout.addWidget(scroll_area)
        else:
            self.content_layout = main_layout

        info_label = QLabel(info_text)
        info_label.setWordWrap(True)
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info_label.setStyleSheet("color: white;")
        self.content_layout.addWidget(info_label)

    def resizeEvent(self, event):
        if hasattr(self, "bg_label"):
            self.bg_label.resize(self.size())
        super().resizeEvent(event)