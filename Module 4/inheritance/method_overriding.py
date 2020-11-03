class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def displayData(self):
        print('In parent class displayData method')
        print(f'{self.name} {self.age}')

class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.empId=id

    def displayData(self):
        print('In child class diplayData method')
        print(f'{self.name} {self.age} {self.empId}')

person = Person('John', 50)
person.displayData()

emp = Employee('John', 50, 'E005')
emp.displayData()