kuukausi = int(input("Anna kuukauden numero (1-12): "))

vuodenajat = ("talvi", "kevät", "kesä", "syksy")
(talvi, kevät, kesä, syksy) = vuodenajat

if kuukausi == 12 or kuukausi == 1 or kuukausi == 2:
    print (f"{kuukausi}. kuukausi on {talvi} kuukausi")
elif kuukausi == 3 or kuukausi == 4 or kuukausi == 5:
    print (f"{kuukausi}. kuukausi on {kevät} kuukausi")
elif kuukausi == 6 or kuukausi == 7 or kuukausi == 8:
    print (f"{kuukausi}. kuukausi on {kesä} kuukausi")
elif kuukausi == 9 or kuukausi == 10 or kuukausi == 11:
    print (f"{kuukausi}. kuukausi on {syksy} kuukausi")
else:
    print("Virheellinen syöte")