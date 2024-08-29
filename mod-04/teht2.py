cm = 2.54

while True:

    tuuma = int(input("Syötä tuumat: "))
    if convert < 0:
        print("Tuumien määrä on negatiivinen. Ohjelma lopetetaan.")
        break

    conversion = convert * cm
    print(f"{tuuma} tuumaa on {conversion:.2f} senttimetriä")


