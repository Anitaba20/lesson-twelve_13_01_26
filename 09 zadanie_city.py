# ZADANIE
#
# Create a class City. Class fields should store the following:
# city name, region name, country name, number of citizens,
# zip code, area code. Implement method to get full address.
#
# ZADANIE
#
# Vytvorte triedu City. Atribúty triedy by mali ukladať nasledujúce údaje:
# názov mesta, názov regiónu, názov krajiny, počet obyvateľov,
# PSČ, smerové číslo. Implementujte metódu na získanie celej (úplnej) adresy.


# class Mesto:
#
#     def __init__(self, nazov_mesta, region, krajina, pocet_obyvatelov, psc, predvolba):
#         self.nazov_mesta = nazov_mesta
#         self.region = region
#         self.krajina = krajina
#         self.pocet_obyvatelov = pocet_obyvatelov
#         self.psc = psc
#         self.predvolba = predvolba
#
#     def adresa(self):
#         print(
#         self.nazov_mesta,
#         self.region,
#         self.krajina,
#         "PSČ",
#         self.psc,
#         "predvoľba",
#         self.predvolba)
#
#
# bratislava = Mesto(
#         "Bratislava",
#         "Bratislavský kraj",
#         "Slovensko",
#         500000,
#         "811 01",
#         "02")
#
# trencin = Mesto(
#         "Trenčín",
#         "Trenčiansky kraj",
#         "Slovensko",
#         30000,
#         "911 01",
#         "032")
#
# bratislava.adresa()
#
# trencin.adresa()


class Mesto:
    def __init__(self, nazov_mesta, region, krajina, pocet_obyvatelov, psc, predvolba):
        self.nazov_mesta = nazov_mesta
        self.region = region
        self.krajina = krajina
        self.pocet_obyvatelov = pocet_obyvatelov
        self.psc = psc
        self.predvolba = predvolba

    def adresa(self):
        return f"{self.nazov_mesta}, {self.region}, {self.krajina}, PSČ {self.psc}, predvoľba {self.predvolba}"


bratislava = Mesto("Bratislava", "Bratislavský kraj", "Slovensko", 500000, "811 01", "02")
trencin = Mesto("Trenčín", "Trenčiansky kraj", "Slovensko", 30000, "911 01", "032")

print(bratislava.adresa())
print(trencin.adresa())

# vytvor ďalšie triedy, ktoré budú dediť z triedy city.
# hlavné mesto - počet úradov
# priemyselné mesto - počet fabrík
# kultúrne mesto - počet pamiatok
# add ku každej triede odlišný atribút

class Mesto:
    def __init__(self, nazov_mesta, region, krajina, pocet_obyvatelov, psc, predvolba):
        self.nazov_mesta = nazov_mesta
        self.region = region
        self.krajina = krajina
        self.pocet_obyvatelov = pocet_obyvatelov
        self.psc = psc
        self.predvolba = predvolba

    def adresa(self):
        return f"{self.nazov_mesta}, {self.region}, {self.krajina}, PSČ {self.psc}, predvoľba {self.predvolba}"


class HlavneMesto(Mesto):
    def __init__(self, nazov_mesta, region, krajina, pocet_obyvatelov, psc, predvolba, pocet_uradov):
        super().__init__(nazov_mesta, region, krajina, pocet_obyvatelov, psc, predvolba)
        self.pocet_uradov = pocet_uradov


class PriemyselneMesto(Mesto):
    def __init__(self, nazov_mesta, region, krajina, pocet_obyvatelov, psc, predvolba, pocet_fabrik):
        super().__init__(nazov_mesta, region, krajina, pocet_obyvatelov, psc, predvolba)
        self.pocet_fabrik = pocet_fabrik


class KulturneMesto(Mesto):
    def __init__(self, nazov_mesta, region, krajina, pocet_obyvatelov, psc, predvolba, pocet_pamiatok):
        super().__init__(nazov_mesta, region, krajina, pocet_obyvatelov, psc, predvolba)
        self.pocet_pamiatok = pocet_pamiatok


bratislava = HlavneMesto("Bratislava", "Bratislavský kraj", "Slovensko", 500000, "811 01", "02", 120)
trencin = KulturneMesto("Trenčín", "Trenčiansky kraj", "Slovensko", 30000, "911 01", "032", 25)

print(bratislava.adresa(), "- počet úradov:", bratislava.pocet_uradov)
print(trencin.adresa(), "- počet pamiatok:", trencin.pocet_pamiatok)