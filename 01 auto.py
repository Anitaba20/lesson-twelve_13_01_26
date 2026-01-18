class Auto:
    def __init__(self, znacka, farba):
        self.znacka = znacka
        self.farba = farba

    def vypis_info(self):
        print(f"Auto značky {self.znacka} má farbu {self.farba}")


# vytvorenie objektu
moje_auto = Auto("Škoda", "červená")

# zavolanie metódy
moje_auto.vypis_info()