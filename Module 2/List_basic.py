list1= ['physics', 'chemistry', 1997, 2000]
list2= [1, 2, 3, 4, 5, 6, 7]

# accessing first element of list1 -> physics
print("list[0]: ", list1[0])
# accessing/slicing  elements starting from position 1 up to 5 not included,
# in case we have exceeded the limit, the return will be from start: last available value
print("list[1:5]: ", list1[1:5])

#updating 
print('Value available at index 2 : ')
#printing the third element
print(list1[2])
#since list is mutable, therefore we are updating the third element to -> 2001
list1[2]= 2001
print('New value available at index 2 :')
#print the updated value
print(list1[2])

# Adding 
list1.append(2020)
print('New List: ', list1)

#insert 
list1.insert(0, 'Python')
print('After inserting: ', list1)
