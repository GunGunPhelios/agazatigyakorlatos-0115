print("Üdvözöljük a gyümölcsboltban!")

gyumolcs=input("Kérem, válasszki a gyümőcsöt (alma/körte): ")
osszeg=0
db=int(input("Kérem, adja meg hány darabot szeretni venni: "))

if gyumolcs== "alma":
    osszeg=150*db
elif gyumolcs== "körte":
    osszeg=200*db
else:
    print("Nem jót adtál meg!")

print(f"A választott gyümölcs: {gyumolcs}")
print(f"A végösszeg {osszeg} ft.")


