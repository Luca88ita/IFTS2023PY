stream = open(".\Lezione0412\prova.txt")
# print(stream.readline())
# print(stream.readline())
for s in stream:
    print(s)
stream.close()
print("-"*20)
#####################

stream = open(".\Lezione0412\prova.txt")
print(stream.read())
stream.close()
print("-"*20)
#####################

stream = open(".\Lezione0412\prova.txt")
linee = stream.readlines()
print(linee)
stream.close()
print("-"*20)
#####################

stream = open(".\Lezione0412\prova.txt")
linee = stream.readlines()
for L in linee:
    print(":")
    print(L[::-1])  # inverte le stringhe
    # print(L[::]) # stampa tutte le linee
    # print(L) #stess come sopra
stream.close()
print("-"*20)
#####################

stream = open(".\Lezione0412\prova.txt")
