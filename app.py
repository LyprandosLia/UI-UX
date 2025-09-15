from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, \
    QDialog, QFrame, QGridLayout, QScrollArea
from PySide6.QtCore import QSize, Signal, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel
import sys

from shop_window import ShopWindow

# Info Window for displaying information about locations
class InfoWindow(QDialog):
    def __init__(self, title, info_text, bg_image=None):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(350, 350, 400, 300)
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
        label.setStyleSheet("color: white;")
        layout.addWidget(label)

        back_button = QPushButton("Πίσω στον χάρτη")
        back_button.clicked.connect(self.close)
        layout.addWidget(back_button)

    def resizeEvent(self, event):
        if hasattr(self, "bg_label"):
            self.bg_label.resize(self.size())
        super().resizeEvent(event)

# Second Window which includes the map
class SecondWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.setWindowTitle("Καστροπολιτεία")
        self.setMinimumSize(QSize(400, 300))
        self.setGeometry(250, 250, 1000, 600)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # Background walls
        self.bg_label = QLabel(centralWidget)
        self.bg_label.setPixmap(QPixmap("images/castle_walls.jpg"))
        self.bg_label.setScaledContents(True)
        self.bg_label.setGeometry(0, 0, 1000, 600)
        self.bg_label.lower()

        self.back_button = QPushButton("← Πίσω", centralWidget)
        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(50, 50, 50, 180);
                color: white;
                font-weight: bold;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: rgba(70, 70, 70, 200);
            }
        """)
        self.back_button.move(20, 20)
        self.back_button.clicked.connect(self.go_back)
        self.back_button.raise_()

        # Map
        map_label = QLabel(centralWidget)
        map_pixmap = QPixmap("images/map.png")
        map_label.setPixmap(map_pixmap)
        map_label.setScaledContents(True)
        map_label.setFixedSize(800, 400)
        map_label.move((self.width() - map_label.width())//2, 100)

        # Castle Button
        castle_button = QPushButton("Κάστρο", map_label)
        castle_button.setGeometry(120, 70, 80, 80)
        castle_button.setFixedSize(80, 80)
        castle_button.setStyleSheet("""
            QPushButton {
                border-radius: 40px;  
                background-color: brown; 
                color: white;
                font-weight: bold;
                border: 2px solid #2980b9;
            }
            QPushButton:hover {
                background-color: red;
            }
        """)
        castle_button.clicked.connect(self.show_castle_info)

    def resizeEvent(self, event):
        self.bg_label.resize(self.size())
        self.back_button.raise_()
        super().resizeEvent(event)

    def go_back(self):
        self.hide()
        self.main_window.show()

    def show_castle_info(self):
        title = "About the castle"
        info_text = " Εδώ βρίσκεται το κάστρο που ζει ο βασιλιάς. Το κάστρο περιβάλλεται από ψηλά τείχη και έχει μια μεγάλη αυλή στο κέντρο. Στο εσωτερικό, υπάρχουν πολλά δωμάτια όπως η αίθουσα του θρόνου, η τραπεζαρία και οι χώροι διαμονής για τη βασιλική οικογένεια."
        info_window = InfoWindow(title, info_text, "images/corridor.jpg")
        info_window.exec()


# First Window which is the Welcome to the Castle City
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Αρχική Σελίδα")
        self.setMinimumSize(QSize(400, 300))
        self.setGeometry(200, 200, 1000, 600)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.bg_label = QLabel(centralWidget)
        self.bg_label.setPixmap(QPixmap("images/castle.jpg"))
        self.bg_label.setScaledContents(True)
        self.bg_label.setGeometry(0, 0, self.width(), self.height())

        self.shop_button = QPushButton("Κατάστημα Αναμνηστικών", centralWidget)
        self.shop_button.setFixedSize(250, 40)
        self.shop_button.setStyleSheet("""
            background-color: rgba(0, 0, 0, 160);
            color: white;
            font-weight: bold;
            border-radius: 5px;
        """)
        self.shop_button.clicked.connect(self.open_shop)

        self.enter_button = QPushButton("Είσοδος στην Καστροπολιτεία", centralWidget)
        self.enter_button.setFixedSize(250, 40)
        self.enter_button.setStyleSheet("""
            background-color: rgba(0, 0, 0, 160);
            color: white;
            font-weight: bold;
            border-radius: 5px;
        """)
        self.enter_button.clicked.connect(self.open_second_window)

        self.update_button_positions()
        self.resizeEvent = self.on_resize

        self.second_window = SecondWindow(self)

    def update_button_positions(self):
        margin = 20
        spacing = 10
        self.enter_button.move(
            (self.width() - self.enter_button.width()) // 2,
            self.height() - self.enter_button.height() - margin
        )
        self.shop_button.move(
            (self.width() - self.shop_button.width()) // 2,
            self.height() - self.enter_button.height() - self.shop_button.height() - margin - spacing
        )

    def on_resize(self, event):
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        self.update_button_positions()

    def open_second_window(self):
        self.second_window.show()
        self.hide()

    def open_shop(self):
        shop = ShopWindow()
        shop.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
