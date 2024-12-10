import os
import sys

from PySide6.QtWidgets import (
    QApplication, QLabel, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QWidget
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHeaderView
from PySide6.QtGui import QIcon

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from Model import api
from pixmap_circle import Background_icon

class Forecast_window(QWidget):
    """
    Creates a new window while obtains information from the main window to request results to an API.
    
    A parameter is needed to continue, however, if nothing is provided, its default response will be "None".
    
    Param: forecast_info
    """
    
    def __init__(self, forecast_info=None):
        super().__init__()
        
        # unpacks the tuple
        self.forecast_icon, self.country, self.temperature, self.temp_min, self.temp_max, self.description, self.humidity, self.visibility, self.thermic_sensation, self.wind_speed = forecast_info
        
        self.setWindowTitle("Forecast")
        self.setWindowIcon(QIcon("images/w_bg_icon.png"))
        self.setFixedSize(400, 322)
        
        self.weather_api = api.Weather_API("e8f5508a551e47209e051618ef638adb")
        
        self.weather_icon = QLabel()
        self.degrees_lbl = QLabel(f"Temperature: {self.temperature:.2f}°C")
        self.country_lbl = QLabel(f"Country: {self.country}")

        self.circle = Background_icon()
        self.pixmap_icon = self.weather_api.get_icon(self.forecast_icon)

        # verifies if an icon is successfully recovered from api to show it on screen
        if self.pixmap_icon and not self.pixmap_icon.isNull():
            circle_pixmap = self.circle.create_circle(self.pixmap_icon)
            self.weather_icon.setFixedSize(100, 100)
            self.weather_icon.setScaledContents(True)
            self.weather_icon.setPixmap(circle_pixmap)
            
        else:
            self.pixmap = QPixmap(100, 100)
            self.pixmap.fill(Qt.gray)
            self.weather_icon.setPixmap(self.pixmap)

        self.weather_icon.setAlignment(Qt.AlignCenter)
        self.degrees_lbl.setAlignment(Qt.AlignCenter)
        self.country_lbl.setAlignment(Qt.AlignCenter)

        # creates a table that holds all information obtained from the api
        self.weather_table = QTableWidget(7, 2)
        self.weather_table.setHorizontalHeaderLabels(["Description", "Details"])
        self.weather_table.setItem(0, 0, QTableWidgetItem("Weather"))
        self.weather_table.setItem(0, 1, QTableWidgetItem(f"{self.description}"))
        
        self.weather_table.setItem(1, 0, QTableWidgetItem("Temp min"))
        self.weather_table.setItem(1, 1, QTableWidgetItem(f"{self.temp_min:.2f}"))
        
        self.weather_table.setItem(2, 0, QTableWidgetItem("Temp max"))
        self.weather_table.setItem(2, 1, QTableWidgetItem(f"{self.temp_max:.2f}"))
        
        self.weather_table.setItem(3, 0, QTableWidgetItem("Humidity"))
        self.weather_table.setItem(3, 1, QTableWidgetItem(f"{self.humidity}%"))
        
        self.weather_table.setItem(4, 0, QTableWidgetItem("Wind Speed"))
        self.weather_table.setItem(4, 1, QTableWidgetItem(f"{self.wind_speed} m/s"))
        
        self.weather_table.setItem(5, 0, QTableWidgetItem("Visibility"))
        self.weather_table.setItem(5, 1, QTableWidgetItem(f"{self.visibility} km"))
        
        self.weather_table.setItem(6, 0, QTableWidgetItem("Thermal sensation"))
        self.weather_table.setItem(6, 1, QTableWidgetItem(f"{self.thermic_sensation:.2f}°C"))

        # this sets the headers' properties
        self.header = self.weather_table.horizontalHeader()
        self.header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.header.setSectionResizeMode(1, QHeaderView.Stretch)
        self.weather_table.verticalHeader().setVisible(False)
        self.weather_table.resizeRowsToContents()
        self.weather_table.setShowGrid(True)

        # deactivates the possibility of user editing the table
        self.weather_table.setEditTriggers(QTableWidget.NoEditTriggers)
        
        self.info_layout = QHBoxLayout()
        self.info_layout.addWidget(self.weather_icon)
        self.info_layout.addWidget(self.degrees_lbl)
        self.info_layout.addWidget(self.country_lbl)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.info_layout)
        self.main_layout.addWidget(self.weather_table)
        
        self.setLayout(self.main_layout)
