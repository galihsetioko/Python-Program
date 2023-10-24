import argparse
import requests

class Mainstart():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--country', help="Berisi kode negara ( ex : Indonesia -> ID )", required=True)
    parser.add_argument('-t', '--town', help="Berisi nama kota ( ex : Jakarta )", required=True)
    args = parser.parse_args()
    with open('apikey/key', 'r') as file:
        key = file.read()
    
    def start(self):
        key = self.key
        self.country = self.args.country
        self.town = self.args.town
        self.geolocation(self.country, self.town, key)
        
        print('\tSource : openweather.com\n')

    def geolocation(self, country, town, key):
        url_geo = f'http://api.openweathermap.org/geo/1.0/direct?q={town},{country}&limit=1&appid={key}'
        r = requests.get(url_geo)
        j = r.json()
        self.getWeather(j[0]['lat'], j[0]['lon'], key)
        
    def getWeather(self, lat, lon, key):
        url_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'
        k = requests.get(url_weather)
        k_info = k.json()
        self.printInfo(weather_info=k_info)
    def toCelcius(self , var):
        return f"{var - 273:.1f}"
    def visibility(self , var):
        return f"{var // 1000:.1f}"
    def printInfo(self,weather_info):
        print(f'''
        Wilayah : {self.country}, {self.town}
        Kondisi Cuaca : {weather_info['weather'][0]['main']}, {weather_info['weather'][0]['description']}
        Terasa Seperti : {self.toCelcius(weather_info['main']['feels_like'])} Celcius
        Temperature : {self.toCelcius(weather_info['main']['temp'])} Celcius
        Jarak Pandang : {self.visibility(weather_info['visibility'])} Km
        Area : {weather_info['name']}
        ''')
        

if __name__ == "__main__":
    mainapp = Mainstart()
    mainapp.start()