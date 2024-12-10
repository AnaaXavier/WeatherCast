from PySide6.QtGui import QPixmap, QPainter, QColor
from PySide6.QtCore import Qt


class Background_icon:
    """
        Creates a black circle. It has a paramater named "icon_pixmap" used to change its size.
        
        param: icon_pixmap: QPixmap
    """
        
    def __init__(self):
        pass

    def create_circle(self, icon_pixmap: QPixmap) -> QPixmap:

        size = 90
        circle_pixmap = QPixmap(size, size)
        circle_pixmap.fill(Qt.transparent)

        painter = QPainter(circle_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(QColor("#212121"))
        painter.setPen(Qt.transparent)
        painter.drawEllipse(0, 0, size, size)
        painter.end()

        icon_scaled = icon_pixmap.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        painter.begin(circle_pixmap)
        painter.drawPixmap(0, 0, icon_scaled)
        painter.end()

        return circle_pixmap
