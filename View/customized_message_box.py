from PySide6.QtWidgets import QApplication, QMessageBox, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QIcon

def custom_message_box(title, message, icon_size=(30, 30)):
    """
    Creates a customized error window.
    
    param: title, message, icon_size (icon_size has x and y set to 30 by default).
    """
    
    qApp.setWindowIcon(QIcon("images/error.png"))
    
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(message)

    custom_icon = QPixmap("images/error.png")
    custom_icon = custom_icon.scaled(icon_size[0], icon_size[1], Qt.AspectRatioMode.KeepAspectRatio)
    msg_box.setIconPixmap(custom_icon)

    custom_button = msg_box.addButton("OK", QMessageBox.AcceptRole)
    custom_button.setStyleSheet("""
        QPushButton {
            background-color: #212121;
            color: white;
            border-radius: 5px;
            padding: 4px;
            padding-right: 30px;
            padding-left: 30px;
            font-size: 12px;
        }
        QPushButton:hover {
            background-color: #333333;
        }
        QPushButton:pressed {
            background-color: #111111;
        }
    """)
    
    layout = msg_box.layout()
    layout.setAlignment(custom_button, Qt.AlignmentFlag.AlignHCenter)

    msg_box.exec()
