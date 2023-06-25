import requests

token = '10184474b778628c79b040e45f6e8a57'


trainer_info = requests.get('https://api.pokemonbattle.me:9104/trainers', params = {'trainer_id': 4858})

print(trainer_info.status_code)



trainer_info = requests.get('https://api.pokemonbattle.me:9104/trainers', params = {'trainer_id': 4858})

print(trainer_info.text)



                                     