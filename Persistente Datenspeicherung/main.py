import time
verkaufsListe = []
file = open("D:\SD2\Persistente Datenspeicherung\Verkaufsdaten.txt","a")
today = time.strftime("%d.%m.%Y %H:%M:%S")
abbruch = 0

while(abbruch == 0):
    verkauftesProdukt = input("Name des verkauften Produkts: ")
    nettoPreis = input("Netto Preis des Produkts: ")
    verkaufsListe = "Datum: " +str(today) + " | Produkt: " + str(verkauftesProdukt) + " | Preis: " + str(nettoPreis) + "\n"
    file.write(verkaufsListe)
    abbruch = int(input("Abbruch? "))
file.close()


