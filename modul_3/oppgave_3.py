brus = 24.90
smørbrød = 45
banan = 8.50

totalsum = brus + smørbrød + banan
print( "Totalsum:", totalsum)

totalsum_mva = totalsum * 1.25
print("Totalsum med mva:", totalsum_mva)

pris = totalsum_mva / 4
print("Pris per person dersom 4 personer deler regningen likt:", pris)

prisforskjell = smørbrød - banan
print("Prisforskjellen mellom den dyreste og billigste varen er:", prisforskjell)

#---Refleksjon---
# Når jeg la sammen heltall og desimaltall fikk jeg desimaltall, en float som resultat og datatype.
# Datatypen ble float når jeg delte på 4. 
# Det er en fordel å bruke variabler når man skal bruke samme tall flere ganger, slipper å skrive det inn flere ganger og lete etter det senere. Også lettere å endre tallene senere, da man bare trenger å endre i variabelen. En variabel forklarer betydningen av tallet. Mindre risiko for tastefeil.