syöte = input("Syötä numero: ")
if syöte == "":
    print("Numeroita ei havaittu.")
else:
    pienin = int(syöte)
    suurin = pienin

while True:

    syöte2 = input("Syötä seuraava numero: ")
    if syöte2 == "":
        break
    numero = int(syöte2)

    if numero < pienin:
        pienin = numero
    if numero > suurin:
        suurin = numero

print("Suurin numero on:", suurin)
print("Pienin numero on:", pienin)
