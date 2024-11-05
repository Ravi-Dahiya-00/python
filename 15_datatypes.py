#what is data type????
#data type specifies the type of value 

#In Python, data types define the kind of values a variable can hold. Here are the built-in data types:

#types of data type in python
#1. numeric data type
#2. text data type
#3. boolean data type
#4. sequenced data type
#5. mapped data type








#what is numeric data type????
#numeric data type specifies the numeric value like int ,float,complex.


#int:represents the integer value.
#float:represents the floating value.
#complex:represents the complex value.




#example of numeric data type
a = 1  #integer data type
b = 2.5  #float data type
c = complex(2, 3)  #complex data type


print('\n', a)     #'\n' is used for new line
print(b)
print(c)









#what is text data type????
#text data type specifies the text value like str,string.

#str:represents the string value.
#string:represents the string value.

#example of text data type
a = 'hello'  #string data type
b = 'world'  #string data type


print(a, '\n', b)

print(a[3])    #thus will give the number 3 character in a.









#what is boolean data type????
#boolean data type specifies the next value like true false.

#example of boolean data type
a = True  #boolean data type     #T should be capital
b = False  #boolean data type     #F should be capital

print(a)
print(b)
print(a, b)

#use of boolean data type in the real world.
a=1
b=2
d=a<b
print(d)


print(type[d])







#mutable:
        # these can be change after creating.

#immutable:
         #these cannot be changed after creating once.




#what is sequenced data type????
#sequenced data type specifies the next value like list,tuple.

#list represents the list value.
#tuple represents the tuple value.

#example of sequenced data type.
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(a)




#1.
list1 = [8, 2.3, [-4, 5], ['apple', 'banana']]
print(
    list1
)  #list is a ordered collection of different data types and enclosed by square brackets and separated by commas.it can be changed these are mutable.
#we can store int,str,boolean,float and many more data types in list. 




#the append() method is used to add items to the list.



chars = ['a', 'b', 'c', 'd']
chars.append("abcd")
print(chars) # will print output as follows

#Output :
['a', 'b', 'c', 'd', 'abcd']





# The extend() method is used to add items of one list to be added as individual items of another list.

chars = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3]
chars.extend(list2)
print(chars) # will print output as follows

# Output : 
['a', 'b', 'c', 'd', 1, 2, 3]

# Note : Closely observe that the items of list2 are added as individual items to the chars list















#2.
tuple1 = (('parrot', 'sparrow'))

print(tuple1)
#tuple is a ordered collection of different data types.it can be changed these are immutable.



#3.
   #range:the range data type is used to represent a sequence of numbers.
   # It provides a convenient way to generate a series of integers within a specified range.



#creating a range:
# You can create a range object using the range() function, which takes three arguments: start, stop, and step.

# The start argument specifies the starting value of the range (inclusive),
# the stop argument specifies the stopping value of the range (exclusive),
# and the step argument specifies the increment between consecutive numbers (default is 1).


# Range from 0 to 9 (exclusive) with a step of 1
range1 = range(10)
print(list(range1))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
# Range from 1 to 10 (exclusive) with a step of 1
range2 = range(1, 11)
print(list(range2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# Range from 0 to 10 (exclusive) with a step of 2
range3 = range(0, 11, 2)
print(list(range3))  # Output: [0, 2, 4, 6, 8, 10]


#using range with loops
# One of the most common use cases of the range data type is to use it with loops for iterating over a sequence of numbers. 
# This allows you to perform a set of actions repeatedly for a specified number of times. Here's an example of using range with a for loop:

# Looping through the range and printing the numbers
for num in range(5):
    print(num)









#what is mapped data type????
#mapped data type specifies the next value like dict,dict.

#dict represents the dict value.
#dict represents the dict value.

#example of mapped data type.
a = {'name': 'Ravi', 'age': '17', 'canvote': 'true'}

print(a)









#what is set data type?????
# A set is a mutable data type that contains an unordered collection of items. A set is represented with { }.

# Every element in the set should be unique (no duplicates) and must be immutable (which cannot be changed).
#  But the set itself is mutable. We can add or remove items / elements from it.

# Note: Mutable data types like list, set and dictionary cannot become elements of a set.

# The set itself is mutable i.e. we can add or remove elements from the set.

# The main uses of sets are:
#  Membership testing
# Removing duplicates from a sequence
# Performing mathematical operations such as intersection, union, difference, and symmetric difference

# Creation of sets
# 1. One way to create a set is by using built-in function set()

# Empty set
# An empty set can be created using built-in set() function.

myset = set()
print(myset)       # Result: set()
print(type(myset)) # <class 'set'>


#
# 2. Another way to create a set is to put all elements inside curly braces separated by commas.
myset1 = {1, 2, 3} 
print(myset1)       # Result: {1, 2, 3}
print(type(myset1)) # Result: <class 'set'>
# Note : Empty curly braces { } does not make an empty set in Python, it makes an empty dictionary instead. Dictionary data type is introduced in the upcoming lessons.
test = { } 
print(type(test)) #Result: <class 'dict'>
