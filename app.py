from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel , QDialog, QFrame
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
import sys

# Info Window for displaying information about locations
class InfoWindow(QDialog):
    def __init__(self, title, info_text, bg_image = None):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(350, 350, 300, 300)
        layout = QVBoxLayout()
        
        #Setting the background image if provided
        if bg_image:
            bg_label = QLabel(self)
            pixmap = QPixmap(bg_image)
            bg_label.setPixmap(pixmap)  
            bg_label.setScaledContents(True)
            bg_label.setGeometry(0, 0, 300, 300)    
            bg_label.lower()

        label = QLabel(info_text, self)
        label.setWordWrap(True)
        label.setStyleSheet("color: white;")
        layout.addWidget(label)
       

        #Button for going back to map
        back_button = QPushButton("Back to Map")   
        back_button.clicked.connect(self.close)
        layout.addWidget(back_button)
        self.setLayout(layout)     

#Second Window which includes the map
class SecondWindow(QMainWindow):    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Καστροπολιτεία")
        self.setMinimumSize(QSize(400, 300))    
        self.setGeometry(250, 250, 1000, 600)

        
        centralWidget = QWidget()   
        layout = QVBoxLayout()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        # BackGround walls
        label = QLabel(centralWidget)
        pixmap = QPixmap("castle_walls.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)   
        label.setGeometry(0, 0, 1000, 600)  

        # Map
        map_label = QLabel()
        map_pixmap = QPixmap("map.png")
        map_label.setPixmap(map_pixmap)
        map_label.setScaledContents(True)
        map_label.setFixedSize(800, 400)

        map_container = QWidget()
        map_layout = QHBoxLayout()   
        map_layout.addStretch()
        map_layout.addWidget(map_label)
        map_layout.addStretch()
        map_container.setLayout(map_layout)

        layout.addWidget(map_container)

        # Castle Button
        castle_button = QPushButton("Κάστρο", map_label)
        castle_button.setGeometry(120, 70, 80, 80)
        castle_button.setFixedSize(80, 80)
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
        castle_button.clicked.connect(self.show_castle_info)

    def show_castle_info(self):
        title =  "About the castle"
        info_text = "This is the castle where the king lives. The castle is surrounded by high walls and has a large courtyard in the center. Inside, there are several rooms including the throne room, dining hall, and living quarters for the royal family."
        info_window = InfoWindow(title,info_text,"corridor.jpg")
        info_window.exec() 
    

#First Window which is the Welcome to the Castle City
class MainWinodw(QMainWindow):
    def __init__(self): 
        super().__init__()

        self.setWindowTitle("Eίσοδος")
        self.setMinimumSize(QSize(400, 300))    
        self.setGeometry(200,200, 1000, 600)

        centralWidget = QWidget()   
        layout = QVBoxLayout()

        label = QLabel(self)
        pixmap = QPixmap("castle.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)   
        self.setCentralWidget(label)

        button1 = QPushButton("Eίσοδος στην Καστροπολιτεία")    
        button1.setFixedSize(250, 40)
        button1.clicked.connect(self.open_second_window)

        layout.addWidget(label, stretch = 1)
        layout.addWidget(button1, alignment=Qt.AlignCenter) 

        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        self.second_window = SecondWindow()

    def open_second_window(self):
        self.second_window.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = MainWinodw()
    window.show()
    sys.exit(app.exec())