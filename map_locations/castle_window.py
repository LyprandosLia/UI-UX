from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QVBoxLayout
from helper_functions.info_window import InfoWindow
from helper_functions.collection_button import create_collection_button

from characters.cook.cook import CookWindow
from characters.king.king import KingWindow


def show_castle(map_window):
    map_window.stop_background()
    map_window.play_sound("castle.mp3")

    collection_title = "Το Βασιλικό Κάστρο"
    title = "Πληροφορίες Κάστρου"
    info_text = (
        '<span style="font-weight: bold; color: white;">'
        'Εδώ βρίσκεται το κάστρο που ζει ο βασιλιάς. Το κάστρο περιβάλλεται από ψηλά τείχη και έχει μια μεγάλη αυλή στο κέντρο. Στο εσωτερικό, υπάρχουν πολλά δωμάτια όπως η αίθουσα του θρόνου, η τραπεζαρία και οι χώροι διαμονής για τη βασιλική οικογένεια.'
        '</span>'
    )

    info_window = InfoWindow(title, info_text, "images/corridor.jpg")
    create_collection_button(info_window, collection_title, info_text)

    cook_button = QPushButton("Μάγειρας")
    cook_button.setFixedSize(100, 40)

    king_button = QPushButton("Βασιλιάς")
    king_button.setFixedSize(100, 40)  # μικρό μέγεθος

    common_btn_css = """
    QPushButton {
        background-color: #f4e9b8;
        color: #2c2c2c;
        font-weight: bold;
        border-radius: 8px;
        padding: 6px 12px;
    }
    QPushButton:hover { background-color: #eadf9f; }
    """

    cook_button.setStyleSheet(common_btn_css)
    king_button.setStyleSheet(common_btn_css)

    buttons_col = QVBoxLayout()
    buttons_col.setSpacing(8)
    buttons_col.addWidget(cook_button, alignment=Qt.AlignLeft)  # ο Μάγειρας πάνω
    buttons_col.addWidget(king_button, alignment=Qt.AlignLeft)
    info_window.content_layout.addLayout(buttons_col)


    def open_cook():

        try:
            map_window.stop_sound()
        except Exception:
            pass

        info_window.cook_window = CookWindow()
        info_window.cook_window.setAttribute(Qt.WA_DeleteOnClose, True)
        info_window.cook_window.setWindowModality(Qt.ApplicationModal)
        # Αν το CookWindow είναι QWidget, αφήνουμε show() (modal δεν έχει νόημα)
        info_window.cook_window.destroyed.connect(lambda: map_window.play_sound("castle.mp3"))
        info_window.cook_window.show()



    def open_king():

        try:
            map_window.stop_sound()
        except Exception:
            pass


        info_window.king_window = KingWindow()
        info_window.king_window.setAttribute(Qt.WA_DeleteOnClose, True)
        info_window.king_window.setWindowModality(Qt.ApplicationModal)

        info_window.king_window.destroyed.connect(lambda: map_window.play_sound("castle.mp3"))
        info_window.king_window.show()

    cook_button.clicked.connect(open_cook)
    king_button.clicked.connect(open_king)

    back_button = QPushButton("Πίσω στον χάρτη")
    back_button.setStyleSheet("""
           QPushButton {
               background-color: lightblue;
               color: black;
               font-weight: bold;
               border-radius: 8px;
               padding: 6px 12px;
           }
           QPushButton:hover {
               background-color: #87CEFA;
           }
       """)
    back_button.clicked.connect(info_window.close)
    info_window.content_layout.addWidget(back_button)

    info_window.finished.connect(map_window.stop_sound)
    info_window.finished.connect(map_window.play_background)
    info_window.exec()