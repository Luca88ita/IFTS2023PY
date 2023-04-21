# scrivere una classe fraction per rappresentare numeri razionali come 1/2 e -3/8
# le frazioni dovrebbero essere salvate in forma ridotta (4/12 => 1/3) (6/-9 => -2/3)
# una funzione MCD mi torna il massimo comune divisore
# definire a funzione add e multiply che accetta un'altra fraction e modifichi la frazione corrente aggiungendo ad essa/moltiplicandola
# definire gli operatori +,*,==,<

import math


def MCD(numeratore, denominatore):
    return math.gcd(int(numeratore), int(denominatore))


def MCM(denominatore1, denominatore2):
    return math.lcm(int(denominatore1), int(denominatore2))


def ralativeNums(Frac1, Frac2):
    mcm = MCM(Frac1.denominatore, Frac2.denominatore)
    num1 = Frac1.numeratore * (mcm / Frac1.denominatore)
    num2 = Frac2.numeratore * (mcm / Frac2.denominatore)
    return num1, num2


class Fraction:
    def __init__(self, numeratore, denominatore=1):
        while numeratore % 1 > 0 or denominatore % 1 > 0:
            numeratore *= 10
            denominatore *= 10
        if denominatore == 0:
            raise ValueError("Non si può dividere per zero")
        else:
            mcd = MCD(numeratore, denominatore)
            if denominatore < 0:
                self.numeratore = int(-numeratore / mcd)
                self.denominatore = int(-denominatore / mcd)
            else:
                self.numeratore = int(numeratore / mcd)
                self.denominatore = int(denominatore / mcd)

    def __str__(self):
        if self.denominatore == 1:
            return f"{self.numeratore}"
        return f"{self.numeratore}/{self.denominatore}"

    def __mul__(self, other):
        num = self.numeratore * other.numeratore
        den = self.denominatore * other.denominatore
        return Fraction(num, den)

    def __truediv__(self, other):
        num = self.numeratore * other.denominatore
        den = self.denominatore * other.numeratore
        return Fraction(num, den)

    def __add__(self, other):
        den = MCM(self.denominatore, other.denominatore)
        num1, num2 = ralativeNums(self, other)
        num = num1 + num2
        return Fraction(num, den)

    def __sub__(self, other):
        den = MCM(self.denominatore, other.denominatore)
        num1, num2 = ralativeNums(self, other)
        num = num1 - num2
        return Fraction(num, den)

    def __eq__(self, other):
        num1, num2 = ralativeNums(self, other)
        if num1 == num2:
            return True
        return False

    def __ne__(self, other):
        num1, num2 = ralativeNums(self, other)
        if num1 != num2:
            return True
        return False

    def __lt__(self, other):
        num1, num2 = ralativeNums(self, other)
        if num1 < num2:
            return True
        return False

    def __gt__(self, other):
        num1, num2 = ralativeNums(self, other)
        if num1 > num2:
            return True
        return False

    def __le__(self, other):
        num1, num2 = ralativeNums(self, other)
        if num1 <= num2:
            return True
        return False

    def __ge__(self, other):
        num1, num2 = ralativeNums(self, other)
        if num1 >= num2:
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
print(f"Somma = {a * b + c + d}")
print(f"Uguaglianza = {c == d}")  # False
