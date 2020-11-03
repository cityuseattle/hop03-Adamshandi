class Parrot:

    def fly(self):
        print('Parrot can fly')

    def swim(self):
        print("Parrot can't swim")
    

class Penguin:

    def fly(self):
        print('Penguin cannnot fly')
    
    def swim (self):
        print('Penguin can swim')


def flying_test(bird):
    bird.fly()

blue= Parrot()
peggy= Penguin()


flying_test(blue)
flying_test(peggy)