class Tvar:
    def obsah(self):
        print("vypocet obsahu")

class Obdlznik(Tvar):
    def obsah(self):
        super().obsah()
        print("obdlznik")

class Kruh(Tvar):
    def obsah(self):
        super().obsah()
        print("kruh")

class Pravouhly_trojuholnik(Tvar):
    def obsah(self):
        super().obsah()
        print("pravouhly trojuholnik")

tvary = [Obdlznik(), Kruh(), Pravouhly_trojuholnik()]

for tvar in tvary:
    tvar.obsah()
