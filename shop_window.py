from PySide6.QtWidgets import QDialog, QVBoxLayout, QGridLayout, QLineEdit, QScrollArea, QLabel, QPushButton, \
    QMessageBox, QWidget
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Signal, Qt
import re  # for payment process
# audio imports
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
import os


class ClickableLabel(QLabel):
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)


class ShopWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.play_sound("violin.mp3")

        self.setWindowTitle("Κατάστημα Αναμνηστικών")
        self.resize(1000, 700)
        self.move(200, 150)
        self.setStyleSheet("""
                    ShopWindow {
                        border-image: url(images/shop/shop_background.jpg) 0 0 0 0 stretch stretch;
                    }
                """)

        self.descriptions = {
            "Μικρογραφία Κάστρου": "Μια λεπτομερής μικρογραφία που αναπαριστά το κάστρο της καστροπολιτείας.\n\nΤιμή: 30€",
            "Χάρτης Καστροπολιτείας": "Ο λεπτομερής χάρτης της καστροπολιτείας μας.\n\nΤιμή: 20€",
            "Σπαθί Ιππότη": "Μινιατούρα ενός αυθεντικού μεσαιωνικού σπαθιού.\n\nΤιμή: 15€",
            "Ασπίδα Ιππότη": "Μινιατούρα μιας αυθεντικής μεσαιωνικής ασπίδας.\n\nΤιμή: 15€",
            "Πανοπλία Ιππότη": "Μινιατούρα μιας αυθεντικής μεσαιωνικής πανοπλίας.\n\nΤιμή: 15€",
            "Μεσαιωνική Σημαία": "Σημαία διαστάσεων 80x30 με τα χρώματα της καστροπολιτείας μας.\n\nΤιμή: 25€",
            "Μεσαιωνικό Νόμισμα": "Αντίγραφο νομίσματος από τον μεσαίωνα.\n\nΤιμή: 4€",
            "Μεσαιωνικό Κερί": "Χειροποίητο μεσαιωνικό κερί.\n\nΤιμή: 5€",
            "Χρυσό Κύπελλο": "Αντίγραφο πολυτελούς μεσαιωνικού κυπέλλου.\n\nΤιμή: 30€",
            "Συλλεκτικό Βιβλίο": "Συλλεκτικό βιβλίο με την ιστορία της καστροπολιτείας μας.\n\nΤιμή: 35€"
        }
        

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(main_layout)
        

        welcome_label = QLabel("Καλώς ήρθατε στο Κατάστημα Αναμνηστικών!")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet("font-size: 15px; font-weight: bold; color: white;")
        main_layout.addWidget(welcome_label)
        welcome_label2 = QLabel("Πατήστε το εικονίδιο του κάθε αντικειμένου για περισσότερες πληροφορίες.")
        welcome_label2.setAlignment(Qt.AlignCenter)
        welcome_label2.setStyleSheet("font-size: 13px; color: white;")
        main_layout.addWidget(welcome_label2)

        # Scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background: transparent;")
        main_layout.addWidget(scroll)

        container = QWidget()
        scroll.setWidget(container)

        self.back_button = QPushButton("← Πίσω", self)
        self.back_button.setStyleSheet("""
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
        self.back_button.setFixedSize(60, 27)
        self.back_button.move(20, 20)
        self.back_button.clicked.connect(self.go_back)
        self.back_button.raise_()

        # Grid layout (3 columns)
        grid = QGridLayout()
        grid.setSpacing(20)
        container.setLayout(grid)

        items = [
            ("Μικρογραφία Κάστρου", "images/shop/castle_souvenir.png", 30),
            ("Χάρτης Καστροπολιτείας", "images/map.png", 20),
            ("Σπαθί Ιππότη", "images/shop/sword_souvenir.png", 15),
            ("Ασπίδα Ιππότη", "images/shop/shield_souvenir.png", 15),
            ("Πανοπλία Ιππότη", "images/shop/armor_souvenir.png", 15),
            ("Μεσαιωνική Σημαία", "images/shop/banner_souvenir.png", 25),
            ("Μεσαιωνικό Νόμισμα", "images/shop/coin_souvenir.png", 4),
            ("Μεσαιωνικό Κερί", "images/shop/candle_souvenir.png", 5),
            ("Χρυσό Κύπελλο", "images/shop/goblet_souvenir.png", 30),
            ("Συλλεκτικό Βιβλίο", "images/shop/book_souvenir.png", 35)
        ]

        for i, (name, img, price) in enumerate(items):
            row = i // 3
            col = i % 3

            item_widget = QWidget()
            item_layout = QVBoxLayout()
            item_layout.setAlignment(Qt.AlignCenter)
            item_widget.setLayout(item_layout)

            item_widget.setStyleSheet(
                "background: rgba(0, 0, 0, 200); border-radius: 10px; padding: 5px;"
            )
            

            img_label = ClickableLabel()
            pixmap = QPixmap(img)
            if not pixmap.isNull():
                pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            img_label.setPixmap(pixmap)
            img_label.setAlignment(Qt.AlignCenter)
            img_label.clicked.connect(lambda n=name, p=img: self.preview_item(n, p))

            name_label = QLabel(name)
            name_label.setAlignment(Qt.AlignCenter)
            name_label.setStyleSheet("font-weight: bold; color: white;")

            price_label = QLabel(f"{price} €")
            price_label.setAlignment(Qt.AlignCenter)
            price_label.setStyleSheet("color: yellow; font-size: 14px;")

            buy_button = QPushButton("Αγορά")
            buy_button.clicked.connect(lambda _, n=name: self.buy_item(n))
            buy_button.setStyleSheet("""
            QPushButton {
                color: white;   /* Μόνο το κείμενο γίνεται λευκό */
            }
           """)
            item_layout.addWidget(img_label)
            item_layout.addWidget(name_label)
            item_layout.addWidget(price_label)
            item_layout.addWidget(buy_button)

            grid.addWidget(item_widget, row, col)

            # Online help
            help_button = QPushButton("Help", self)
            help_button.setStyleSheet("color: white; background-color: gray;")
            help_button.move(850, 20)  
            help_button.clicked.connect(self.show_help)
            help_button.raise_()

    def show_help(self):
        QMessageBox.information(
            self,
        "Οδηγίες Αγοράς στο Κατάστημα Αναμνηστικών",
        """Επιλέξτε το αντικείμενο της αρεσκείας σας.
        Πατήστε πάνω στο αντικείμενο ώστε να δείτε την περιγραφή του.

        Πατήστε 'Αγορά' και εισάγετε τα στοιχεία χρέωσης.
        ΠΡΟΣΟΧΗ: Φροντίστε να συμπληρώσετε όλα τα πεδία τα πέδια χρέωσης."""
    )
    def play_sound(self, filename):
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "sounds", filename)
        url = QUrl.fromLocalFile(file_path)
        self.player.setSource(url)
        self.player.play()

    def stop_sound(self):
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.stop()

    def go_back(self):
        self.close()

    def closeEvent(self, event):
        self.stop_sound()
        super().closeEvent(event)

    def preview_item(self, item_name, img_path):
        from PySide6.QtWidgets import QDialog, QVBoxLayout
        dialog = QDialog(self)
        dialog.setWindowTitle(item_name)
        dialog.setGeometry(500, 300, 400, 400)
        layout = QVBoxLayout()
        dialog.setLayout(layout)

        bg_label = QLabel(dialog)
        bg_pixmap = QPixmap("images/shop/wood_background.jpg")
        bg_label.setPixmap(bg_pixmap)
        bg_label.setScaledContents(True)
        bg_label.resize(dialog.size())
        bg_label.lower()

        img_label = QLabel()
        pixmap = QPixmap(img_path)
        if not pixmap.isNull():
            pixmap = pixmap.scaled(250, 250, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        img_label.setPixmap(pixmap)
        img_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(img_label)

        name_label = QLabel(item_name)
        name_label.setAlignment(Qt.AlignCenter)
        name_label.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        layout.addWidget(name_label)

        desc_text = self.descriptions.get(item_name, "Δεν υπάρχει διαθέσιμη περιγραφή για αυτό το αντικείμενο.")
        desc = QLabel(desc_text)
        desc.setWordWrap(True)
        desc.setAlignment(Qt.AlignCenter)
        desc.setStyleSheet("color: white;")
        layout.addWidget(desc)

        buy_button = QPushButton("Αγορά")
        buy_button.setStyleSheet("""
            background-color: yellow;
            color: black;
            font-weight: bold;
            border-radius: 5px;
            padding: 5px;
        """)
        buy_button.clicked.connect(lambda: self.buy_item(item_name))
        layout.addWidget(buy_button)

        def resize_event(event):
            bg_label.resize(dialog.size())

        dialog.resizeEvent = resize_event
        dialog.exec()

    def buy_item(self, item_name):

        class PaymentDialog(QDialog):
            def __init__(self, parent=None):
                super().__init__(parent)
                self.setWindowTitle(f"Αγορά: {item_name}")
                self.setGeometry(500, 300, 400, 400)

                self.bg_label = QLabel(self)
                bg_pixmap = QPixmap("images/shop/paper_background.jpg")
                self.bg_label.setPixmap(bg_pixmap)
                self.bg_label.setScaledContents(True)
                self.bg_label.resize(self.size())
                self.bg_label.lower()

                layout = QVBoxLayout()
                layout.setContentsMargins(10, 10, 10, 10)

                def add_label(text):
                    lbl = QLabel(text)
                    lbl.setStyleSheet("color: black; font-weight: bold;")
                    layout.addWidget(lbl)
                    return lbl

                add_label("Διεύθυνση:")
                self.address_input = QLineEdit()
                layout.addWidget(self.address_input)

                add_label("Ταχυδρομικός Κώδικας:")
                self.postal_input = QLineEdit()
                self.postal_input.setMaxLength(5)
                layout.addWidget(self.postal_input)

                add_label("Όνομα Κατόχου Κάρτας:")
                self.name_input = QLineEdit()
                layout.addWidget(self.name_input)

                add_label("Αριθμός Κάρτας:")
                self.card_input = QLineEdit()
                self.card_input.setMaxLength(16)
                layout.addWidget(self.card_input)

                add_label("Ημερομηνία Λήξης (MM/YY):")
                self.exp_input = QLineEdit()
                layout.addWidget(self.exp_input)

                add_label("CVV:")
                self.cvv_input = QLineEdit()
                self.cvv_input.setMaxLength(3)
                layout.addWidget(self.cvv_input)

                pay_button = QPushButton("Πληρωμή")
                pay_button.setStyleSheet("""
                    background-color: yellow;
                    color: black;
                    font-weight: bold;
                    border-radius: 5px;
                    padding: 5px;
                """)
                pay_button.clicked.connect(self.process_payment)
                layout.addWidget(pay_button)

                self.setLayout(layout)

            def resizeEvent(self, event):
                self.bg_label.resize(self.size())
                super().resizeEvent(event)

            def process_payment(self):
                address = self.address_input.text().strip()
                postal = self.postal_input.text().strip()
                name = self.name_input.text().strip()
                card = self.card_input.text().strip()
                exp = self.exp_input.text().strip()
                cvv = self.cvv_input.text().strip()

                if not all([address, postal, name, card, exp, cvv]):
                    QMessageBox.warning(self, "Σφάλμα", "Όλα τα πεδία είναι υποχρεωτικά.")
                    return

                if not (card.isdigit() and len(card) == 16):
                    QMessageBox.warning(self, "Σφάλμα", "Ο αριθμός κάρτας πρέπει να έχει 16 ψηφία.")
                    return

                if not re.match(r'^(0[1-9]|1[0-2])\/\d{2}$', exp):
                    QMessageBox.warning(self, "Σφάλμα", "Η ημερομηνία λήξης πρέπει να είναι στη μορφή MM/YY.")
                    return

                if not (cvv.isdigit() and len(cvv) == 3):
                    QMessageBox.warning(self, "Σφάλμα", "Το CVV πρέπει να έχει 3 ψηφία.")
                    return

                if not (postal.isdigit() and len(postal) == 5):
                    QMessageBox.warning(self, "Σφάλμα", "Ο ταχυδρομικός κωδικός πρέπει να έχει 5 ψηφία (π.χ. 12345).")
                    return

                QMessageBox.information(self, "Επιτυχία", f"Η αγορά του '{item_name}' ολοκληρώθηκε.")
                self.accept()

        dlg = PaymentDialog(self)
        dlg.exec()
