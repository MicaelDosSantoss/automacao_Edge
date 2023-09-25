import requests
import json


api = 'https://pokeapi.co/api/v2/pokedex/1/'

get = requests.get(api)

pokedex_json = get.json()

poke_list = []

for pok in pokedex_json['pokemon_entries']:
    pok_name = pok['pokemon_species']['name']
    poke_list.append(pok_name)

#  with - relacionamente de recursos
# open() - abrir arquivo
with open('pokemon.json','w') as pokedex_json:
    json.dump(poke_list,pokedex_json,indent=2)
