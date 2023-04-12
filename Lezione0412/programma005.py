# verificare moto rettilineo uniforme
# leggere il file
# per ogni distanza calcolare la velocità media
stream = open("./Lezione0412/laboratorio.txt")
L = []
for item in stream:
    # spazio
    i = item.find(":")
    spazio = item[0:i]
    item = item[i+2:]
    media = 0
    for j in range(4):
        i = item.find(" ")
        tempo = item[0:i]
        item = item[i+1:]
        media += float(spazio)/float(tempo)
    # calcolo velocità
    media /= 4
    print(media)
stream.close()
print("-"*20)
#####################
#
# buona pratica per lasciar gestire a python l'apertura e chiusura dei files
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
        print(media)

print("-"*20)
