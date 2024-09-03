numerot = []

syöte = input("Anna luku: ")
numerot.append(syöte)

while syöte != "":
    syöte = input("Anna seuraava luku: ")
    numerot.append(syöte)
    numerot.sort(reverse=True)
print(numerot[:5])
