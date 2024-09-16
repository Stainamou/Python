import mysql.connector
from geopy.distance import geodesic

icao1 = input("Anna ensimmäinen ICAO-koodi: ").upper()
icao2 = input("Anna toinen ICAO-koodi: ").upper()

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='stenukka',
         password='bombastic',
         autocommit=True,
         )

def koordinaatit(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport where ident = %s "
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()
    if tulos:
        return tulos
    else:
        print(f"Lentokenttää ICAO-koodilla {icao} ei löytynyt.")
        return None

def laske_etäisyys(icao1, icao2):
    koordinaatit1 = koordinaatit(icao1)
    koordinaatit2 = koordinaatit(icao2)
    if koordinaatit1 and koordinaatit2:
        etäisyys = geodesic(koordinaatit1, koordinaatit2).kilometers
        print(f"Lentokenttien {icao1} ja {icao2} välinen etäisyys on {etäisyys:.2f} kilometriä.")
    else:
        print("Etäisyyden laskeminen epäonnistui.")

laske_etäisyys(icao1, icao2)
