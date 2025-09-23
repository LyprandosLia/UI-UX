from PySide6.QtWidgets import QPushButton
from helper_functions.info_window import InfoWindow
from helper_functions.collection_button import create_collection_button

def show_castle(map_window):
    map_window.stop_background()
    map_window.play_sound("castle.mp3")

    collection_title = "Κάστρο Γενικές Πληροφορίες:"
    title = "Πληροφορίες Κάστρου"
    info_text = (
        '<span style="font-weight: bold; color: white;">'
        'Εδώ βρίσκεται το κάστρο που ζει ο βασιλιάς. Το κάστρο περιβάλλεται από ψηλά τείχη και έχει μια μεγάλη αυλή στο κέντρο. Στο εσωτερικό, υπάρχουν πολλά δωμάτια όπως η αίθουσα του θρόνου, η τραπεζαρία και οι χώροι διαμονής για τη βασιλική οικογένεια.'
        '</span>'
    )

    info_window = InfoWindow(title, info_text, "images/corridor.jpg")
    create_collection_button(info_window, collection_title, info_text)
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