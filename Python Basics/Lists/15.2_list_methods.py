# here is a list of methods that can be applied to list:



# 1. append(): Adda a single item at the end of the list.

x = ['a', 'b', 'c', 'd']
x.append('e')
print(x)
['a', 'b', 'c', 'd', 'e']
x.append([1, 2, 3])
print(x)
['a', 'b', 'c', 'd', [1, 2, 3]]
# Click on  Live Demo button to know how to append elements to a List in Python.



# 2. extend(): It is used to extend a list by appending elements from an iterable (such as another list, tuple, or string) to the end of the list. 
# This method modifies the original list and does not create a new list.

x = ['a', 'b', 'c', 'd']
x.extend([1, 2, 3, 4])
print(x)
['a', 'b', 'c', 'd', 1, 2, 3, 4]


# 3. insert(index, item): It is used to insert a specified element (item) at a specific position (index) in a list.

x = ['a', 'b', 'c', 'd']
x.insert(0, 1)
print(x)
[1, 'a', 'b', 'c', 'd']


# 4. remove(element): It is used to remove the first occurrence of a specified element from a list.
#  It returns an error if the element doesn't exist.

L1 = [1, 'a', 'b', 'c', 'd', 'e']
L1.remove(1)
print(L1)
['a', 'b', 'c', 'd', 'e']
# L1.remove('f')
'''Traceback (most recent call last):
  File "", line 1, in 
ValueError: list.remove(x): x not in list'''


# 5. pop(), pop(index): pop() is used to remove and return the last element from a list.
#  It can also take an optional index argument to remove and return an element from a specific index in the list. If an invalid index is specified, 
# then an IndexError is thrown.

x = ['a', 'b', 'c', 'd', 'e']
x.pop(2)
'c'
print(x)
['a', 'b', 'd', 'e']
x.pop()
'e'
print(x)
['a', 'b', 'd']
# x.pop(3)
'''Traceback (most recent call last):
  File "", line 1, in 
IndexError: pop index out of range'''


# 6. count(element): It is used to count the occurrences of a specified element within a list.

x = ['a', 'b', 'a', 'c', 'd', 'e', 'a']
x.count('a')
3


# 7. sort(key = None, reverse = False): It is used to sort the elements of a list in ascending order. 
# It modifies the original list in-place and does not return a new list.
#  If the parameter reverse = True,
#  then the list is sorted in descending order.

x = ['z', 'f', 'e', 'a','b', 'g', 't']
x.sort()
print(x)
['a', 'b', 'e', 'f', 'g', 't', 'z']
x.sort(key = None, reverse = True)
print(x)
['z', 't', 'g', 'f', 'e', 'b', 'a']


# 8. reverse(): It is used to reverse the order of elements of a list in place.

x = ['z', 'f', 'e', 'a','b', 'g', 't']
x.reverse()
print(x)
['t', 'g', 'b', 'a', 'e', 'f', 'z']


# 9. copy(): It is used to create a shallow copy of a list.

x = ['z', 'f', 'e', 'a','b', 'g', 't']
y = x.copy()
print(y)
['z', 'f', 'e', 'a', 'b', 'g', 't']
print(x is y)
False