boltnev= input("Kérem az üzletlánc nevét!: ")
arak=[]

print("Kérem adja meg a vásárlás során kifizetett termékek árát!: (Min. 4 termék)")
while len(arak)<4 or input("Szeretne még terméket megadni? (i/n): ").lower()=="i":
    try:
        ar=float(input(f"{len(arak)+1}.termék ára."))
        arak.append(ar)
    except ValueError:
        print("Kérem számot adjon meg.")

atlagkoltseg= sum(arak) /len(arak)

print("\n--- Vásárlási információk ---")
print(f"Üzlet neve: {boltnev}")
print(f"Megadott árak: {', '.join(map(str, arak))}")
print(f"Átlagos költség: {round(atlagkoltseg)} Ft")


