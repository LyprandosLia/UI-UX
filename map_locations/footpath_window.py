from PySide6.QtWidgets import QListWidget, QLabel, QPushButton, QScrollArea, QVBoxLayout, QWidget
from helper_functions.info_window import InfoWindow
from PySide6.QtCore import Qt
from helper_functions.collection_button import create_collection_button

def show_footpath(map_window):
    map_window.stop_background()
    map_window.play_sound("footpath.mp3") 

    collection_title = "Το Αρχαίο Μονοπάτι των Φρουρών"
    title = "Το μονοπάτι προς το Κάστρο"
    info_text = (
         '<span style="font-weight: bold; color: white;">'
        "Λέγεται πως το μονοπάτι που οδηγεί στο κάστρο δεν είναι απλώς ένας δρόμος. Πάνω σε πέτρες φθαρμένες από τα χρόνια, οι φρουροί του παρελθόντος έχουν αφήσει ψιθύρους και σημάδια που μόνο οι τολμηροί μπορούν να καταλάβουν. Καθώς περπατάς ανάμεσα στα δέντρα και τα πυκνά βάτα, νιώθεις ότι τα βλέμματα των παλιών φρουρών σε συνοδεύουν και ότι κάθε στροφή μπορεί να αποκαλύψει μυστικά κρυμμένα από αιώνες. Το μονοπάτι δεν οδηγεί μόνο στο κάστρο· σε καλεί να ανακαλύψεις τις ιστορίες που οι τοίχοι δεν μπορούν να πουν."
        '</span>'
    )
    info_window = InfoWindow(title, info_text, "images/footpath.jpg")
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