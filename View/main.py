import os
import sys

from PySide6.QtWidgets import QApplication, QSlider, QMessageBox, QLabel, QCheckBox, QSpacerItem, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy, QMessageBox
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from Model import api
from Controller import handle_user_input
from forecast_window import Forecast_window
from customized_message_box import custom_message_box

class Main(QMainWindow):
    """
    The main window of the application.
    
    It's the primary interface for the user. It manages core widgets and handles the information obtained from user to other classes.
    
    Methods: get_input_info(city, country_code), call_forecast_window()
    
    Methods params: city, country_code
    """
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather forecast")
        self.setFixedSize(400, 165)
        self.setWindowIcon(QIcon("images/w_bg_icon.png"))

        self.API_KEY = os.getenv("OPENWEATHER_API_KEY")
        self.weather_forecast = api.Weather_API(self.API_KEY)

        self.city_name_lbl = QLabel("City name")
        self.country_code_lbl = QLabel("Country code")
        
        self.city_name = QLineEdit()
        self.city_name.setPlaceholderText("ex: London, Tokyo, New York...")
        self.city_name.setStyleSheet("""QLineEdit { border: 1px solid #b3b3b3; border-radius: 10px; padding: 5px; font-size: 14px;}""")
        
        self.country_code = QLineEdit()
        self.country_code.setPlaceholderText("ex: UK, JP, US...")
        self.country_code.setStyleSheet("""QLineEdit { border: 1px solid #b3b3b3; border-radius: 10px; padding: 5px; font-size: 14px;}""")
        
        self.search_btn = QPushButton("Search")
        self.search_btn.setStyleSheet("""QPushButton { background-color: #212121; color: white; border-radius: 5px; padding: 30px; font-size: 12px; } QPushButton:hover { background-color: #333333; } QPushButton:pressed { background-color: #111111; }""")
        
        self.button_allignment = QHBoxLayout()
        self.button_allignment.addWidget(self.search_btn)
        self.button_allignment.setAlignment(Qt.AlignCenter)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.city_name_lbl)
        self.v_layout.addWidget(self.city_name)
        self.v_layout.addWidget(self.country_code_lbl)
        self.v_layout.addWidget(self.country_code)
        self.v_layout.addLayout(self.button_allignment)
        
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.v_layout)
        
        self.setCentralWidget(self.central_widget)

        self.search_btn.clicked.connect(self.call_forecast_window)
        
    def get_input_info(self, city, country_code):
        # transforms user's input into strings
        city = self.city_name.text()
        country_code = self.country_code.text()
        
        if handle_user_input.handle_missing_inputs(city, country_code):
            return None
        
        if handle_user_input.handle_country_code_mistypes(country_code):
            return None
            
        self.forecast_result = self.weather_forecast.get_and_send_data_from_api(city, country_code)
        
        # if forecast_result returns None, it means that data was not found
        if handle_user_input.handle_no_data_found_error(self.forecast_result):
            return None
        
        return self.forecast_result
    
    def call_forecast_window(self):
        # obtains info given by user into string and verifies if input_info is not None
        input_info = self.get_input_info(self.city_name.text(), self.country_code.text())
    
        if input_info is not None:
            self.forecast_window = Forecast_window(input_info)
            self.forecast_window.show()

if __name__ == "__main__":
    app = QApplication()
    win = Main()
    win.show()
    app.exec()
