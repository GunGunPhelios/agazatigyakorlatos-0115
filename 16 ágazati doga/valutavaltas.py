currency=input("Milyen valutáról szeretne váltani? (EUR/USD/HUF):")

összeg= int(input("Mekkora összeget szeretne átváltani?: "))
eredmeny=0
if currency == "USD":
   eredmeny= 360*összeg
   print(f"A kapott összeged: {eredmeny} Ft.")
elif currency== "EUR": 
    eredmeny= 400*összeg
    print(f"A kapott összeged: {eredmeny} Ft.")
elif currency == "Euro":
    eredmeny=1.1*összeg
    print(f"A kapott összeged: {eredmeny} Dollár.")
else:
    print("Nem jó összeget adtál meg!")


