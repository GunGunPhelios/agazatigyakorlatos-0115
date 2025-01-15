print("Üdvözöljük a halboltban!")
fish= input("Melyik halat szeretnéd venni? (L/P )").lower()
mennyiség=int(input("Hány kgot szeretnél?"))

összeg=0
if fish== "l":
    összeg= 3000*mennyiség
elif fish== "p":
    összeg=2500*mennyiség
else:
    print("Nem adtál meg halat!")

print(f"A választott halad: {fish}")
print(f"Mennyiség: {mennyiség} kg")
print(f"Az összeg: {összeg} ft.")