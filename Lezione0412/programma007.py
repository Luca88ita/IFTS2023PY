# classi, oggetti, ereditaditarietà

class Fumetto:
    # titolo = "fumetto"
    __titolo__ = "Fumetto"

    def __init__(self, titolo, prezzo):
        self.titolo = titolo
        self.prezzo = prezzo
        self.Leggimi()

    def Leggimi(self):
        print(f"leggo il fumetto {self.titolo}")

    def Buttami(self):
        print(f"hai buttato il fumetto {self.titolo}")

    def Acquistami(self, quantita):
        prezzo = quantita*self.prezzo
        print(prezzo)

    def __str__(self):
        return f"{self.titolo} - prezzo: {self.prezzo}"


# questo sarebbe da evitare, così da tener visibile la funzione solo tramite l'utilizzo della classe
def Acquistami(self, quantita):
    prezzo = quantita*5
    print(prezzo)


# questo sarebbe da evitare, così da tener visibile la funzione solo tramite l'utilizzo della classe
Fumetto.Acquistami = Acquistami


f = Fumetto("Sanpei", 3.99)
f.Leggimi()
print(f.__titolo__)
f.Acquistami(4)
Acquistami(f, 3)

print(f)
