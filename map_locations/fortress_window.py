from helper_functions.info_window import InfoWindow

def show_fortress(map_window):
    map_window.stop_background()
    map_window.play_sound("fortress.mp3")

    title = "Βρισκόμαστε στο οχυρό!"
    info_text = (
        '<span style="font-weight: bold; color: white;">'
        'Το οχυρό είναι η κύρια αμυντική δομή της καστροπολιτείας μας, χτισμένο για να προστατεύει τους κατοίκους και τον βασιλιά. '
        'Στο εσωτερικό του οχυρού βρίσκονται οι φρουροί, ενώ υπάρχει η αίθουσα στρατηγικής και η αίθουσα του εξοπλισμού των πολεμιστών.'
        '</span>'
    )

    info_window = InfoWindow(title, info_text, "images/fortress.jpg")
    info_window.finished.connect(map_window.stop_sound)
    info_window.finished.connect(map_window.play_background)
    info_window.exec()