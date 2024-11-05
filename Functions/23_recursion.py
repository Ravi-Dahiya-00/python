#recursion
'''when a function calls itself repeatedly

   it is similar to loops it can perform the same tasks as for and while loops.
   
    but it is easier way then loops. '''


import sys
print(sys.getrecursionlimit())                               #this will print the max no of recursion value  #this is 1000 default.

#we can change the value of recursion
sys.setrecursionlimit(200)                          #this will set the recursion value to be 200 
print(sys.getrecursionlimit())

#recursive function : function in which recursion is done

def show(n):          #this is function that is defined
    if n==0:       #this if condition is called as base case(this base case decides function should stop or go)
               #first this condition will be checked if this condition is false then it will check the next condition
        return              #if this condition will become true then it will stop otherwise it will be an infinite loop.
    print(n)                    #second this condition will be executed this will print n first
    show(n-1)                     # now this show(n-1) value will replace the show(n) in the function

show(5)




# for factorial

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))



# sum of first n natural number
def num(n):
    if n==0:
        return 0
    else:
        return num(n-1) + n

print(num(6))





##list printing through recursion

def a(x,y=0):
    if ( y == len(x)):
        return
    
    print(x[y])
    a(x,y+1)

list1=["1","2","3","4"]
a(list1)








#indirect recursion

'''
A function calls another function which then calls the first function again.'''


def num1(n):
    if n<=0:
        return
    print(n)
    num2(n-1)          #here  function is calling num2

def num2(n):
    print(n)
    num1(n-1)          #here function is calling num1

num2(10)                