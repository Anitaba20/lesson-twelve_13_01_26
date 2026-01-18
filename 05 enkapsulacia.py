# class Person:
#     def __init__(self, name, age, gender, occupation):
#         self.name = name
#         self.age = age
#         self._gender = gender      # _protected
#         self.__occupation = occupation  # __private
#
#     def pozdrav(self):
#         print(f"Ahoj volám sa {self.name} a mám {self.age} rokov")
#
#     def bydlisko(self):
#         print(f"{self.name} býva v {self.__occupation}")
#
#
# patrik = Person(name="Patrik", age=30, gender="muž", occupation="Bratislava")
#
# print(patrik.name)
# print(patrik.__occupation)
# print(patrik._gender)
#
#
# patrik.pozdrav()
# patrik.bydlisko()

# from datetime import date
#
#
# class Auto:
#     def __init__(self, rok, farba, model):
#         self.rok_vyroby = rok
#         self.__farba = farba
#         self.znacka = "Audi"
#         self.model = model
#
#     def vek_auta(self):
#         current_date = date.today()
#         current_year = current_date.year
#         return current_year - self.rok_vyroby
#
#     def daj_farbu(self):
#         return self.__farba
#
# # patrik_auto = Auto(rok=2020, farba="biela", model="A4")
# # print(patrik_auto.vek_auta())
#
# daslie_auto = Auto(rok=2019, farba="zelena", model="A5")
# print(daslie_auto.znacka)
#
# daslie_auto = Auto(rok=2019, farba="zelena", model="A5")
# print(daslie_auto.farba)
# daslie_auto.farba = "modrá"
# print(daslie_auto.farba)

# from datetime import date
#
#
# class Auto:
#     def __init__(self, rok, farba, model):
#         self.rok_vyroby = rok
#         self.__farba = farba
#         self.znacka = "Audi"
#         self.model = model
#
#     def vek_auta(self):
#         current_date = date.today()
#         current_year = current_date.year
#         return current_year - self.rok_vyroby
#
#     def daj_farbu(self):
#         return self.__farba
#
#
# daslie_auto = Auto(rok=2019, farba="zelena", model="A5")
# print(daslie_auto.daj_farbu())

# daslie_auto.farba = "modra"
# print(daslie_auto.farba)

# from datetime import date
#
#
# class Auto:
#     def __init__(self, rok, farba, model):
#         self.__rok_vyroby = rok
#         self.__farba = farba
#         self.znacka = "Audi"
#         self.model = model
#
#     def vek_auta(self):
#         current_date = date.today()
#         current_year = current_date.year
#         return current_year - self.__rok_vyroby
#
#     def daj_farbu(self):
#         return self.__farba
#
#
# daslie_auto = Auto(rok=2019, farba="zelena", model="A5")
# print(daslie_auto.vek_auta())

# daslie_auto.farba = "modra"
# print(daslie_auto.farba)

# from datetime import date
#
#
# class Auto:
#     def __init__(self, rok, farba, model):
#         self.__rok_vyroby = rok
#         self.__farba = farba
#         self.znacka = "Audi"
#         self.model = model
#
#     def vek_auta(self):
#         current_date = date.today()
#         current_year = current_date.year
#         return current_year - self.__rok_vyroby
#
#     def daj_farbu(self):
#         return self.__farba
#
#
# daslie_auto = Auto(rok=2019, farba="zelena", model="A5")
# print(daslie_auto.__rok_vyroby)

from datetime import date

class Auto:
    def __init__(self, rok, farba, model):
        self.__rok_vyroby = rok
        self.__farba = farba
        self.znacka = "Audi"
        self.model = model

    def vek_auta(self):
        current_date = date.today()
        current_year = current_date.year
        return current_year - self.__rok_vyroby


    def nastav_rok_vyroby(self, novy_rok_vyroby):
        if novy_rok_vyroby > 1900:
            self.__rok_vyroby = novy_rok_vyroby
        else:
            print("Rok vyroby musi byt v rozsahu od 1900 do dnesneho roku")

    def daj_farbu(self):
        return self.__farba


daslie_auto = Auto(rok=2019, farba="zelena", model="A5")
daslie_auto.nastav_rok_vyroby(2020)
print(daslie_auto.vek_auta())
