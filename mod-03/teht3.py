kysely1 = input("Oletko nainen vai mies?: ")
kysely2 = int(input("Kerro hemoglobiiniarvosi: "))

if kysely1 == "mies":
    if kysely2 < 134:
        print("Hemoglobiinisi on liian alhainen")
    elif 134 <= kysely2 <= 195:
        print("Hemoglobiinisi on normaali")
    else:
        print("Hemoglobiinisi on liian korkea")

if kysely1 == "nainen":
    if kysely2 < 117:
        print("Hemoglobiinisi on liian alhainen")
    elif 117 <= kysely2 <= 175:
        print("Hemoglobiinisi on normaali")
    else:
        print("Hemoglobiinisi on liian korkea")




