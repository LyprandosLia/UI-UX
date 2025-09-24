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
    info_window.content_layout.addStretch(1)


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
    info_window.exec()