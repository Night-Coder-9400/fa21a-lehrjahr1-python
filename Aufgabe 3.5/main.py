################### Aufgabe 3.5b):



#minuten = 1000 % 60
#stunden = 1000 // 60

#print("1000 Minuten nach Mitternacht sind: ", stunden,":",minuten, "Uhr")


#################### Aufgabe 3.5c):


#gibMinutenEin = int(input("Geben sie Minuten ein: "))

#minuten = gibMinutenEin % 60
#stunden = gibMinutenEin // 60

#print(gibMinutenEin, "Minuten nach Mitternacht sind: ", stunden,":",minuten, "Uhr")



#################### Aufgabe 3.5d):

#montag = 3
#dienstag = 4
#mittwoch = 5
#donnerstag = 6
#freitag = 7
#samstag = 1
#sonntag = 2

#tag23= 23%7
#tag200=200%7

#print("Tag 23 ist:", tag23, "Tag 200 ist:", tag200)


#################### Aufgabe 3.5e):




#gibEinenBetragEin = int(input("Gewünschter Betrag: "))

#auszahlung50Euro = gibEinenBetragEin//50
#auszahlung20Euro = (gibEinenBetragEin - (auszahlung50Euro * 50)) // 20

#restBetrag1 = gibEinenBetragEin - (auszahlung50Euro * 50)
#auszahlung10Euro = (restBetrag1 - (auszahlung20Euro * 20)) // 10

#restBetrag2 = restBetrag1 - (auszahlung20Euro * 20)
#auszahlung5Euro = (restBetrag2 - (auszahlung10Euro * 10)) // 5

#restBetrag3 = restBetrag2 - (auszahlung10Euro * 10)
#auszahlung2Euro = (restBetrag3 - (auszahlung5Euro * 5)) // 2

#restBetrag4 = restBetrag3 - (auszahlung5Euro * 5)
#auszahlung1Euro = (restBetrag4 - (auszahlung2Euro * 2)) // 1

#print("Auszahlung erfolgt als")
#print("50-Euro-Scheine: ", auszahlung50Euro)
#print("20-Euro-Scheine: ", auszahlung20Euro)
#print("10-Euro-Scheine: ", auszahlung10Euro)
#print("5-Euro-Scheine: ", auszahlung5Euro)
#print("2-Euro-Münzen: ", auszahlung2Euro)
#print("1-Euro-Münzen: ", auszahlung1Euro)




#################### Aufgabe 3.5f):

zuZahlenderBetrag = float(input("Zu zahlender Betrag: "))
gezahlterBetrag = float(input("Gezahlter Betrag: "))
wechselgeld = round(gezahlterBetrag-zuZahlenderBetrag,2)
print("Wechselgeld:", wechselgeld,"€")


auszahlung50Euro = wechselgeld//50
auszahlung20Euro = (wechselgeld - (auszahlung50Euro * 50)) // 20

#restBetrag1 = gibEinenBetragEin - (auszahlung50Euro * 50)
#auszahlung10Euro = (restBetrag1 - (auszahlung20Euro * 20)) // 10

#restBetrag2 = restBetrag1 - (auszahlung20Euro * 20)
#auszahlung5Euro = (restBetrag2 - (auszahlung10Euro * 10)) // 5

#restBetrag3 = restBetrag2 - (auszahlung10Euro * 10)
#auszahlung2Euro = (restBetrag3 - (auszahlung5Euro * 5)) // 2

#restBetrag4 = restBetrag3 - (auszahlung5Euro * 5)
#auszahlung1Euro = (restBetrag4 - (auszahlung2Euro * 2)) // 1

print("Das Wechselgeld wird ausgezahlt als")
print("50-Euro-Scheine: ", int(auszahlung50Euro))
print("20-Euro-Scheine: ", int(auszahlung20Euro))
#print("10-Euro-Scheine: ", auszahlung10Euro)
#print("5-Euro-Scheine: ", auszahlung5Euro)
#print("2-Euro-Münzen: ", auszahlung2Euro)
#print("1-Euro-Münzen: ", auszahlung1Euro)
