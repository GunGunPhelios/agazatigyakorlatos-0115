import random

jatekok=[]
db=0
while True:
    jatek=(input("Kérlek add meg a kedvenc játékod: "))
    jatekok.append(jatek)
    db+=1
    print(f"{db}.{jatek} hozzáadva a listához.")
    if len(jatekok)==4:
        break
print()
evjateka=random.choice(jatekok)
print(f"A 2025-ös év játéka: {evjateka}")
