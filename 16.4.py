class Zoldsegek:
    def __init__(self):
        self.lista=[]
    def beolvas(self):
        with open("zoldsegek.txt", "r", encoding="utf-8") as file:
            adatok=file.readlines()
            for adat in adatok:
                adat=adat.strip().split(",")
                zoldseg=adat[0]
                tonna=int(adat[1])
                ft= int(adat[2])
                ev= int(adat[3])
                self.lista.append({zoldseg,tonna,ft,ev})
            print(self.lista)
            for adat in self.lista:
                if adat[3] > 2015:
                    print(f"{adat[0]}, {adat[1]}, {adat[2]} {adat[3]}")
                if adat[2] < legolcsobb:
                    legolcsobb= adat[2]
                    legolcsobbzoldseg=adat[0]
                if adat[0].startswith("Paprika"):
                    

z=Zoldsegek()



        

        
            

