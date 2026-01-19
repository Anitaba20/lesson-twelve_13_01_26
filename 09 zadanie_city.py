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