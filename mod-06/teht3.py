#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain
# nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa
# sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista
# jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.

def bensiini(gallon):
    litraa_per_gallon = gallon * 3.785
    print(f"{gallon} gallonia bensiiniä on {litraa_per_gallon} litraa bensiiniä)
    return litraa_per_gallon

gallon = int(input("Anna gallonamäärä: "))

while gallon > 0:
    bensiini(gallon)
    break
else:
    print("Anna positiivinen luku")


