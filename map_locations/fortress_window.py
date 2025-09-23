from PySide6.QtWidgets import QPushButton
from helper_functions.info_window import InfoWindow
from helper_functions.collection_button import create_collection_button

def show_fortress(map_window):
    map_window.stop_background()
    map_window.play_sound("fortress.mp3")

    collection_title = "Η άμυνα της καστροπολιτείας, το Οχυρό"
    title = "Βρισκόμαστε στο οχυρό!"
    info_text = (
        '<span style="font-weight: bold; color: white;">'
        'Το οχυρό είναι η κύρια αμυντική δομή της καστροπολιτείας μας, χτισμένο για να προστατεύει τους κατοίκους και τον βασιλιά. Στο εσωτερικό του οχυρού βρίσκονται οι φρουροί, ενώ υπάρχει η αίθουσα στρατηγικής και η αίθουσα του εξοπλισμού των πολεμιστών.'
        '</span>'
    )

    info_window = InfoWindow(title, info_text, "images/fortress.jpg")
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