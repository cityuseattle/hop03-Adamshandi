class Employee:

    ## Class Attribute shared by all instances
    emp_count=0
    
    def __init__(self,first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last +'@company.com'
        
        ## This get incremented whenever we create an instance
        Employee.emp_count+=1

    def showinfo(self):
        return f'{self.first} {self.last}, {self.email}'


emp1= Employee('Elliot', 'Alderson', 7000)
emp2=Employee('Jean', 'Grey', 8000)

print(emp2.showinfo())
print('Total Employee: ', Employee.emp_count)


