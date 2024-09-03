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


