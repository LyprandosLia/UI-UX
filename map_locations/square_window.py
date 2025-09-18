from PySide6.QtWidgets import QListWidget, QLabel, QPushButton, QScrollArea, QVBoxLayout, QWidget
from helper_functions.info_window import InfoWindow
from PySide6.QtCore import Qt
from helper_functions.collection_button import create_collection_button

def show_square(map_window):
    map_window.stop_background()
    collection_button = None

    title = "Καλώς ήρθατε στην κεντρική πλατεία!"
    info_text = (
        '<span style="font-weight: bold; color: white;">'
        'Άκου τους ήχους από το παζάρι, το πανηγύρι ή την χορωδία.'
        '</span>'
    )

    info_window = InfoWindow(title, info_text, "images/square.jpg", width=700, height=500, scrollable=False)

    list_container = QWidget()
    list_container.setStyleSheet("background-color: rgba(0, 0, 0, 150); border-radius: 10px;")
    list_container.setFixedSize(150, 100)
    info_window.content_layout.addWidget(list_container)

    list_widget = QListWidget(list_container)
    list_widget.addItems(["Παζάρι", "Πανηγύρι", "Χορωδία"])
    list_widget.setStyleSheet("""
        QListWidget {
            background-color: transparent;
            color: white;
            border: none;
        }
        QListWidget::item:selected {
            background-color: rgba(255, 255, 255, 80);
        }
    """)
    list_widget.setGeometry(0, 0, 150, 100)

    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setFixedHeight(180)
    content_widget = QWidget()
    scroll_layout = QVBoxLayout(content_widget)

    info_label = QLabel("Διάλεξε μια δραστηριότητα")
    info_label.setWordWrap(True)
    info_label.setAlignment(Qt.AlignmentFlag.AlignTop)
    info_label.setStyleSheet("color: white; padding: 5px; background-color: rgba(0,0,0,180);")

    scroll_layout.addWidget(info_label)
    scroll_area.setWidget(content_widget)
    info_window.content_layout.addWidget(scroll_area)

    def show_square_info(current, previous):
        nonlocal collection_button

        if not current:
            return
        text = current.text()

        if collection_button:
            info_window.content_layout.removeWidget(collection_button)
            collection_button.deleteLater()
            collection_button = None

        if "Παζάρι" in text:
            info_label.setText(
                '<span style="color: white; background-color: black; padding: 5px;">'
                'Στο παζάρι έμποροι από κάθε γωνιά της καστροπολιτείας εκθέτουν τα προϊόντα τους: σπάνια νομίσματα, υφάσματα, κεραμικά και αρωματικά κεριά. Οι πολίτες και οι επισκέπτες συναντιούνται για να συζητήσουν νέα, να διαπραγματευτούν τις τιμές και να θαυμάσουν τις δεξιότητες των τεχνιτών της καστροπολιτείας.'
                '</span>'
            )
            map_window.play_sound("bazaar.mp3")
            collection_title = "Πληροφορίες Παζαριού:"
        elif "Πανηγύρι" in text:
            info_label.setText(
                '<span style="color: white; background-color: black; padding: 5px;">'
                'Στην καρδιά της καστροπολιτείας, στην κεντρική πλατεία, παίρνει μέρος ένα ζωντανό πανηγύρι γεμάτο μουσική και χορούς. Εκεί βρίσκονται διάφοροι πωλητές που έχουν στους πάγκους τους χειροποίητα αντικείμενα, υφάσματα και μεσαιωνικά τρόφιμα, ενώ οι μουσικοί παίζουν με χαρά τα λαούτα και τα τύμπανά τους, στους ρυθμούς των τραγουδιών. Οι μυρωδιές από ψωμί που ψήνεται στα ξύλα, καπνιστά κρέατα και μέλι γεμίζουν την ατμόσφαιρα, ενώ σημαίες κρέμονται κατά μήκος των δρόμων, προσθέτοντας στο σκηνικό μια ζωντανή γιορτινή αίσθηση. Το πανηγύρι είναι μια πραγματική γιορτή για όλες τις αισθήσεις, που φέρνει κοντά κατοίκους και επισκέπτες σε μια μοναδική εμπειρία μεσαιωνικής ζωής.'
                '</span>'
            )
            map_window.play_sound("festival.mp3")
            collection_title = "Πληροφορίες Πανηγυριού:"
        elif "Χορωδία" in text:
            info_label.setText(
                '<span style="color: white; background-color: black; padding: 5px;">'
                'Η χορωδία γεμίζει τους πέτρινους τοίχους της καστροπολιτείας μας με μελωδίες από τον μεσαιωνικό κόσμο. Οι φωνές των τραγουδιστών αντηχούν στις αίθουσες και τους δρόμους, μεταφέροντας ιστορίες γενναιότητας, τιμής και αγάπης. Οι ακροατές ζούν μια μοναδική εμπειρία, ακούγοντας τα τραγούδια που αποτυπώνουν την ψυχή της καστροπολιτείας.'
                '</span>'
            )
            map_window.play_sound("choir.mp3")
            collection_title = "Πληροφορίες Χορωδίας:"

        collection_button = create_collection_button(info_window, collection_title, info_label.text())
        info_window.content_layout.addWidget(collection_button)

        info_window.content_layout.addWidget(back_button)

    list_widget.currentItemChanged.connect(show_square_info)
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