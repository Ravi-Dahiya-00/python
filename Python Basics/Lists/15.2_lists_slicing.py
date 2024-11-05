# List slicing extracts a subset of elements from a list to create a new list. The syntax for List slicing:


'''
Listname[start:stop]
Listname[start:stop:steps]
Default start: 0
 Default stop: n-1
[:] prints the whole list
[2:2] creates an empty slice
'''

# Let's consider a = [9, 8, 7, 6, 5, 4], observe the following examples:

a = [9, 8, 7, 6, 5, 4]
# Slices	Example	Description
print(a[0:3])	
# [9, 8, 7]	Print a part of list from index 0 to 2

print(a[:4]	)
# [9, 8, 7, 6]	Default start value is 0.
# Prints the values from index 0 to 3


print(a[1:]	)
# [8, 7, 6, 5, 4]	Prints values from index 1 onwards


print(a[:]	)
# [9, 8, 7, 6, 5, 4]	Prints the entire list


print(a[2:2])
# [ ]	Prints an empty slice


print(a[0:6:2])
# [9, 7, 5]	Slicing list values with step size 2


print(a[::-1])
# [4, 5, 6, 7, 8, 9]	Prints the list in reverse order


print(a[-3:])
# [6, 5, 4]	Prints the last 3 items in list


print(a[:-3])
# [9, 8, 7]	Prints all except the last 3 items in list























# List repetition uses the * operator to create a new list with elements repeated 'n' times.



# For example, if 
y = [2, 3, 4]

print(y * 0)  # Output: []
print(y * 2)  # Output: [2, 3, 4, 2, 3, 4]
print(y * 3)  # Output: [2, 3, 4, 2, 3, 4, 2, 3, 4]
# List concatenation combines two lists using the + operator:



# For example,

x = [1, 5, 6]
y = [2, 3, 4]
print(x + y)  # Output: [1, 5, 6, 2, 3, 4]


'''Python also offers the extend() method for this purpose. Call this method on the first list and pass the second list as an argument.
 This appends the second list to the first:'''

x.extend(y)
print(x)     # Output: [1, 5, 6, 2, 3, 4]
# List comparison checks if two lists are equal or not using the == and != operators, which returns a boolean value True or False.



# For example,

x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 3, 4]
print(x == y)    # Returns: False
print(x != y)    # Returns: True










# Aliasing occurs when a list is assigned to another variable, making both point to the same memory location. This leads to the same list being referenced by different names, causing changes from one reference to affect the other.



# For example,

a = [1, 2, 3, 4, 5, 6]
b = a
print(a)  # Output: [1, 2, 3, 4, 5, 6]
print(b)  # Output: [1, 2, 3, 4, 5, 6]
b is a    # Returns: True
a is b    # Returns: True
a[0] = 100
print(a)  # Output: [100, 2, 3, 4, 5, 6]
print(b)  # Output: [100, 2, 3, 4, 5, 6]


