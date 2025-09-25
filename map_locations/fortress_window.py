from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QHBoxLayout
from helper_functions.info_window import InfoWindow
from helper_functions.collection_button import create_collection_button

from characters.guard.guard import GuardWindow

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

    guard_button = QPushButton("Φρουρός")
    guard_button.setFixedSize(100, 40)  # μικρό μέγεθος
    guard_button.setStyleSheet("""
        QPushButton {
            background-color: #f4e9b8;
            color: #2c2c2c;
            font-weight: bold;
            border-radius: 8px;
        }
        QPushButton:hover {
            background-color: #eadf9f;
        }
    """)


    button_row = QHBoxLayout()
    button_row.addWidget(guard_button, alignment=Qt.AlignLeft)

    info_window.content_layout.addLayout(button_row)

    info_window.content_layout.addWidget(guard_button)


    def open_guard():

        try:
            map_window.stop_sound()
        except Exception:
            pass


        info_window.guard_window = GuardWindow()
        info_window.guard_window.setAttribute(Qt.WA_DeleteOnClose, True)
        info_window.guard_window.setWindowModality(Qt.ApplicationModal)

        info_window.guard_window.destroyed.connect(lambda: map_window.play_sound("fortress.mp3"))
        info_window.guard_window.show()

    guard_button.clicked.connect(open_guard)


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
    help_button = QPushButton("Help")
    help_button.setFixedSize(60, 27)
    help_button.setStyleSheet("""
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
    help_button.clicked.connect(lambda: show_walls_help(info_window))
    top_layout = QHBoxLayout()
    top_layout.addStretch()       
    top_layout.addWidget(help_button)
    info_window.content_layout.insertLayout(0, top_layout)  
    info_window.exec()
    

   
   

def show_walls_help(window):
    from PySide6.QtWidgets import QMessageBox
    QMessageBox.information(
            window,
            "Βοήθεια – Οχυρό Κάστρου",
            "Σε αυτή την οθόνη μπορείτε να δείτε το οχυρό της καστροπολιτείας.\n\n"
            "- Πατήστε 'Φρουρός' για να δείτε περισσότερα για τον φρουρό.\n"
            "- Πατήστε 'Πίσω στον χάρτη' για να επιστρέψετε στον χάρτη.\n"
            "- Πατήστε 'Προσθήκη' ώστε να συλλέξετε πληροφορίες για το κάστρο."
        )