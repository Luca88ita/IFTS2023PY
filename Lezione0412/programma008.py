# scrivere una classe fraction per rappresentare numeri razionali come 1/2 e -3/8
# le frazioni dovrebbero essere salvate in forma ridotta (4/12 => 1/3) (6/-9 => -2/3)
# una funzione MCD mi torna il massimo comune divisore
# definire a funzione add e multiply che accetta un'altra fraction e modifichi la frazione corrente aggiungendo ad essa/moltiplicandola
# definire gli operatori +,*,==,<

import math


def MCD(num, den):  # massimo comune divisore
    mcd = math.gcd(int(num), int(den))
    num = int(num / mcd)
    den = int(den / mcd)
    return Fraction(num, den)


def mcm(den1, den2):  # minimo comune multiplo
    mcm = math.lcm(den1, den2)
    m1 = int(mcm / den1)
    m2 = int(mcm / den2)
    den = den1 * m1
    return m1, m2, den


class Fraction:
    def __init__(self, numeratore: float, denominatore=1.0):
        while numeratore % 1 > 0 or denominatore % 1 > 0:
            numeratore = numeratore * 10
            denominatore = denominatore * 10
        if denominatore < 0:
            self.numeratore = -numeratore
            self.denominatore = -denominatore
        elif denominatore == 0:
            raise ValueError("Non è possibile dividere per 0")
        else:
            self.numeratore = numeratore
            self.denominatore = denominatore

    def __str__(self):
        if self.denominatore == 1:
            return f"{self.numeratore}"
        return f"{self.numeratore}/{self.denominatore}"

    def __add__(self, other):
        mult1, mult2, denominatore = mcm(self.denominatore, other.denominatore)
        numeratore = (self.numeratore * mult1) + (other.numeratore * mult2)
        return MCD(numeratore, denominatore)

    def __sub__(self, other):
        mult1, mult2, denominatore = mcm(self.denominatore, other.denominatore)
        numeratore = (self.numeratore * mult1) - (other.numeratore * mult2)
        return MCD(numeratore, denominatore)

    def __mul__(self, other):
        numeratore = self.numeratore * other.numeratore
        denominatore = self.denominatore * other.denominatore
        return MCD(numeratore, denominatore)

    def __truediv__(self, other):
        numeratore = self.numeratore * other.denominatore
        denominatore = self.denominatore * other.numeratore
        return MCD(numeratore, denominatore)

    def __eq__(self, other):
        mult1, mult2, denominatore = mcm(self.denominatore, other.denominatore)
        if (self.numeratore * mult1) == (other.numeratore * mult2):
            return True
        return False

    def __ne__(self, other):
        mult1, mult2, denominatore = mcm(self.denominatore, other.denominatore)
        if (self.numeratore * mult1) != (other.numeratore * mult2):
            return True
        return False

    def __lt__(self, other):
        mult1, mult2, denominatore = mcm(self.denominatore, other.denominatore)
        if (self.numeratore * mult1) < (other.numeratore * mult2):
            return True
        return False

    def __gt__(self, other):
        mult1, mult2, denominatore = mcm(self.denominatore, other.denominatore)
        if (self.numeratore * mult1) > (other.numeratore * mult2):
            return True
        return False

    def __le__(self, other):
        mult1, mult2, denominatore = mcm(self.denominatore, other.denominatore)
        if (self.numeratore * mult1) <= (other.numeratore * mult2):
            return True
        return False

    def __ge__(self, other):
        mult1, mult2, denominatore = mcm(self.denominatore, other.denominatore)
        if (self.numeratore * mult1) >= (other.numeratore * mult2):
            return True
        return False


a = Fraction(7.5, -2)
b = Fraction(-3, -2)

c = d = Fraction(-1, 4)  # maggiore
d = Fraction(-1.5, 4)  # minore

print(f"Moltiplicazione = {a * b}")  # -45/8
print(f"Somma = {a + b}")  # -9/4
print(f"Divisione = {a / b}")  # -5/2
print(f"Sottrazione = {a - b}")  # -21/4
print(f"Uguaglianza = {c == d}")  # False
print(f"Disuguaglianza = {c != d}")  # True
print(f"Maggiore => {c > d}")
print(f"Minore => {c < d}")
print(f"Maggiore o uguale => {c >= d}")
print(f"Minore o uguale => {c <= d}")
