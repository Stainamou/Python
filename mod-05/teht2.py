# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää
# tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi
# suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden
# lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

numerot = []

syöte = input("Anna luku: ")
numerot.append(syöte)

while syöte != "":
    syöte = input("Anna seuraava luku: ")
    numerot.append(syöte)
    numerot.sort(reverse=True)
print(numerot[:5])
