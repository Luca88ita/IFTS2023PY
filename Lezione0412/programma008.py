# scrivere una classe fraction per rappresentare numeri razionali come 1/2 e -3/8
# le frazioni dovrebbero essere salvate in forma ridotta (4/12 => 1/3) (6/-9 => -2/3)
# una funzione MCD mi torna il massimo comune divisore
# definire a funzione add e multiply che accetta un'altra fraction e modifichi la frazione corrente aggiungendo ad essa/moltiplicandola
# definire gli operatori +,*,==,<

""" import math


class Fraction:
    mcd = 1

    def __init__(self, numeratore, denominatore):
        if denominatore < 0:
            self.numeratore = -numeratore
            self.denominatore = -denominatore
        elif denominatore == 0:
            raise ValueError("Non è possibile dividere per 0")
        else:
            self.numeratore = numeratore
            self.denominatore = denominatore
        self.MCD()

    def MCD(self):

        mcd = math.gcd(self.numeratore, self.denominatore)
        print(mcd)

        self.numeratore = int(self.numeratore/mcd)
        self.denominatore = int(self.denominatore/mcd)

    def __str__(self):
        if self.denominatore == 1:
            return (f"{self.numeratore}")
        else:
            return (f"{self.numeratore}/{self.denominatore}")

    def __mul__(self, other):
        numeratore = self.numeratore * other.numeratore
        denominatore = self.denominatore * other.denominatore


a = Fraction(-100, -10)
print(a)
 """
