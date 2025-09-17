from helper_functions.info_window import InfoWindow

def show_castle(map_window):
    map_window.stop_background()
    map_window.play_sound("castle.mp3")

    title = "Πληροφορίες Κάστρου"
    info_text = (
        '<span style="font-weight: bold; color: white;">'
        'Εδώ βρίσκεται το κάστρο που ζει ο βασιλιάς. Το κάστρο περιβάλλεται από ψηλά τείχη και έχει μια μεγάλη αυλή στο κέντρο. '
        'Στο εσωτερικό, υπάρχουν πολλά δωμάτια όπως η αίθουσα του θρόνου, η τραπεζαρία και οι χώροι διαμονής για τη βασιλική οικογένεια.'
        '</span>'
    )

    info_window = InfoWindow(title, info_text, "images/corridor.jpg")
    info_window.finished.connect(map_window.stop_sound)
    info_window.finished.connect(map_window.play_background)
    info_window.exec()