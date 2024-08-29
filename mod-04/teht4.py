import random

oikea_luku = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa numero: "))

    if arvaus < oikea_luku:
        print("Liian pieni arvaus")
    if arvaus > oikea_luku:
        print("Liian iso arvaus")
    if arvaus == oikea_luku:
        print("Oikein")
        break