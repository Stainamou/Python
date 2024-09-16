import mysql.connector

def lentokenttä_lukumäärä(maakoodi):
    sql = f"SELECT type, COUNT(*) as count FROM airport where iso_country='{maakoodi}' GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for i in tulos:
            print(f"Maakoodissa {maakoodi} on {i[0]}: {i[1]} kpl")


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='stenukka',
         password='bombastic',
         autocommit=True,
         )

maakoodi = input("Anna maakoodi (esim. FI): ").upper()
lentokenttä_lukumäärä(maakoodi)