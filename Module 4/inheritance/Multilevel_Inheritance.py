class Animal:

    def __init__(self, name):
        self.name= name
        print('Parent got called')

    def getName(self):
        return self.name

class Dog(Animal):

    def __init__(self, name, age):
        Animal.__init__(self, name)
        self.age=age

    def getAge(self):
        return self.age

class Pug(Dog):

    def __init__(self, name, age, color):
        Dog.__init__(self, name, age)
        self.color=color

    def getColor(self):
        return self.color

ob = Pug('PugPug', 2, 'brown')
print(ob.getName(), ob.getName(), ob.getColor())