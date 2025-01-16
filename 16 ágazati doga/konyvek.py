
def __init__(self,cim,ar,eladottdb,ev):
        self.cim=cim
        self.ar=int(ar)
        self.eladottdb=int(eladottdb)
        self.ev=int(ev)

def __str__(self):
        return f"{self.cim}, {self.ar} Ft, {self.eladottdb} db, {self.ev}" 
def fajlbeolvasas(fajlnev):
        konyvek=[]
        with open(fajlnev, "r", encoding="UTF-8") as fajl:
            for sor in fajl:
                try:
                    adatok = sor.strip().split(", ")
                if len(adatok) == 4:
                    konyvek.append({
                        "cim": adatok[0],
                        "ar": int(adatok[1]),
                        "eladott_db": int(adatok[2]),
                        "ev": int(adatok[3])
                    })
                else:
                    print(f"Hibás adat: {sor.strip()}")
                except ValueError as e:
                print(f"Hiba az adatfeldolgozásban: {sor.strip()}, hiba: {e}")
        return konyvek

def konyvekkiirasa(konyvek):
        print("\nA könyvek listája:")
        for konyv in konyvek:
            print(konyv)

def konyvek2010utan(konyvek):
        return [konyv for konyv in konyvek if konyvek.ev >2010]
    
def legolcsobbkonyv(konyvek):
        return min(konyvek,key=lambda k: k.ar)
    
def harrypotterkonyvek(konyvek):
        return [konyv for konyv in konyvek if "Harry Potter" in konyvek.cim]
    
def fajlbakiir(konyvek,fajlnev):
        with open(fajlnev, "w", encoding="UTF-8") as fajl:
            for konyv in konyvek:
                fajl.write(f"{konyv}\n")

konyvek= fajlbeolvasas("konyvek.txt")

konyvekkiirasa(konyvek)
konyvek2010=konyvek2010utan(konyvek)
print("\n2010 után megjelent könyvek:")
for konyv in konyvek:
    print(konyv)
legolcsobb=legolcsobbkonyv(konyvek)
print(f"\nA legolcsóbb könyv: {legolcsobb.cim}, {legolcsobb.ar} Ft")
Harrypotterlista=harrypotterkonyvek(konyvek)
print("\nHarry Potter könyvek:")
for konyv in Harrypotterlista:
        print(konyv.cim)
fajlbakiir(Harrypotterlista, "Harrypotterkonyvek.txt")


