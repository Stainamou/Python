import requests

vastaus = requests.get("https://api.chucknorris.io/jokes/random")
print(vastaus.json()["value"])
