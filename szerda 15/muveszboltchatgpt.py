import os

class Termek:
    """Egy művészbolt termékeit reprezentáló osztály."""
    def __init__(self, nev, ar, eladott_mennyiseg, szallitasi_datum):
        self.nev = nev
        self.ar = float(ar)
        self.eladott_mennyiseg = int(eladott_mennyiseg)
        self.szallitasi_datum = szallitasi_datum

    def __str__(self):
        return f"{self.nev}, {self.ar} Ft, {self.eladott_mennyiseg} db, szállítva: {self.szallitasi_datum}"


def beolvas_termekek(fajlnev):
    """Beolvassa a termékeket a megadott fájlból, és Termek objektumokat hoz létre."""
    termekek = []
    if not os.path.exists(fajlnev):
        print(f"A {fajlnev} fájl nem található.")
        return termekek

    with open(fajlnev, "r", encoding="utf-8") as fajl:
        for sor in fajl:
            adatok = sor.strip().split(";")
            if len(adatok) == 4:
                termekek.append(Termek(*adatok))
    return termekek


def legdragabb_termek(termekek):
    """Meghatározza a legdrágább terméket a listából."""
    return max(termekek, key=lambda termek: termek.ar)


def atlag_eladott_mennyiseg(termekek):
    """Kiszámítja az eladott termékek darabszámának átlagát."""
    osszes_mennyiseg = sum(termek.eladott_mennyiseg for termek in termekek)
    return osszes_mennyiseg / len(termekek) if termekek else 0


def c_betus_termekek(termekek):
    """Kiválogatja a 'C' betűvel kezdődő termékeket."""
    return [termek for termek in termekek if termek.nev.upper().startswith("C")]


def irj_fajlba_c_betus_termekek(termekek, fajlnev):
    """Kiírja a 'C' betűs termékeket egy fájlba."""
    with open(fajlnev, "w", encoding="utf-8") as fajl:
        for termek in termekek:
            fajl.write(f"{termek.nev};{termek.ar};{termek.eladott_mennyiseg};{termek.szallitasi_datum}\n")


def main():
    fajlnev = "termekek.txt"
    termekek = beolvas_termekek(fajlnev)

    # 4. Írja ki a fájl teljes tartalmát a konzolra
    print("A termékek listája:")
    for termek in termekek:
        print(termek)

    # 5. Legdrágább termék meghatározása
    if termekek:
        legdragabb = legdragabb_termek(termekek)
        print(f"\nA legdrágább termék: {legdragabb.nev}, {legdragabb.ar} Ft")

    # 6. Eladott termékek átlagának kiszámítása
    atlag = atlag_eladott_mennyiseg(termekek)
    print(f"\nAz eladott termékek átlagos darabszáma: {atlag:.2f} db")

    # 7. 'C' betűs termékek számlálása
    c_betus_lista = c_betus_termekek(termekek)
    print(f"\n'C' betűs termékek száma: {len(c_betus_lista)}")

    # 8. 'C' betűs termékek fájlba írása
    c_fajlnev = "C_betus_termekek.txt"
    irj_fajlba_c_betus_termekek(c_betus_lista, c_fajlnev)
    print(f"A 'C' betűs termékek kiírva a {c_fajlnev} fájlba.")

    # 9. Konzolra is kiírja a 'C' betűs termékeket
    print("\n'C' betűs termékek:")
    for termek in c_betus_lista:
        print(termek)


if __name__ == "__main__":
    main()
