from datetime import date


class Auto:
    def __init__(self, rok, farba, znacka, model):
        self.rok_vyroby = rok
        self.farba = farba
        self.znacka = znacka
        self.model = model

    def vek_auta(self):
        current_date = date.today()
        current_year = current_date.year
        return current_year - self.rok_vyroby


patrik_auto = Auto(rok=2020, farba="biela", znacka="Skoda", model="Fabia")
print(patrik_auto.vek_auta())

daslie_auto = Auto(rok=2019, farba="zelena", znacka="Audi", model="A4")
print(daslie_auto.znacka)

