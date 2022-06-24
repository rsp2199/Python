# input() function
'''its allows the user to take the inpute 
from the keybord but it will store as string
datatype'''
 
a =input("enter your name:-") #syntax
print (a) #to print the given inpute
print(type(a)) # to check its type
'''if we enter the int value it can be store as 
str datatype only'''
a=int(a) # convert datatype by using type casting
print(type(a)) # print the datatype
a+=12 # add the value to the given input
print (a) # print the added value