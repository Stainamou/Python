import random

pistemäärä = int(input("Anna pistemäärä: "))

if pistemäärä <= 0:
    print("Pistemäärän pitää olla positiivinen")
else:
    ympyrässä = 0

for i in range(pistemäärä):

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= 1:
        ympyrässä += 1

pi_likiarvo = 4 * ympyrässä / pistemäärä

print("Piin likiarvo annetulla arvolla on ", pi_likiarvo)
