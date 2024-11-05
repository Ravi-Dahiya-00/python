#list objects are mutable once we create list objects we can perform any changes in that object.

#if content is changing we can go for a list.

#list objects can not used as key for dictionaries because key should be hashable and immutable.



# Here is a list of operations that are possible on a list sequence:

# Operations	Example	Description


# Create a List	
a = [2 ,3, 4, 5, 6, 7, 8, 9, 10]
print(a) # [2 ,3, 4, 5, 6, 7, 8, 9, 10]
# Create a comma separated list of elements and assign to variable 'a'




# Indexing	
print(a[0])    # 2
print(a[-1])   # 10
# Access the item at position '0'
# Access the last item using negative indexing



# Slicing	
print(a[0:3]) # [2, 3, 4]
print(a[0:])  # [2, 3, 4, 5, 6, 7, 8, 9, 10]
# Print a part of list starting at index '0' till index '2'
# Print a part of the list starting at index '0' till the end of list



# Concatenation	
b = [20, 30]
print(a + b)  # [2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]
# Concatenate two lists and display its output



# Updating	
a[2] = 100
print(a)   # [2, 3, 100, 5, 6, 7, 8, 9, 10]
# Update the list element at index 2



# Membership	
5 in a     # True
102 in a   # False

# Returns True if element is present in list.

# Otherwise returns false.

# Comparison	
a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [2, 3, 4]
a == b     # False
# Returns True if all elements in both lists are same.


# Otherwise returns false
# Repetition	
a = [1, 2, 3]
print(a * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3] 
# Here the * operator repeats a list for the given number of times.









# Here is a list of built-in functions that can be applied on a list:
# 1. all(): Returns True if all the items in the list have a true value.
print(all([' ', ',', '1', '2']))
True

# 2. any(): Returns True if atleast one item in the list has a true value.
print(any([' ', ',', '1', '2']))
True

# 3. enumerate(): Returns an enumerate object consisting of the index and the values of all items of the list as a tuple pair.
print(list(enumerate(['a','b','c','d','e'])))
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

# 4. len(): It calculates the length of the list i.e., the number of elements in the list.
print(len(['a', 'b', 'c', 'd', 'e']))
5

# 5. max(): Returns the item with the highest value from the list
print(max([1, 2, 3, 4, 5]))
5

# 6. min(): Returns the item with the lowest value from the list.
print(min([1, 2, 3, 4, 5]))
1

# 7. sorted(): Returns a sorted version of the given list, leaving the original list unchanged.
origlist = [1, 5, 3, 4, 7, 9, 1, 27]
print(sorted(origlist)
[1, 1, 3, 4, 5, 7, 9, 27]

# 8. sum(): Returns the sum of all the elements of a list. It works only on an integer list.
print(sum([1, 5, 3, 4, 7, 9, 1, 27]))