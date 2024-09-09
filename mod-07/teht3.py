lentoasemat = {}

haku = int(input("Valitse 1 jos haluat syöttää uuden lentoaseman, 2 jos haluat hakea jo syötetyn lentoaseman tai 3 jos haluat lopettaa: "))

while 1 <= haku <= 3:

    if haku == 1:
       icao = input("Syötä ICAO-koodi: ").upper()
       nimi = input("Syötä lentoaseman nimi: ")
       lentoasemat[icao] = nimi
       print(f"{nimi} lentoasema ICAO-koodilla {icao} on tallennettu")

    elif haku == 2:
        icao = input("Syötä ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoasema ICAO-koodilla {icao} on {lentoasemat[icao]}")
        else:
            print(f"Lentoasemaa ICAO-koodilla {icao} ei löydy")

    elif haku == 3:
        print("Ohjelma lopetetaan")
        break

    haku = int(input("Valitse 1 jos haluat syöttää uuden lentoaseman, 2 jos haluat hakea jo syötetyn lentoaseman tai 3 jos haluat lopettaa: "))




