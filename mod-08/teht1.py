import mysql.connector

def lentokenttä_ja_sijainti(icao):
    sql = f"SELECT name, municipality FROM airport where ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Hakemanne lentokenttä ICAO-koodilla {icao_koodi} on {rivi[0]} "
                  f"sijaintikunnassa {rivi[1]}")
    else:
        print(f"Lentokenttää ICAO-koodilla {icao} ei löytynyt")
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='stenukka',
         password='bombastic',
         autocommit=True,
         )

icao_koodi = input("Anna lentokentän ICAO-koodi: ").upper()
lentokenttä_ja_sijainti(icao_koodi)
