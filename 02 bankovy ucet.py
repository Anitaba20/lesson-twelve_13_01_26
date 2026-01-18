# Trieda
class BankovyUcet:
    def __init__(self, majitel, zostatok):
        self.majitel = majitel
        self.zostatok = zostatok

    def vklad(self, suma):
        self.zostatok += suma

    def vyber(self, suma):
        if suma <= self.zostatok:
            self.zostatok -= suma
        else:
            print("Nedostatok peňazí")

    def vypis(self):
        print(f"{self.majitel} má na účte {self.zostatok} €")

# Vytvorenie objektov
ucet1 = BankovyUcet("Ján", 100)
ucet2 = BankovyUcet("Eva", 250)

# Použitie objektov
ucet1.vklad(50)
ucet1.vyber(30)
ucet1.vypis()

ucet2.vyber(300)
ucet2.vypis()