# dizionari

me = {
    "name": "Luca",
    "lastName": "Pennini",
    "age": 35
}

me["nationality"] = "Italian"
me["hobbies"] = ["kayak", "mtb", "hicking"]

print(me.keys())
print(me.values())

print(
    f"My name is {me['name']} {me['lastName']}, I'm {me['nationality']} and I'm {me['age']} years old")
print(f"I have these hobbies: {me['hobbies']}")

for i in range(4):
    me[f"conteggio{i}"] = i

print(f"{me['conteggio0']}, {me['conteggio3']}, {me['conteggio1']}, {me['conteggio2']}")
