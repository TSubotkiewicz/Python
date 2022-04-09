from urllib import response
import requests
from pprint import pprint

response = requests.get("https://hp-api.herokuapp.com/api/characters")
data = response.json()

print('Co chciał/-a byś zobaczyć?')
print('1. Postacie z określonym kolorem oczy? ')
print('2. Postacie z określonym "species"? ')
option = input('Podaj swój wybór: ')
if option == '1':
    eye_colour = input("Podaj kolor oczu: ")
    pprint([char for char in data if char.get('eyeColour') == eye_colour])
elif option == '2':
    species = input("Podaj species: ")
    pprint([char for char in data if char.get('species') == species])
