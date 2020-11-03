class OverloadDemo:

    def sum(self, a, b, c=0):
        s= a + b + c
        return s

od= OverloadDemo()

sum=od.sum(7, 8)
print(f'Sum is: -> {sum}')


sum = od.sum(7, 8, 9)
print(f'Sum is -> {sum}')