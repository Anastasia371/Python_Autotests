import requests


token = 'fbd733bd6826586465de956a94dda933'
host = 'https://pokemonbattle.me:9104'


create_poke = requests.post(f'{host}/pokemons', json = {
    "name": "generate",
    "photo": "generate"
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print (create_poke.status_code, create_poke.text)

if create_poke.status_code == 201:
    print('Все ок!')
else:
    print('Что-то не так...')



change_poke_name = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "12554",
    "name": "Fitzwilliam",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print (change_poke_name.status_code, change_poke_name.text)



pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "12554"
}, headers = {"Content-Type" : "application/json", "trainer_token" : token})

print (pokeball.status_code, pokeball.text)



