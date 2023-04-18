# scrivere una classe fraction per rappresentare numeri razionali come 1/2 e -3/8
# le frazioni dovrebbero essere salvate in forma ridotta (4/12 => 1/3) (6/-9 => -2/3)
# una funzione MCD mi torna il massimo comune divisore
# definire a funzione add e multiply che accetta un'altra fraction e modifichi la frazione corrente aggiungendo ad essa/moltiplicandola
# definire gli operatori +,*,==,<

import math


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
        numeratore = self.numeratore
        denominatore = self.denominatore
        mcd = math.gcd(numeratore, denominatore)
        numeratore = int(numeratore / mcd)
        denominatore = int(denominatore / mcd)

    def __str__(self):
        if self.denominatore == 1:
            return f"{self.numeratore}"
        else:
            return f"{self.numeratore}/{self.denominatore}"

    def __add__(self, other):
        mcm = math.lcm(self.denominatore, other.denominatore)
        mult1 = mcm / self.denominatore
        mult2 = mcm / other.denominatore
        numeratore = (self.numeratore * mult1) + (other.numeratore * mult2)
        denominatore = self.denominatore * mult1
        mcd = math.gcd(int(numeratore), int(denominatore))
        return f"{int(numeratore / mcd)}/{int(denominatore / mcd)}"

    def __sub__(self, other):
        mcm = math.lcm(self.denominatore, other.denominatore)
        mult1 = mcm / self.denominatore
        mult2 = mcm / other.denominatore
        numeratore = (self.numeratore * mult1) - (other.numeratore * mult2)
        denominatore = self.denominatore * mult1
        mcd = math.gcd(int(numeratore), int(denominatore))
        return f"{int(numeratore / mcd)}/{int(denominatore / mcd)}"

    def __mul__(self, other):
        numeratore = self.numeratore * other.numeratore
        denominatore = self.denominatore * other.denominatore
        mcd = math.gcd(numeratore, denominatore)
        return f"{int(numeratore / mcd)}/{int(denominatore / mcd)}"

    def __truediv__(self, other):
        numeratore = self.numeratore * other.denominatore
        denominatore = self.denominatore * other.numeratore
        mcd = math.gcd(numeratore, denominatore)
        return f"{int(numeratore / mcd)}/{int(denominatore / mcd)}"

    def __eq__(self, other):
        mcm = math.lcm(self.denominatore, other.denominatore)
        mult1 = mcm / self.denominatore
        mult2 = mcm / other.denominatore
        if (self.numeratore * mult1) == (other.numeratore * mult2):
            return True
        else:
            return False

    def __ne__(self, other):
        mcm = math.lcm(self.denominatore, other.denominatore)
        mult1 = mcm / self.denominatore
        mult2 = mcm / other.denominatore
        if (self.numeratore * mult1) != (other.numeratore * mult2):
            return True
        else:
            return False

    def __lt__(self, other):
        mcm = math.lcm(self.denominatore, other.denominatore)
        mult1 = mcm / self.denominatore
        mult2 = mcm / other.denominatore
        if (self.numeratore * mult1) < (other.numeratore * mult2):
            return True
        else:
            return False

    def __gt__(self, other):
        mcm = math.lcm(self.denominatore, other.denominatore)
        mult1 = mcm / self.denominatore
        mult2 = mcm / other.denominatore
        if (self.numeratore * mult1) > (other.numeratore * mult2):
            return True
        else:
            return False

    def __le__(self, other):
        mcm = math.lcm(self.denominatore, other.denominatore)
        mult1 = mcm / self.denominatore
        mult2 = mcm / other.denominatore
        if (self.numeratore * mult1) <= (other.numeratore * mult2):
            return True
        else:
            return False

    def __ge__(self, other):
        mcm = math.lcm(self.denominatore, other.denominatore)
        mult1 = mcm / self.denominatore
        mult2 = mcm / other.denominatore
        if (self.numeratore * mult1) >= (other.numeratore * mult2):
            return True
        else:
            return False


a = Fraction(5, -2)
b = Fraction(-3, -2)

c = d = Fraction(-1, 4)
d = Fraction(1, 8)

print(f"Moltiplicazione = {a * b}")  # -15/4
print(f"Somma = {a + b}")  # -1/1
print(f"Divisione = {a / b}")  # -5/3
print(f"Sottrazione = {a - b}")  # -4/1
print(f"Uguaglianza = {c == d}")  # False
print(f"Disuguaglianza = {c != d}")  # True
print(f"Maggiore => {c > d}")
print(f"Minore => {c < d}")
print(f"Maggiore o uguale => {c >= d}")
print(f"Minore o uguale => {c <= d}")
