original= [8, 20, -10, 55, -777]

for i in range(len(original)):
    print(original[i])


## The challenge
original= [8, 20, -10, 55, -777]
print("No negative numbers version! ")

for i in range(len(original)):
    if(original[i] < 0):
        original[i]=abs(original[i])
    print(original[i])