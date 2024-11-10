# writing a function in shorter way using lambda function

# syntax :
#      lambda input:expression




#function to find a square of any number
x=lambda x:x**2
print(x(5))





# function to calculate sum of two numbers 

a=lambda x,y : x+y
print(a(4,5))










b = lambda x:x[0]=="a"

print(b("apple"))
print(b("banana"))






b=lambda x: "even" if x%2==0 else "odd"

print(b(6))
print(b(3))






#difference between normal function and lambda function

# 1. lambda has no return value.
type(a)           #function

# 2. can be return only in one line
# 3. lambda function can be made only to use once, not used for code reusability
# 4. lambda functions have no name c         





# why we use this lambda function ????

#used along with higher function.

"""Accepting Functions as Arguments: A higher-order function can take other functions as parameters.
Returning Functions as Results: A higher-order function can return functions as its output.

    
    """




#Higher order functions

def return_sum(func,L):
    
    result=0
    
    for i in L:
        if func(i):
            result=result+i
            
    return result

L=[12,3,13,342,13,54,32,23]

x = lambda x:x%2==0
y = lambda x:x%2!=0
z = lambda x:x%3==0

print(return_sum(x,L))
print(return_sum(y,L))
print(return_sum(z,L))





#python inbuilt lambda function

# map , filter and reduce
 
 
 
 # map 
 
L=[1,2,3,4,5,6]
print(L)

print(list(map(lambda x:x*2,L)))

print(list(map(lambda x:x%2==0,L)))








# filter 
fruits=["apple","orange","mango","guava"]

print(list(filter(lambda fruit : "e" in fruit ,fruits)))










# reduce

import functools

l=[1,233,424,55,12]

print(functools.reduce(lambda x,y:x+y,l))




l1=[12,32,46,24,76,34]

print(functools.reduce(lambda x,y:x if x>y else y,l1))              #largest number


print(functools.reduce(lambda x,y:x if x<y else y,l1))              #smallest number