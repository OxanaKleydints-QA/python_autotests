import requests

token = '10184474b778628c79b040e45f6e8a57'


add_pokemon_response = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = 
                                     {
    "name": "Oxxxi",
    "photo": "https://dolnikov.ru/pokemons/albums/916.png"
}, headers = {"Content-Type" : 'application/json', 
             "trainer_token" : token})                                  

print(add_pokemon_response.text)


change_pokemon_response = requests.put('https://api.pokemonbattle.me:9104/pokemons', json =
                                       {
    "pokemon_id": "13878",
    "name": "Oxxxi",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {"Content-Type" : 'application/json', 
             "trainer_token" : token})                                  

print(change_pokemon_response.text)


catch_pokemon_response = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json = 
                                     
    {
    "pokemon_id": "13878"
}
, headers = {"Content-Type" : 'application/json', 
             "trainer_token" : token})                                  

print(catch_pokemon_response.text)

