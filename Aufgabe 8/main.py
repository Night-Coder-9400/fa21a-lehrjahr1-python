# Aufgabe 8.4 Erweiterung
#----------------------------------------------------------------------
"""
import statistics
besucherzahl = []
i = 0
median = 0

while(i < 6):
    eingabe =  int(input("Gib hier die Besucherzahlen ein: "))
    besucherzahl.append(eingabe)
    i+=1

print("Geringste Besucherzahl: ", min(besucherzahl))
print("Höchste Besucherzahl: ", max(besucherzahl))
print("Durchschnittliche Besucherzahl: ", sum(besucherzahl)//len(besucherzahl))
print("Median der Besucherzahlen: ", statistics.median(besucherzahl))

list.sort(besucherzahl)

median = (besucherzahl[2]+besucherzahl[3])//2
print("\n","Der Median beträgt: ", median)

print("\n" , besucherzahl)

#-------------------------------------------------------------------
#-------------------------------------------------------------------

#Aufgabe 8.5 Übungen
#A)
#-------------------------------------------------------------------

Auswertung = ["sehr schlechte Fitness", "schlechte Fitness", "durchschnittliche Fitness", "gute Fitness", "sehr gute Fitness"]
punktewert_eingabe =  int(input("Gib hier deinen erhaltenen Punktewert (0-4) ein: "))
print("Deine Fitness Auswertung lautet:", Auswertung[punktewert_eingabe])

#B)
#-------------------------------------------------------------------
i = 1
tag = int(input("Gib hier an, an wie vielen Tagen du gewandert bist: "))
WanderungKM = []
WanderungZeit = []
zeit=[]

while (i <= tag):
    streckeInKM = int(input("Gib hier die gewanderte Strecke in km ein: "))
    WanderungKM.append(streckeInKM)
    zeit = input("Gib hier die gewanderte Zeit ein (00:00): ")
    WanderungZeit.append(zeit)
    i+=1

if(WanderungZeit[0]=="0"):
    zeitM=int(WanderungZeit[3]+WanderungZeit[4])
    zeitH=int(WanderungZeit[1])
    minuten = (zeitH * 60) + zeitM
    zeit.append(minuten)
else:
    zeitM=int(WanderungZeit[3]+WanderungZeit[4])
    zeitH=int(WanderungZeit[0]+WanderungZeit[1])
    minuten = (zeitH * 60) + zeitM
    zeit.append(minuten)minuten = (zeitH * 60) + zeitM


print("Gewanderte km pro Tag:", WanderungKM, "\n","Gewanderte Zeit pro Tag:", WanderungZeit)

print("Durchschnittliche gewanderte Strecke pro Tag in km: ",round(sum(WanderungKM)/len(WanderungKM)))
print("Durchschnittsgeschwindigkeit hh:mm: ",sum(WanderungZeit)/len(WanderungZeit))
"""

lstrecke = list()
lzeit = list()
lwanderer = list()
x = 0
y = int(input("Wie viele Tage? "))
z = int(input("Wie viele Wanderer? "))

while(x < z):

    while(x < y):

        strecke = int(input("Strecke in km: "))
        zeit = input("benötigte Zeit (hh:mm): ")


        if zeit[0] == "0":
            mzeit = int(zeit[3] + zeit[4])
            hzeit = int(zeit[1])
            minuten = (hzeit * 60) + mzeit
            lzeit.append(minuten)
        else:
            mzeit = int(zeit[3] + zeit[4])
            hzeit = int(zeit[0] + zeit[1])
            minuten = (hzeit * 60) + mzeit
            lzeit.append(minuten)

        lstrecke.append(strecke)
        x = x+1

        streckenschnitt = sum(lstrecke) / len(lstrecke)
        zeitschnitt = (sum(lzeit) / len(lzeit)) / 60
        speed = round(streckenschnitt / zeitschnitt, 2)

        print("Du läufst pro Tag durchschnittlich " + str(round(streckenschnitt, 2)) + " km, deine Durchschnittgeschwindigkeit beträgt damit " + str(speed) + " km/h.")

print("Wanderer X ist schneller: ")
#-------------------------------------------------------------------
#-------------------------------------------------------------------
