from datetime import datetime as dt
class Viragok:
def __init__(self,nev,ar,db,datum):
        self.nev=nev
        self.ar=int(ar)
        self.db=int(db)
        self.datum=datum

def __str__(self):
        return f"{self.nev}, {self.ar}, {self.db}, {self.datum}"
    
lista=[]

with open ("viragok.txt", "r", encoding="utf-8") as file:
        for sor in file:
            adat=sor.strip().split(",")
            lista.append{Viragok(adat[0], adat[1], adat[2], adat[3])}
print("A fájl tartalma:")
for i in lista:
    print(i)
draga=lista[0]
for i in lista:
     if i.ar>draga.ar:
          draga=i
print(f"A legdrágább virág: {draga.nev} ft.")

osszesen=0
for i in lista:
      osszesen+=1.db
      print(f"Az eladott virágok átlagos darabszáma: {round(osszesen/len(lista))} darab")

Rlista=[]
for i in lista:
      if i.nev[0] == "R":
            Rlista.append(i)

