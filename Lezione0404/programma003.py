import random
s1 = "afragola"
print(s1)
print(len(s1))
print(s1[1])
print(s1[1::1])
print(s1[::-1])

# liste in python

l = [1, 6, 9, 5, 4, 7]
print(len(l))
print(l[2])
print(l[::-1])
print(l[3:1:-1])

print([1, 2]+[4, 2])
l += [568]
print(l)

l.append(123)
print(l)
l.append([123])
print(l)
l.append({"luca", "pennini", 35})
print(l)

# raddoppia il valore di una lista
l1 = ["1", 5, 8, "12", 5.7, "5.7"]
l2 = []
for x in l1:
    if type(x) == type(1):
        # l2.append(int(x)*2)
        l2 += [int(x)*2]
    else:
        l2 += [float(x)*2]

print(l2)

print(ord("a"))
print(chr(97))

# numeri casuali
print(random.randint(10, 100))  # estrae inclusi gli estremi

print(random.random())

print(random.choice(["p1", "p2", "p3", "p4",
      "p5", "p6", "p7", "p8", "p9", "p10", 1, 5, 7, None]))
print(random.choice("prova"))

squadre = ["Germania", "Francia", "Spagna", "Argentina",
           "Marocco", "Brasile", "Svizzera", "Giappone"]
estratte = []


def estrai():
    global squadre, estratte
    while True:
        s = random.choice(squadre)
        if s not in estratte:
            estratte += [s]
            return s


for i in range(len(squadre)//2):
    s1 = estrai()
    s2 = estrai()
    girone = chr(ord("A")+i)
    print(f"1 Girone {girone}: {s1} - {s2}")


for i in range(len(squadre)//2):
    s1 = random.choice(squadre)
    squadre.remove(s1)
    s2 = random.choice(squadre)
    squadre.remove(s2)
    girone = chr(ord("A")+i)
    print(f"2 Girone {girone}: {s1} - {s2}")

# ------------------------

# tuple
tupla = (1, 2, 3)
# non posso scrivere tupla2 = (1) perchè altrimenti non viene considerata una tupla
tupla2 = (1,)
