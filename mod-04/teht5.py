käyttis = "python"
salis = "rules"

yritykset = 0
max_yritykset = 5

while yritykset < max_yritykset:
    käyttäjätunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if käyttis == käyttäjätunnus and salis == salasana:
        print("Tervetuloa")
        break

    else:
        yritykset += 1
        print("Pääsy evätty")

