from PySide6.QtWidgets import QLabel, QPushButton, QScrollArea
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from helper_functions.info_window import InfoWindow
import re

collection_items = []

def add_to_collection(title, content):
    if not any(item['title'] == title for item in collection_items):
        collection_items.append({'title': title, 'content': content})

def show_collection(map_window):
    map_window.stop_background()
    map_window.play_sound("collection.mp3")

    title = "Προσωπική Συλλογή Γνώσεων"
    info_text = (
        '<span style="font-weight: bold; color: #ADD8E6;">'
        'Εδώ βρίσκεται η προσωπική σου συλλογή από όλες τις γνώσεις που έχεις μάθει μέχρι τώρα.'
        '</span>'
    )

    info_window = InfoWindow(title, info_text, "images/collection.jpg",
                             width=900, height=700, scrollable=True)

    scroll_area = info_window.findChild(QScrollArea)
    if scroll_area:
        scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: rgba(0, 0, 0, 100);
                border: none;
            }
        """)
        scroll_area.viewport().setStyleSheet("""
            background-color: rgba(0, 0, 0, 100);
            border: none;
        """)

    layout = info_window.content_layout
    content_widget = layout.parentWidget()
    content_widget.setAutoFillBackground(True)
    content_widget.setStyleSheet("background: transparent;")

    insert_index = layout.count() - 1 if layout.count() > 0 else 0
    insert_index += 1

    if collection_items:
        for item in collection_items:
            title_label = QLabel(f"• {item['title']}")
            title_label.setStyleSheet("color: white; font-weight: bold;")
            clean_text = re.sub(r'<[^>]*>', '', item['content'])
            content_label = QLabel()
            content_label.setWordWrap(True)
            content_label.setTextFormat(Qt.PlainText)
            content_label.setText(clean_text)
            content_label.setStyleSheet("color: white; background: transparent;")
            layout.insertWidget(insert_index, title_label)
            insert_index += 1
            layout.insertWidget(insert_index, content_label)
            insert_index += 1
    else:
        empty_label = QLabel("Η συλλογή σου είναι κενή αυτήν την στιγμή. Πρόσθεσε κάτι!")
        empty_label.setStyleSheet("color: white; font-weight: bold;")
        layout.insertWidget(insert_index, empty_label)
        insert_index += 1

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
    layout.addWidget(back_button)
    
    info_window.finished.connect(map_window.stop_sound)
    info_window.finished.connect(map_window.play_background)

    info_window.exec()