monat = int(input("Bitte geben sie eine Zahl von 1-12 ein:"))

if monat == 1:
    print("Januar")
elif monat == 2:
    print("Febuar")
elif monat == 3:
    print("März")
elif monat == 4:
    print("April")
elif monat == 5:
    print("Mai")
elif monat == 6:
    print("Juni")
elif monat == 7:
    print("Juli")
elif monat == 8:
    print("August")
elif monat == 9:
    print("September")
elif monat == 10:
    print("Oktober")
elif monat == 11:
    print("November")
elif monat == 12:
    print("Dezember")
else:
    print("Keine gültiger Monat")

entfernung = int(input("Geben Sie die Entfernung ein: "))

"""
# i)
if entfernung > 30:
    print("Der Lieferpreis beträgt 30€")

# ii)
else:
    print("Der Lieferpreis beträgt 10€")

# iii)
if entfernung <= 30:
    print("Der Lieferpreis beträgt 10€")
elif entfernung > 30 and entfernung <= 70:
    print("Der Lieferpreis beträgt 30€")
elif entfernung > 70 and entfernung <= 100:
    print("Der Lieferpreis beträgt 50€")
else:
    print("Der Lieferpreis bträgt 100€")
"""

# iv)
kundentyp = input("Geben Sie den Kundentypen ein: ")
lieferpreis = 0.0

if entfernung <= 30:
    lieferpreis = 10.00
    print("Der Lieferpreis beträgt ", lieferpreis, "€")
    if kundentyp == "A":
        lieferpreis = lieferpreis - 10.00
        print("Der Lieferpreis beträgt ", lieferpreis, "€")
    elif kundentyp == "B":
        print("Der Lieferpreis beträgt ", lieferpreis, "€")
elif entfernung > 30 and entfernung <= 70:
    lieferpreis = 30.00
    print("Der Lieferpreis beträgt ", lieferpreis, "€")
elif entfernung > 70 and entfernung <= 100:
    lieferpreis = 50.00
    print("Der Lieferpreis beträgt ", lieferpreis, "€")
else:
    lieferpreis = 100.00
    print("Der Lieferpreis beträgt ", lieferpreis, "€")

#Aufgabe c)

zahl = int(input("Geben sie eine Zahl von 1-6: "))
if zahl == 1:
    print("-----\n|   |\n| * |\n|   |\n-----")
elif zahl == 2:
    print("-----\n|*  |\n|   |\n|  *|\n-----")
elif zahl == 3:
    print("-----\n|*  |\n| * |\n|  *|\n-----")
elif zahl == 4:
    print("-----\n|* *|\n| * |\n|* *|\n-----")
elif zahl == 5:
    print("-----\n|* *|\n| * |\n|* *|\n-----")
elif zahl == 6:
    print("-----\n|* *|\n|* *|\n|* *|\n-----")
else:
    print("-----\n|   |\n| ? |\n|   |\n-----")



