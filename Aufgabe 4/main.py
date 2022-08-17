bewerbernr = int(input("Bewerbernr: "))
print("Bewerbernummer: ", str(bewerbernr))

vorname = input("Vorname: ")
print("Vorname: ", vorname)

nachname = input("Nachname: ")
print("Nachname: ", nachname)

geschlecht = input("Geshclecht: ")
print("Geschlecht: ", geschlecht)

strasse = input("Straße: ")
print("Straße: ", strasse)

hausnr = input("Hausnummer: ")
print("Hausnummer: ", hausnr)

plz = input("Postleitzahl: ")
print("Postleitzahl: ", plz)

stadt = input("Stadt: ")
print("Stadt: ", stadt)

geburtsdatum = input("Geburtsdatum: ")
print("Geburtsdatum: ", geburtsdatum)

gehaltsvorstellung = float(input("Gehaltsvorstellung: "))
print("Gehaltvorstellung: ", str(gehaltsvorstellung))

vorstrafen = bool(input("Vorstrafen: "))
print("Vorstrafen: ", str(vorstrafen))

############  Eingabe (modifizierte Version unserer Lösung für Abschnitt 2):

bewerbernummer = int(input("Bewerbernummer: "))
name = input("Name: ")
vorname = input("Vorname: ")
geschlecht = input("Geschlecht: ")
strasse = input("Straße: ")
hausnr = input("Hausnummer: ")
plz = input("PLZ: ")
stadt = input("Stadt: ")
alter = int(input("Alter: "))     #  Abweichung zu Abschnitt 2
gehaltsvorstellung = round(float(input("Gehaltsvorstellung: ")), 2)
vorbestraft = input("Vorstrafen? (J/N): ")


"""############ Überprüfen der Bedingungen:

# Bedingung 1: vorbestraft? (ja/nein)?

# Bedingung 2: jünger als 50? (ja/nein)?

# Bedingung 3: kommt aus PLZ-Regionen 40, 42, 45, 46, 47, 48, 58 oder 59 (ja/nein)?

"""




##########  Ausgabe (muss gemäß der Aufgabenstellung noch erweitert werden):

print("Die Bewerbernummer lautet ", bewerbernummer)
print("Name: ", name)
print("Vorname: ", vorname)
print("Geschlecht: ", geschlecht)
print("Straße: ", strasse)
print("Hausnummer: ", hausnr)
print("Postleitzahl: ", plz)
print("Stadt: ", stadt)
print("Alter: ", alter)
print("Gehaltsvorstellung: ", gehaltsvorstellung)
print("Vorstrafen?", vorbestraft)




if vorstrafen:
    print("Kein geeigneter Bewerber, da Vorstrafen vorhanden sind.")

if alter <= 50:
    print("Kein geeigneter Bewerber, da der Bewerber zu alt ist.")

if plz.startswith('40' or '42' or '45' or '46' or '47' or '48' or '58' or '59'):
   print("Kein geeigneter Bewerber, da der Bewerber zu alt ist.")
