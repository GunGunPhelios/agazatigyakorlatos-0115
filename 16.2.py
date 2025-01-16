import random
allatok=[]
db=0
print("Add meg a 3 kedvenc állatodat!")

while len(allatok) <3:
    bekertallatok=input("Add meg a kedvenc állatod: ")
    allatok.append(bekertallatok)
    db+=1
    print (f"{db} állat került hozzáadásra a listádhoz.")
print(f"A kedvenc állataid: {allatok[0]}, {allatok[1]}, {allatok[2]}")

sorsoltallat=random.choice(allatok)
print(f"A kivalasztott kedvenc állat: {sorsoltallat}.")

