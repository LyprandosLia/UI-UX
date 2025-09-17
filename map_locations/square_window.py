from PySide6.QtWidgets import QListWidget, QLabel
from helper_functions.info_window import InfoWindow

def show_square(map_window):
    map_window.stop_background()

    title = "Καλώς ήρθατε στην κεντρική πλατεία!"
    info_text = (
        '<span style="font-weight: bold; color: white;">'
        'Άκου τους ήχους από το παζάρι, το πανηγύρι ή την χορωδία.'
        '</span>'
    )
    info_window = InfoWindow(title, info_text, "images/square.jpg")

    list_widget = QListWidget(info_window)
    list_widget.addItems(["Παζάρι", "Πανηγύρι", "Χορωδία"])
    list_widget.setGeometry(50, 400, 150, 100)

    info_label = QLabel("Διάλεξε μια δραστηριότητα", info_window)
    info_label.setWordWrap(True)
    info_label.setGeometry(220, 400, 500, 100)

    def show_square_info(current, previous):
        if not current:
            return
        text = current.text()
        if "Παζάρι" in text:
            info_label.setText(
                '<span style="color: white; background-color: black; padding: 5px;">'
                'Ένα παραμύθι για το παζάρι...'
                '</span>'
            )
            map_window.play_sound("bazaar.mp3")
        elif "Πανηγύρι" in text:
            info_label.setText(
                '<span style="color: white; background-color: black; padding: 5px;">'
                'Το μεγάλο πανηγύρι με μουσική και χορό!'
                '</span>'
            )
            map_window.play_sound("festival.mp3")
        elif "Χορωδία" in text:
            info_label.setText(
                '<span style="color: white; background-color: black; padding: 5px;">'
                'Η χορωδία τραγουδά παραδοσιακά τραγούδια.'
                '</span>'
            )
            map_window.play_sound("choir.mp3")

    list_widget.currentItemChanged.connect(show_square_info)

    info_window.finished.connect(map_window.stop_sound)
    info_window.finished.connect(map_window.play_background)
    info_window.exec()