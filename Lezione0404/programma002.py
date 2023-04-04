# from math import *
import math


def stampa_ripetuta(parola, numero=1, has_cornice=True):
    print(parola*numero, has_cornice)


stampa_ripetuta("Ciao")
stampa_ripetuta("Luca", 2)
# vado a specificare che voglio dargli solo il parametro obbligatorio e l'ultimo non obbligatorio
stampa_ripetuta("Ciao", has_cornice=False)

print(math.ceil(7.8567))

print(max(1, 5, 9, 85, 68, 47, 548, 25, 35))
print(min(1, 5, 9, 85, 68, 47, 548, 25, 35))


def coppia():
    return "Pippo", "Pluto"


a, b = coppia()
print(coppia())
print(a)
print(b)

print("\n"+"-"*20+"\n")  # ripeto la stringa

txt = input("Ciao, inserisci il tuo nome: ")


if txt == "mario rossi":
    print("benvenuto", txt)
else:
    print("vattene", txt)

while txt != "luca verdi":
    txt = input("utente non riconosciuto. Inserisci un utente valido: ")

if txt == "mario rossi":
    print("benvenuto", txt)
elif txt == "luca verdi":
    print("vattene!")
else:
    print("malvenuto")

print("\n"+"-"*20+"\n")  # ripeto la stringa

if 5 == 5 and 4 < 9:
    print("bravo1")
if 5 == 5 or 4 > 9:
    print("bravo2")
if not 5 == 5 and 4 < 9:
    print("bravo3")

print("\n"+"-"*20+"\n")  # ripeto la stringa

for lettera in "parola":
    print(lettera)

parola = "caramella alla fragola"
print(parola[0])
print(len(parola))

# stampare l'indice della lettera z
print(parola.find("z"))
# stampare l'indice della lettera a
print(parola.find("a"))  # mi torna la prima lettera a trovata

for i in range(len(parola)):
    if parola[i] == "a":
        print(i)
