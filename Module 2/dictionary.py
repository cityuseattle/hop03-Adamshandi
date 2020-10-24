#Accessing
dict= {'Name':'abc', 'Age':7}
print('Name : ', dict['Name'], "\n", "Age : ", dict['Age'])

#Updating
dict['Age']=20
print('Updated age :', dict['Age'])


#Adding
dict['phone_no']=12334343
print('After adding the new pair :', dict)

#deleting
del dict['phone_no']
print('After deleting phone_no :', dict)