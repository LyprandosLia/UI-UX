from PySide6.QtWidgets import QMainWindow, QPushButton, QWidget
from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

# audio imports
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
import os

from map_locations.fortress_window import show_fortress
from map_locations.castle_window import show_castle
from map_locations.square_window import show_square
from map_locations.walls_window import show_walls
from map_locations.footpath_window import show_footpath
from collection_window import show_collection

class MapWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.setWindowTitle("Καστροπολιτεία")
        self.setMinimumSize(QSize(400, 300))
        self.setGeometry(250, 250, 1000, 600)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.bg_label = QLabel(centralWidget)
        self.bg_label.setPixmap(QPixmap("images/castle_walls.jpg"))
        self.bg_label.setScaledContents(True)
        self.bg_label.setGeometry(0, 0, 1000, 600)
        self.bg_label.lower()

        self.back_button = QPushButton("← Πίσω", centralWidget)
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
        self.back_button.move(20, 20)
        self.back_button.clicked.connect(self.go_back)
        self.back_button.raise_()

        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        # for background music (map.mp3)
        self.bg_player = QMediaPlayer()
        self.bg_audio_output = QAudioOutput()
        self.bg_player.setAudioOutput(self.bg_audio_output)

        # Map
        self.map_label = QLabel(centralWidget)
        map_pixmap = QPixmap("images/map.png")
        self.map_label.setPixmap(map_pixmap)
        self.map_label.setScaledContents(True)
        self.map_label.setFixedSize(800, 400)
        self.center_map()
        # All buttons
        # Castle Button
        castle_button = QPushButton("Κάστρο", self.map_label)
        castle_button.setGeometry(125, 85, 80, 80)
        castle_button.setFixedSize(60, 60)
        castle_button.setStyleSheet("""
            QPushButton {
                border-radius: 40px;  
                background-color: brown; 
                color: white;
                font-weight: bold;
                border: 2px solid #2980b9;
            }
            QPushButton:hover {
                background-color: red;
            }
        """)
        castle_button.clicked.connect(lambda: show_castle(self))

        # Square Button
        square_button = QPushButton("Πλατεία", self.map_label)
        square_button.setGeometry(260, 220, 80, 80)
        square_button.setFixedSize(60, 60)
        square_button.setStyleSheet("""
                    QPushButton {
                        border-radius: 40px;  
                        background-color: green; 
                        color: white;
                        font-weight: bold;
                        border: 2px solid #2980b9;
                    }
                    QPushButton:hover {
                        background-color: red;
                    }
                """)
        square_button.clicked.connect(lambda: show_square(self))

        # Fortress Button
        fortress_button = QPushButton("Οχυρό", self.map_label)
        fortress_button.setGeometry(300, 160, 80, 80)
        fortress_button.setFixedSize(60, 60)
        fortress_button.setStyleSheet("""
                            QPushButton {
                                border-radius: 30px;  
                                background-color: red; 
                                color: white;
                                font-weight: bold;
                                border: 2px solid #2980b9;
                            }
                            QPushButton:hover {
                                background-color: red;
                            }
                        """)
        fortress_button.clicked.connect(lambda: show_fortress(self))
        # Walls Button  
        walls_button = QPushButton("Τείχη", self.map_label)
        walls_button.setGeometry(500, 100, 100, 30)
        walls_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                font-weight: bold;
                border-radius: 10px;  
                border: 2px solid #2980b9;      
                }
            QPushButton:hover {
                background-color: #2ecc71;
            }       
        """)      
        walls_button.clicked.connect(lambda: show_walls(self))             
        #Footpath Button
        footpath_button = QPushButton("Μονοπάτι", self.map_label)
        footpath_button.setGeometry(400, 200, 100, 30)
        footpath_button.setStyleSheet("""
            QPushButton {
                background-color: #f39c12;  
                color: white;
                font-weight: bold;
                border-radius: 10px;  
                border: 2px solid #2980b9;      
                }
            QPushButton:hover {
                background-color: #f1c40f;
            }       
        """)
        footpath_button.clicked.connect(lambda: show_footpath(self))
        # Collection Button
        collection_button = QPushButton("Συλλογή", self.map_label)
        collection_button.setGeometry(670, 350, 100, 30)
        collection_button.setStyleSheet("""
            QPushButton {
                background-color: #8e44ad;
                color: white;
                font-weight: bold;
                border-radius: 10px;
                border: 2px solid #2980b9;
            }
            QPushButton:hover {
                background-color: #9b59b6;
            }
        """)
        collection_button.clicked.connect(lambda: show_collection(self))

    def play_sound(self, filename, loop=False):
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "sounds", filename)
        url = QUrl.fromLocalFile(file_path)
        self.player.setSource(url)
        self.player.play()
        if loop:
            self.player.setLoops(QMediaPlayer.Infinite)

    def stop_sound(self):
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.stop()

    def resizeEvent(self, event):
        self.bg_label.resize(self.size())
        self.back_button.raise_()
        super().resizeEvent(event)

    def play_background(self):
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, "sounds", "map.mp3")
        url = QUrl.fromLocalFile(file_path)
        self.bg_player.setSource(url)
        self.bg_player.play()
        self.bg_player.setLoops(QMediaPlayer.Infinite)

    def stop_background(self):
        if self.bg_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.bg_player.stop()

    def go_back(self):
        self.stop_sound()
        self.stop_background()
        self.hide()
        self.main_window.show()

    def showEvent(self, event):
        super().showEvent(event)
        self.play_background()

    def closeEvent(self, event):
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.stop()
        event.accept()

    def resizeEvent(self, event):  # ⚡ ΝΕΟ: override της resizeEvent
        """Καλείται κάθε φορά που αλλάζει μέγεθος το παράθυρο."""
        self.bg_label.setGeometry(0, 0, self.width(), self.height())  # ⚡ ΑΛΛΑΓΗ: τεντώνουμε το background
        self.center_map()  # ⚡ ΑΛΛΑΓΗ: ξανακεντράρουμε το map_label
        super().resizeEvent(event)

    def center_map(self):  # ⚡ ΝΕΟ: βοηθητική συνάρτηση για να βάζει το map_label στο κέντρο
        """Τοποθετεί τον χάρτη στο κέντρο του παραθύρου."""
        x = (self.width() - self.map_label.width()) // 2
        y = (self.height() - self.map_label.height()) // 2
        self.map_label.move(x, y)