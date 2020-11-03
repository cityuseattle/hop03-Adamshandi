class Dog:

    #Class attribute
    species= 'mammal'

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'


#Child class
class RussellTerrier(Dog):

    def run (self, speed):
        return f'{self.name} runs {speed}'


class Bulldog(Dog):

    def run (self, speed):
        return f'{self.name} runs {speed}'

jim = Bulldog('jim', 12)
print(jim.description())

print(jim.run('slowly'))