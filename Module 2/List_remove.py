#del 
motorcycle= ['honda', 'yamaha', 'suzuki']
del motorcycle[1]
print(motorcycle)

#pop 
motorcycle= ['honda', 'yamaha', 'suzuki']
popped_motorcycle= motorcycle.pop()
print(motorcycle)
print(popped_motorcycle)
first_owned= motorcycle.pop(0)
print('The first motorcycle I owned was a', first_owned)

#remove
motorcycle= ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycle.remove('ducati')
print(motorcycle)