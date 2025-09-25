from PySide6.QtWidgets import QListWidget, QLabel, QPushButton, QScrollArea, QVBoxLayout, QWidget, QHBoxLayout
from PySide6.QtCore import Qt
from helper_functions.info_window import InfoWindow
from helper_functions.collection_button import create_collection_button

from characters.scarecrow.scarecrow import ScarecrowWindow

def show_footpath(map_window):
    map_window.stop_background()
    map_window.play_sound("footpath.mp3")

    collection_title = "Το Αρχαίο Μονοπάτι των Φρουρών"
    title = "Το μονοπάτι προς το Κάστρο"
    info_text = (
        '<span style="color: #FFFFFF  ; font-weight: bold; font-size:16x;">'
        "Λέγεται πως το μονοπάτι που οδηγεί στο κάστρο δεν είναι απλώς ένας δρόμος. Πάνω σε πέτρες φθαρμένες από τα χρόνια, οι φρουροί του παρελθόντος έχουν αφήσει ψιθύρους και σημάδια που μόνο οι τολμηροί μπορούν να καταλάβουν. Καθώς περπατάς ανάμεσα στα δέντρα και τα πυκνά βάτα, νιώθεις ότι τα βλέμματα των παλιών φρουρών σε συνοδεύουν και ότι κάθε στροφή μπορεί να αποκαλύψει μυστικά κρυμμένα από αιώνες. Το μονοπάτι δεν οδηγεί μόνο στο κάστρο· σε καλεί να ανακαλύψεις τις ιστορίες που οι τοίχοι δεν μπορούν να πουν."
        '</span>'
    )
    info_window = InfoWindow(title, info_text, "images/footpath.jpg")
    create_collection_button(info_window, collection_title, info_text)

    scarecrow_button = QPushButton("Σκιάχτρο")
    scarecrow_button.setFixedSize(100, 40)
    scarecrow_button.setStyleSheet("""
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
    button_row.addWidget(scarecrow_button, alignment=Qt.AlignLeft)

    info_window.content_layout.addLayout(button_row)
    info_window.content_layout.addWidget(scarecrow_button)

    def open_scarecrow():

        try:
            map_window.stop_sound()
        except Exception:
            pass

        info_window.scarecrow_window = ScarecrowWindow()
        info_window.scarecrow_window.setAttribute(Qt.WA_DeleteOnClose, True)
        info_window.scarecrow_window.setWindowModality(Qt.ApplicationModal)

        info_window.scarecrow_window.destroyed.connect(lambda: map_window.play_sound("footpath.mp3"))
        info_window.scarecrow_window.show()

    scarecrow_button.clicked.connect(open_scarecrow)

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
            "Βοήθεια – Μονοπάτι",
            "Σε αυτή την οθόνη μπορείτε να δείτε το ιστορικό μονοπάτι της καστροπολιτείας.\n\n"
            "- Πατήστε 'Σκιάχτρο' για να δείτε περισσότερα για το σκιάχτρο.\n"
            "- Πατήστε 'Πίσω στον χάρτη' για να επιστρέψετε στον χάρτη.\n"
            "- Πατήστε 'Προσθήκη' ώστε να συλλέξετε πληροφορίες για το μονοπάτι."
        )