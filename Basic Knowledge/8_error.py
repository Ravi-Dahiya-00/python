#programming errors:
#programming errors can be categorized into three types:


#1.syntax error:
              #most common error in python.
              #syntax error results from errors in code construction, such as mistyping a statement , incorrect indentation, omitting some necessary punctuation, or using an open parenthesis without a corresponding closing parenthesis.


#print("not used punctuation error)  
'''punctuation error'''

# easy to detect because python tells where they are and caused them.

#example:
'''File "<stdin>", line 1
    print("not used punctuation error)
          ^
SyntaxError: unterminated string literal (detected at line 1)
>>>'''



#2. Run-time error:
'''Runtime errors in Python are instances where a program terminates abnormally during execution,often due to incorrect or invalid operations.These errors occur after the program has been successfully compiled, typically when the code attempts to perform operations that are logically or mathematically invalid.'''




#example
'''Some examples of Python runtime errors:

1. division by zero
2. performing an operation on incompatible types
3. using an identifier which has not been defined
4. accessing a list element, dictionary value or object attribute which doesn’t exist
5. trying to access a file which doesn’t exist'''



#3. logic error:
'''it occurs when the program does not perform the way it was intended to.
      errors of this kind occur for a variety of reasons,
      such as incorrect assumptions about the program's behavior'''

#example:
'''some example of python logic errors:

converting a string to an integer 
using the wrong comparison operator
using the wrong logical error operator
using the wrong arithmetic operator
using the wrong assignment operator
using the wrong membership operator
using the wrong identity operator
using the wrong bitwise operator
using the wrong ternary operator'''




#in python, syntax errors are treated as run-time errors because they are detected by the interpreter when the program is executed.


#in general, syntax and runtime errors are easy to find and easy to correct , because python gives indications as to where the error is and ehy they are wrong.


#logic errors finding can be very challenging.






#4.type error 
#this error occurs when we typed something wrong such as written string as int

#length(12345)                      #wrong method
#length("12345")                    #right method












#5.value error
#this error happens when we want to convert some string value into integer and they cannot be converted into int data type.
#print(10+int(ravi))