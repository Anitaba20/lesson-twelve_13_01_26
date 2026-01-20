class City:
    def __init__(self, name, region, country, number_of_citizens, zip_code, area_code):
        self.name = name
        self.region = region
        self.country = country
        self.number_of_citizens = number_of_citizens
        self.zip_code = zip_code
        self.area_code = area_code

    def full_address(self):
        return f"{self.name}, {self.region}, {self.country}"

    def income(self):
        return self.number_of_citizens * 10


class CulturalCity(City):
    def __init__(self, name, region, country, number_of_citizens, zip_code, area_code, number_of_museums):
        super().__init__(name, region, country, number_of_citizens, zip_code, area_code)
        self.number_of_museums = number_of_museums

    def address_with_museums(self):
        return f"{self.full_address()}, Number of museums: {self.number_of_museums}"

    def income(self):
        return self.number_of_citizens * 10 + self.number_of_museums * 500

class TouristCity(City):
    def __init__(self, name, region, country, number_of_citizens, zip_code, area_code, number_of_visitors):
        super().__init__(name, region, country, number_of_citizens, zip_code, area_code)
        self.number_of_visitors = number_of_visitors

    def income(self):
        return self.number_of_citizens * 10 + self.number_of_visitors * 5


class IndustrialCity(City):
    def __init__(self, name, region, country, number_of_citizens, zip_code, area_code, number_of_factories):
        super().__init__(name, region, country, number_of_citizens, zip_code, area_code)
        self.number_of_factories = number_of_factories

    def income(self):
        return self.number_of_citizens * 10 + self.number_of_factories * 1000

    # alebo

    def income(self):
        return super().income() + self.number_of_factories * 1000


kosice = CulturalCity(
    "Kosice",
    "Kosice",
    "Slovensko",
    100000,
    1000,
    1000,
    10
)

mikulas = TouristCity(
    "Liptovsky Mikulas",
    "Zilinsky",
    "Slovensko",
    100000,
    1000,
    1000,
    10000
)

zlin = IndustrialCity(
    "Zlin",
    "Zlinsky",
    "Cesko",
    12231,
    1232,
    1222,
    2
)

print(kosice.number_of_citizens)

# print(kosice.income())
# print(mikulas.income())
# print(zlin.income())

mesta = [kosice, mikulas, zlin]

for mesto in mesta:
    print(mesto.full_address())
    print(mesto.income())