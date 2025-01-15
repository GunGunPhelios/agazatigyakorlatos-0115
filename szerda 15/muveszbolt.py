class Muveszbolt:
    def __init__(self):
        self.lista=[]
    def bolt(self):
        with open("termekek.txt", "r", encoding="UTF-8") as file:
            adatok=file.readlines()
            for adat in adatok[1:]:
                adat= adat.strip()
                adat= adat.split(";")

                termek=adat[0]
                ar= int(adat[1])
                eladottmennyiseg=int(adat[2])
                ev=int(adat[3])
                self.lista.append([termek,ar,eladottmennyiseg,ev])

            Legdragabbar=0
            legdragabbtermek=""

            db=[]
            c_betus=0 
            for item in self.lista:
                #print(f"{item[0]},{item[1]},{item[2]},{item[3]}")
                c_betus+=1
                db.append(item[2])
                if item[1]> Legdragabbar:
                    Legdragabbar=item[1]
                    legdragabbtermek=item[0]


            print(f"A legdrágább termék: {legdragabbtermek}")
            print(f"A legdrágább ár: {Legdragabbar} ft.")
            print(f"átlag: {round(sum(db) / len(db))}")

            with open("C_betus_termekek.txt", "w", encoding="UTF-8") as fajl:
                for ir in self.lista:
                    if ir[0].startswith("C"):
                        fajl.write(f" {ir[0]}, {ir[1]},{ir[2]},{ir[3]}")



mbolt= Muveszbolt()
mbolt.bolt()
