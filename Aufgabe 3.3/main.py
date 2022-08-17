weinname = input("Bitte geben Sie einen Weinnamen ein: ")
preisProFlasche = float(input("Geben Sie einen Preis pro Flasche ein: "))
anzahlDerBestelltenFlaschen = int(input("Geben Sie die Anzahl der bestellten Flaschen ein: "))

bruttoPreis = round(preisProFlasche*anzahlDerBestelltenFlaschen, 2)
nettoPreis = round(bruttoPreis/100*81, 2)
anzahlKartons = anzahlDerBestelltenFlaschen//6
mehrKartons = anzahlDerBestelltenFlaschen % 6
if mehrKartons > 0:
    anzahlKartons += 1

print("Zusammenfassung der Bestellung: " + weinname + ", " + str(anzahlDerBestelltenFlaschen) + " Stück")
print("Gesamtpreis: " + "brutto:" + str(bruttoPreis) + ", netto: " + str(nettoPreis))
print("Anzahl nötiger Kartons " + str(anzahlKartons))


##OHNE IF

weinname = input("Bitte geben Sie einen Weinnamen ein: ")
preisProFlasche = float(input("Geben Sie einen Preis pro Flasche ein: "))
anzahlDerBestelltenFlaschen = int(input("Geben Sie die Anzahl der bestellten Flaschen ein: "))

bruttoPreis = round(preisProFlasche*anzahlDerBestelltenFlaschen,2)
nettoPreis = round(bruttoPreis/100*81, 2)
anzahlKartons = (anzahlDerBestelltenFlaschen+5)//6


print("Zusammenfassung der Bestellung: " + weinname + ", " + str(anzahlDerBestelltenFlaschen) + " Stück")
print("Gesamtpreis: " + "brutto:" + str(bruttoPreis) + ", netto: " + str(nettoPreis))
print("Anzahl nötiger Kartons " + str(anzahlKartons))