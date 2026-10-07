alder = 31
aldersgrense = 18
navn = "Michael"
antall_studenter = 30

# Jeg tror svaret blir: True, fordi 31 er større enn 18.
print(alder > aldersgrense)

# Jeg tror svaret blir: True, den er lik.
print(alder == 31)

#Jeg tror svaret blir: True, fordi alder og aldersgrense ikke er like.
print(alder != aldersgrense)

#Jeg tror svaret blir: False, fordi aldersgrensen er ikke mindre enn eller lik 31.
print(alder <= aldersgrense)

#Jeg tror svaret blir: True, fordi den stemmer med variabelen.
print(navn == "Michael")

#Jeg tror svaret blir: False, fordi de ikke er helt like, Micheal har stor M og michael har liten m.
print(navn == "michael")

#Jeg tror svaret blir: True, fordi det er mer eller lik 30.
print(antall_studenter >= 30)

#Jeg tror svaret blir: True, fordi alder + 5 er 36, som er større enn 30.
print(alder + 5 > antall_studenter)

#---Refleksjon---
# Uttrykk 5 og 6 er nesten like og gir ulikt svar. Det er fordi de skal være helt like for å gi True.
# = brukes for å tilordne en verdi til en variabel, mens == brukes for å sammenligne to verdier, sjekke om verdien til venstre er lik verdien til høyre.
# True og False, Kan brukes til å sjekke om noe er sant eller usant, kan ta beslutninger, en ting skjer hvis det er sant, en annen ting skjer hvis det er usant. Brukes til å sammenligne ting.