# Leonardi Manon

import requests
from pprint import pprint

contenu = requests.get("http://api.open-notify.org/astros.json")
for personne in contenu.json()["people"]:
    if personne["craft"] == "ISS":
        print(personne)