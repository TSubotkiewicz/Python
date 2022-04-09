import requests

url = "https://api.weatherapi.com/v1/current.json"

print('Pogoda z https://www.weatherapi.com/')
miasto = input('Podaj angielską nazwe kraju i miasta które chcesz sprawdzić, np. Poland/Krakow: ')
querystring = {"key": "432b886f0fdb4eb49be201022220904", "q": miasto, "aqi": "yes", "lang": "pl" }
response = requests.request("GET", url, params=querystring)
if response.ok:
    data = (response.json())
    print('Kraj: ' + data['location']['country'])
    print('Miasto: ' + data['location']['name'])
    print('Czas lokalny: ' + data['location']['localtime'])
    print('Pogoda: ' + data['current']['condition']['text'])
    print('Temperatura: ', data['current']['temp_c'], 'stopni C')
    print('Temperatura odczuwalna: ', data['current']['feelslike_c'], 'stopni C')
    print('Ciśnienie: ', data['current']['pressure_mb'], 'hPa')
    print('Wilgotność: ', data['current']['humidity'], '%')
    print('Prędkość wiatru: ', data['current']['wind_kph'], 'km/h')
    print('Kierunek wiatru: ' + data['current']['wind_dir'])
else:
    print("Nie znaleziono takiego miasta")
