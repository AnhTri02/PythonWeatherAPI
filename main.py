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
    api_key = "2950f7e9bcc56b918f8ab9152c3a02ea" #yes I know my api key is public :)
    city = self.city_input.text()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url) #response object
        response.raise_for_status()
        data = response.json()
        
        if data["cod"] == 200:
            self.display_weather(data)
    except requests.exceptions.HTTPError as http_error:
        match response.status_code:
            case 400:
                self.display_error("Error code 400: Bad request \n Please check your input")
            case 401:
                self.display_error("Error code 401: Unauthorized:\nInvalid API key")
            case 403:
                self.display_error("Error code 403: Forbidden:\nAccess is denied")
            case 404:
                self.display_error("Error code 404: Not found:\nCity not found")
            case 500:
                self.display_error("Error code 500: Internal Server Error:\nPlease try again later")
            case 502:
                self.display_error("Error code 502: Bad Gateway:\nInvalid response from the server")
            case 503:
                self.display_error("Error code 503: Service Unavailable:\nServer is down")
            case 504:
                self.display_error("Error code 504: Gateway Timeout:\nNo response from the server")
            case _:
                self.display_error(f"Error code ?: HTTP error occurred:\n{http_error}")     
            
    except requests.exceptions.ConnectionError:
        print("Connection Error \n Check your internet connection")
    except requests.exceptions.Timeout:
        print("Timeout Error \n The request timed out")
    except requests.exceptions.TooManyRedirects:
        print("Too many redirects \n check the url")
    except requests.exceptions.RequestException as req_error:
        print(f"Request error:\n {req_error}")
    
        
    
    
  
  def display_error(self, message):
      self.temperature_label.setText(message)
  
  def display_weather(self,data):
      print(data)
  
  
    
if __name__ =="__main__":
  app = QApplication(sys.argv)
  weather_app = WeatherApp() # constructed Weatherapp object
  weather_app.show() #Showing it
  sys.exit(app.exec_()) #Makes window stay until close