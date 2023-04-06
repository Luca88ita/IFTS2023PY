list1 = ["FR 60", "XS", "6XL", "S", 42, 43, "XL", 40, 46, 44, "M", 12, "IT 35", "IT 43", "FR 12", "UK 50", "XXL", "IT 50", "L",
         "FR 43", "FR 44", "8XL", "45", "44", 44, "48", "6XL", "XS", "6XL", "pippo", "70", 70, "XL", "IT 470", "IT 70", "IT 450", "XXS", "3XS", "4XS"]


taglie_numeriche = []
taglie_francesi = []
taglie_italiane = []
taglie_inglesi = []
taglie_europee = []
taglie_europee_ordinate = []


def ordina_e_stampa_europee():
    temp1 = []  # 5,4,3XS
    temp0 = []  # XXS,XS,S
    temp2 = []  # M
    temp3 = []  # L,XL,XXL
    temp4 = []  # 3,4,5XL
    for i in range(len(taglie_europee)):
        if taglie_europee[i].find("S") >= 0:
            if taglie_europee[i][0].isnumeric():
                temp0.append(taglie_europee[i])
            else:
                temp1.append(taglie_europee[i])
        elif taglie_europee[i].find("M") == 0:
            temp2.append(taglie_europee[i])
        elif taglie_europee[i].find("L") >= 0:
            if taglie_europee[i][0].isnumeric():
                temp4.append(taglie_europee[i])
            else:
                temp3.append(taglie_europee[i])
    temp0.sort(reverse=True)
    temp1.sort(reverse=True)
    temp3.sort()
    temp4.sort()
    taglie_europee_ordinate = temp0+temp1+temp2+temp3+temp4
    print("-"*20)
    print(f"Taglie europee: {list(dict.fromkeys(taglie_europee_ordinate))}")


def separa_taglie():
    for i in range(len(list1)):
        if type(list1[i]) == int:
            taglie_numeriche.append(list1[i])
        elif type(list1[i]) == str and len(list1[i]) < 6:
            if list1[i][0] == "F" and list1[i][1] == "R":
                taglie_francesi.append(list1[i])
            elif list1[i][0] == "I" and list1[i][1] == "T":
                taglie_italiane.append(list1[i])
            elif list1[i][0] == "U" and list1[i][1] == "K":
                taglie_inglesi.append(list1[i])
            elif list1[i].isnumeric():
                taglie_numeriche.append(int(list1[i]))
            elif len(list1[i]) < 4:
                taglie_europee.append(list1[i])
            else:
                print(f"{list1[i]} non è una taglia valida")
        else:
            print(f"{list1[i]} non è una taglia valida")


def ordina_e_stampa(listx, listStr):
    listx.sort()
    print(f"{listStr}: {list(dict.fromkeys(listx))}")


separa_taglie()
print("-"*20)
ordina_e_stampa(taglie_numeriche, "Taglie numeriche")
ordina_e_stampa(taglie_francesi, "Taglie Francesi")
ordina_e_stampa(taglie_italiane, "Taglie Italiane")
ordina_e_stampa(taglie_inglesi, "Taglie Inglesi")
ordina_e_stampa_europee()
