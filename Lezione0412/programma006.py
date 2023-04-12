import time


def writelines(file, lista):
    for linea in lista:
        file.write(linea+"\n")


with open("./Lezione0412/prova2.txt", "wt") as file:
    i = 0
    while True:
        i += 1
        file.write("ciao\nLuca")
        writelines(file, ["Ciao ancora", "Bella bionda"])
        time.sleep(3)
        print(i)
