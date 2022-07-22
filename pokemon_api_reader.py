import requests
import pandas as pd
import json
import csv


url = ('https://pokeapi.co/api/v2/pokemon/')
response = requests.get(url)
pokemon_info = []
all_data = response.json()
for x in range(1,151):
    new_url = f'{url}{x}'
    pokemon = requests.get(new_url)
    pokemon = pokemon.json()
    pokemon_info.append({'name': pokemon['name'], 'id':pokemon['id'], 'height':pokemon['height'],
    'weight': pokemon['weight'], 'type':(pokemon['types'][0]['type']['name']), 'sprite url':pokemon['sprites']['other']['official-artwork']['front_default']})


with open('pokemon_info.csv', 'w', encoding='utf8', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=pokemon_info[0].keys())

    dict_writer.writeheader()
    dict_writer.writerows(pokemon_info)

# url = ('https://pokeapi.co/api/v2/pokemon/')
# response = requests.get(url)
# pokemon_info = []
# all_data = response.json()
# for x in range(1,2):
#     new_url = f'{url}{x}'
#     pokemon = requests.get(new_url)
#     pokemon = pokemon.json()
#     sprite = pokemon['sprites']['other']['official-artwork']['front_default']
#     print(sprite)