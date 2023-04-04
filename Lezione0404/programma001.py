print("ciao")

COSTANTE = 10


def saluto(stringa):
    print(stringa)
    return (stringa)


saluto("Ciao a tutti")

print(7//2)  # divisione intera con //
print(7/2)  # altrimenti divide con la virgola
print(8//7.5)

print(10**2)  # elevamento a potenza
print(9**(1/2))  # radice quadrata
print((-9)**(1/2))  # numeri complessi
print(type((-9)**(1/2)))
print(type(saluto("Ciao a tutti")))
print("-"*20+"\n")  # ripeto la stringa
print(5 == 6)
print(type(5 == 6))

x = None
print(x)

print("ciao "+"Luca")  # concateno stringhe
print("-"*20+"\n")  # ripeto la stringa
print("ciao", "Luca", 123)  # passa alla funzione print 3 argomenti da stampare

# questi sono 3 modi alternativi per iterare un ciclo for
for i in range(5):  # qui stampa tutti i valori da 0 a 5 escluso (0 non esplicitato)
    print(i)
for i in range(0, 5):  # qui stampa tutti i valori da 0 a 5 escluso (0 esplicitato)
    print(i)
for i in range(0, 5, 1):  # qui stampa tutti i valori da 0 a 5 escluso (con step da 1 e 0 esplicitato)
    print(i)
for i in range(5, 0, -1):  # qui stampa tutti i valori da 5 a 0 escluso (con step da -1)
    print(i)

print("-"*20+"\n")  # ripeto la stringa

for fila in range(10):
    stringa_fila = ""
    for posto in range(10):
        stringa_fila += "#"
    print(fila*COSTANTE, "", stringa_fila)

print("-"*20+"\n")  # ripeto la stringa

txt = input()
numero = int(txt)
print(txt*2)
print(numero*2)


print("-"*20+"\n")  # ripeto la stringa
# stampare una cornicetta 9 colonne per 5 righe dove nella terza risiede un numero dato in input raddoppiato


def righePiene():
    for i in range(2):
        print(("#"*9))


def rigaNum(numero):
    print(f"####{numero}####")


num = input()
righePiene()
rigaNum(int(num)*2)
righePiene()

print("-"*20+"\n")  # ripeto la stringa
