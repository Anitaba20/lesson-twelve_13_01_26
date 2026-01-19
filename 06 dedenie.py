class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self._gender = gender          # _protected
        self.__address = address # __private

    def pozdrav(self):
        print(f"Ahoj, volam sa {self.name} a mam {self.age} rokov")

    def bydlisko(self):
        print(f"{self.name} byva v {self.__address}")

patrik = Person(name="Patrik", age=30, gender="muz", address="Bratislava")
print(patrik.name)
print()
patrik.bydlisko()

class Student(Person):
    def __init__(self, name, age, gender, address, score):
        super().__init__(name, age, gender, address)
        self.score = score

    def jeGenius(self):
        if self.score > 90:
            print(f"{self.name} je genius a {self._gender}")
        else:
            print(f"{self.name} nie je genius a {self._gender}")

patrik = Student(name="Patrik", age=30, gender="muz", address="Bratislava", score=95)
milan = Student(name="Milan", age=20, gender="muz", address="Bratislava", score=40)