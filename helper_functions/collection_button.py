from PySide6.QtWidgets import QPushButton, QMessageBox
from collection_window import add_to_collection

def create_collection_button(parent_window, title, content, x_offset=20, y_offset=50):
    button_width, button_height = 180, 35
    x_pos = parent_window.width() - button_width - x_offset
    y_pos = parent_window.height() - button_height - y_offset

    collect_button = QPushButton("Προσθήκη", parent_window)
    collect_button.setGeometry(x_pos, y_pos, button_width, button_height)
    collect_button.setStyleSheet("""
           QPushButton {
               background-color: #f1c40f; 
               color: black;
               font-weight: bold;
               border-radius: 10px;
               border: 2px solid #b7950b;
           }
           QPushButton:hover {
               background-color: #f7dc6f;
           }
       """)

    def on_click():
        add_to_collection(title, content)
        QMessageBox.information(parent_window, "Προστέθηκε", "Η πληροφορία προστέθηκε με επιτυχία στη συλλογή σου!")

    collect_button.clicked.connect(on_click)
    return collect_button
