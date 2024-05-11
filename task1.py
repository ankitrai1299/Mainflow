#Main Flow
#Task 1

#Create a List
my_list = [2,52,65,41,23]

#Create a Dictionary
my_dict = {'a': 22,'b': 15,'c': 43,'d': 38}

#Create a Set
my_set = {54,18,21,16,43}

#Printing the Initial values
print("Initial List:", my_list)
print("Initial Dictionary:", my_dict)
print("Initial Set:", my_set)

#Basic Operation

#Add an element to the List
my_list.append(45)

#Add a key-value pair from the Dictionary
my_dict['e']=68

#Add an element to the Set
my_set.add(77)

#Remove an element from the List
my_list.remove(65)

#Remove a key-value pair from the Dictionary
del my_dict['b']

#Remove an element from the Set
my_set.remove(43)

#Modify an element in the List
my_list[4]= 81

#Modify a value in the Dictionary
my_dict['a'] = 94

#Printing the Final values
print("Final List:", my_list)
print("Final Dictionary:", my_dict) 
print("Final Set:", my_set)