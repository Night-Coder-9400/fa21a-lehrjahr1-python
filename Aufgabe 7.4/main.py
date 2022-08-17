# Aufgabe 7.4 a)


#passwort = "12345"

#for i in range(0,3):
#    passwort_eingabe = input("Geben Sie ein Passwort ein oder 'Nixdorf' für Ende: ")

#    if passwort_eingabe == "Nixdorf":
#        print("Eingabe beendet!")
#        break
#    elif passwort_eingabe == passwort:
#        print("Passwort richtig!")
#        break
#    elif passwort_eingabe != passwort:
#            print("Passwort falsch!")

#if passwort_eingabe != passwort:
#    print("Programm beendet nach 3 falschen Passwort eingaben")

#else:
#    print("")




# Aufgabe b)

land_a = 60000000
land_b = 4000000
jahre = 0

erreicht = False

while not erreicht:
    jahre += 1
    land_a = land_a * 0.995
    land_b = land_b * 1.025
    print("Nach " + str(jahre) + " Jahren hat Land A " + str(round(land_a, 2)) + " Einwohner")
    if land_b >= land_a:
        erreicht = True
