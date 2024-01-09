class Person:
    def __init__(self, name, age, gender, occupation, eyecolour):
        self.__name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.eyecolour = eyecolour

    def pozdrav(self):
        print(f"Ahoj volam sa {self.__name} a mam {self.age} rokov")

    def zamestnanie(self):
        print(f"Ahoj volam sa {self.__name} a byvam v {self.occupation}")

    def zostarni(self, pocetrokov):
        self.age = self.age + pocetrokov

patrik = Person("Patrik", 30, "muz", "Programator", "green")
print.pozdrav()
patrik.zamestnanie()
print(patrik.age)
patrik.zostarni(5)
print(patrik.age)
print(patrik.eyecolour)

lucia = Person("Lucia", 25, "zena", "Studentka")
lucia.zamestnanie()







