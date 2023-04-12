import time


def writelines(file, lista):
    for linea in lista:
        file.write(linea+"\n")


res = []
with open("./Lezione0412/prova2.txt", "wt") as file:
    i = 0
    while i == 4:
        i += 1
        file.write("ciao\nLuca")
        writelines(file, ["Ciao ancora", "Bella bionda"])
        time.sleep(3)
        print(i)

with open("./Lezione0412/laboratorio.txt") as stream:
    L = []
    for item in stream:
        # spazio
        L = (item.strip()).split(":")
        spazio = L[0]
        tempi = L[1]
        numeri = (tempi.strip()).split()
        media = 0
        for tempo in numeri:
            media += float(spazio)/float(tempo)
        media /= 4
        res.append(media)


def applica_a_tutti(lista, funzione):
    n_lista = []
    for x in lista:
        n_lista += [funzione(x)]
    return n_lista


with open("./Lezione0412/prova2.txt", "wt") as file:
    res = applica_a_tutti(res, str)
    # res = res.apply(str) #valida sula libreria numpy
    # res = [str(x) for x in res]
    stringa = " - ".join(res)
    print(stringa)

print("-"*20)
