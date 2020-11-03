class Animal:
    def __init__(self):
        self.str1='Dog'
        print('Base1')

class Color:
    def __init__(self):
        self.str2='Black'
        print('Base2')

class Dog(Animal, Color):
    def __init__(self):
        Animal.__init__(self)
        Color.__init__(self)
        print('Derived')

    def printStat(self):
        print(self.str2, self.str1)

ob =Dog()
ob.printStat()