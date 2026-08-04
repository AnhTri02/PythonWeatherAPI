import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)

from PyQt5.QtCore import Qt

#Class WeatherApp that inherits QWidget
class WeatherApp(QWidget):
  def __init__(self):
    super().__init__()
    self.city_label = QLabel("Enter city name", self)
    self.city_input = QLineEdit(self)
    self.get_weather_button =QPushButton("Get weather",self)
    self.temperature_label = QLabel(self)
    self.emoji_label = QLabel(self)
    self.description_label = QLabel(self)
    self.initUI()
    
  def initUI(self):
  
    self.setWindowTitle("Weather App") #calling inherited method from QWidget
    
    vbox = QVBoxLayout()
    
    widgets = [
      self.city_label,
      self.city_input,
      self.get_weather_button,
      self.temperature_label,
      self.description_label
      ]
    
    for i in widgets:
      vbox.addWidget(i)

  
    self.setLayout(vbox)
    
    self.city_label.setAlignment(Qt.AlignCenter)
    self.temperature_label.setAlignment(Qt.AlignCenter)
    self.description_label.setAlignment(Qt.AlignCenter)
    
    self.city_label.setObjectName("city_label")
    self.city_input.setObjectName("city_input")
    self.get_weather_button.setObjectName("get_weather_button")
    self.temperature_label.setObjectName("temperature_label")
    self.description_label.setObjectName("description_label")
    
    self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)
    self.get_weather_button.clicked.connect(self.get_weather)        
        
  def get_weather(self):
    api_key = "2950f7e9bcc56b918f8ab9152c3a02ea"
    city = self.city_input.text()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    
    response = requests.get(url) #response object
    data = response.json()
    print(data)
    
    
  
  def display_error(self):
      pass
  
  def display_weather(self):
      pass
  
  
    
if __name__ =="__main__":
  app = QApplication(sys.argv)
  weather_app = WeatherApp() # constructed Weatherapp object
  weather_app.show() #Showing it
  sys.exit(app.exec_()) #Makes window stay until close