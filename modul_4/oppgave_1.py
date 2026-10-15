navn = input("Hva heter du: ")
print("Hei,", navn)

print(f"Hei, {navn}!")

alder = input("Hvor gammel er du: ")
print(type(alder)) # Datatypen er string.

# print(alder + 1) # TypeError: can only concatenate str (not "int") to str.

alder = int(alder)
print(type(alder)) # Datatypen er blitt gjort om til integer.
print(f"Du blir {alder + 1} til neste år!")

#---Refleksjon---
# String var datatypen på alderen før jeg brukte int(). input gir string fordi
# I steg 5 klaget Python på at den ikke kan blande datatype str og int
# 
# 