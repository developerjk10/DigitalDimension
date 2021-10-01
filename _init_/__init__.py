class mammal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age

x = mammal("jay", 20)
print(x.getAge())

class Pet(mammal):
    def __init__(self, name, age, kind):
        super().__init__(name,age)
        self.kind = kind
    def setSpecies(self,kind):
        self.kind = kind
    def getSpecies(self):
        return self.kind
Pet1 = Pet("Boogers",8, "cat")
print(Pet1.getAge())
