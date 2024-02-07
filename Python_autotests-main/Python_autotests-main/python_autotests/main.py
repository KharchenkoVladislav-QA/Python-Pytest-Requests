"""
Kolorado test API
"""

import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json', 
'trainer_token':'93200da72bbd14197c15946a94f956da'}

#Создание покемона#

body = {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print (f'Результат выполнения запроса: {response.text}') 


#Поймать покемона в покебол#

body = {
    "pokemon_id": "28305"
}
response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER, timeout=5)
print (f'Результат выполнения запроса: {response.text}') 


#Смена имени покемона#

body = {
    "pokemon_id": "28305",
    "name": "Evan",
}
response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER, timeout=5)
print (f'смена имени: {response.text}') 