class Person:
    def __init__(self, name, age, gender, occupation):
        self.name = name
        self.age = age
        self._gender = gender  # _protected
        self.__occupation = occupation  # __private

    def pozdrav(self):
        print(f"Ahoj volam sa {self.name} a mam {self.age} rokov")

    def bydlisko(self):
        print(f"{self.name} byva v {self.__occupation}")


class Student(Person):
    def __init__(self, name, age, gender, occupation, score):
        super().__init__(name, age, gender, occupation)
        self.score = score

    def jeGenius(self):
        if self.score > 90:
            print(f"{self.name} je genius a {self._gender}")
        else:
            print(f"{self.name} nie je genius a {self._gender}")


patrik = Student(name="Patrik", age=30, gender="muz",
                 occupation="Bratislava", score=95)
milan = Student(name="Milan", age=20, gender="muz",
                occupation="Bratislava", score=60)

print(patrik.name)
patrik.pozdrav()
patrik.bydlisko()
patrik.jeGenius()
milan.jeGenius()