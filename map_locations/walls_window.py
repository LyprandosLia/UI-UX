from PySide6.QtWidgets import QListWidget, QLabel, QPushButton, QScrollArea, QVBoxLayout, QWidget, QHBoxLayout
from helper_functions.info_window import InfoWindow
from PySide6.QtCore import Qt
from helper_functions.collection_button import create_collection_button

from characters.archer.archer import ArcherWindow

def show_walls(map_window):
    map_window.stop_background()
    map_window.play_sound("walls.mp3") 

    collection_title = "Τα ιστορικά τείχη της Καστροπολιτείας"
    title = "Τα τείχη του Κάστρου"
    info_text = (
         '<span style="font-weight: bold; color: white;">'
        "Τα τείχη του Κάστρου των Τεσσάρων Ανέμων υψώνονται εδώ και αιώνες, σμιλεμένα από μαύρη πέτρα που λέγεται πως εξορύχτηκε από το ίδιο το βουνό όπου κοιμόταν ένας δράκος. Χτισμένα αρχικά για να αποκρούσουν τις εισβολές βόρειων φυλών, τα τείχη άντεξαν πολιορκίες, φωτιά και καταιγίδες, χωρίς ποτέ να πέσουν ολοκληρωτικά."
        '</span>'
    )
    info_window = InfoWindow(title, info_text, "images/castle_walls2.jpg")
    create_collection_button(info_window, collection_title, info_text)

    archer_button = QPushButton("Τοξότρια")
    archer_button.setFixedSize(100, 40)
    archer_button.setStyleSheet("""
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
    button_row.addWidget(archer_button, alignment=Qt.AlignLeft)

    info_window.content_layout.addLayout(button_row)
    info_window.content_layout.addWidget(archer_button)

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

    def show_walls_help(window):
        from PySide6.QtWidgets import QMessageBox
        QMessageBox.information(
            window,
            "Βοήθεια – Τείχη Κάστρου",
            "Σε αυτή την οθόνη μπορείτε να δείτε τα ιστορικά τείχη του Κάστρου.\n\n"
            "- Πατήστε 'Τοξότρια' για να δείτε περισσότερα για την τοξότρια.\n"
            "- Πατήστε 'Πίσω στον χάρτη' για να επιστρέψετε στον χάρτη.\n"
            "- Πατήστε 'Προσθήκη' ώστε να συλλέξετε πληροφορίες για τα τείχη."
        )
    def open_archer():

        try:
            map_window.stop_sound()
        except Exception:
            pass


        info_window.archer_window = ArcherWindow()
        info_window.archer_window.setAttribute(Qt.WA_DeleteOnClose, True)
        info_window.archer_window.setWindowModality(Qt.ApplicationModal)

        info_window.archer_window.destroyed.connect(lambda: map_window.play_sound("walls.mp3"))
        info_window.archer_window.show()

    archer_button.clicked.connect(open_archer)

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