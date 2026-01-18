
class Person:
    def __init__(self, name, age, gender, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation

    def pozdrav(self):
        print(f"Ahoj volam sa {self.name} a mam {self.age} rokov")


patrik = Person(
    name="Patrik",
    age=30,
    gender="muz",
    occupation="Bratislava"
)

patrik.pozdrav()