#1. split function
'''
1. The split() Function
Purpose: The split() function is used to divide a string into a list of substrings based on a specified delimiter.
'''


# str.split([separator[, maxsplit]])

# separator (optional): The delimiter on which to split the string (default is whitespace).
# maxsplit (optional): The maximum number of splits to make (default is -1, meaning "all").




# Example 1: Default split (by whitespace)
text = "Hello World! Welcome to Python."
words = text.split()  # Splits by whitespace
print(words)  # Output: ['Hello', 'World!', 'Welcome', 'to', 'Python.']

# Example 2: Split by a specific separator (comma)
csv_data = "name,age,city"
fields = csv_data.split(',')  # Splits by comma
print(fields)  # Output: ['name', 'age', 'city']

# Example 3: Split with maxsplit
sentence = "One two three four five"
parts = sentence.split(' ', 2)  # Split at most 2 times
print(parts)  # Output: ['One', 'two', 'three four five']

# Example 4: Handling consecutive separators
text = "apple;;banana;;cherry"
fruits = text.split(';')  # Splits by semicolon
print(fruits)  # Output: ['apple', '', 'banana', '', 'cherry']












'''
2. The map() Function
Purpose: The map() function applies a specified function to each item in an iterable (like a list or tuple) 
and returns a map object (which can be converted to a list).'''

# map(function, iterable, ...)


# function: A function to apply to each element of the iterable.
# iterable: An iterable (like a list) whose elements will be processed.


# Example 1: Using map to square numbers
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))  # Squaring each number
print(squared)  # Output: [1, 4, 9, 16, 25]

# Example 2: Convert string numbers to integers
input_string = "1,2,3,4,5"
# Split the string and convert to integers
number_list = list(map(int, input_string.split(',')))  # Convert strings to integers
print(number_list)  # Output: [1, 2, 3, 4, 5]

# Example 3: Using map with multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Adding corresponding elements of two lists
sum_lists = list(map(lambda x, y: x + y, list1, list2))
print(sum_lists)  # Output: [5, 7, 9]








# split() is used to break strings into lists based on delimiters.
# map() is used to transform items in an iterable using a function.
