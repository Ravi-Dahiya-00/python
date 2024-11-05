#function is block of statement which perform some specific task when it is called.

# this saves us from writing the code multiple times 
'''
def function_name(parameters):
    function body
    return expression
    
fun_name(arguments)
              '''

def calc_sum(a , b):                               #this will take input        #here a,b are (par1, par2)
    sum = a + b
    print(sum)
    return sum                                         #this will give output

calc_sum(5,6)                                        #called this function to perform the task
         #this 5,6 are (arg1,arg2)
        #when we will call this function these argument values will store in parameters and this task will be executed









def greet():             #this is function is defined
    print("hii")            #this is block of code in the function
    print("ravi")

greet()                        #this is where we called the function
greet()                         #this is we can call any function multiple times


a = greet()
print(a)                #none because the function which doesn't return any value that gives none












def greet_and_ask_age(name):
    # Print the greeting using the provided name
    print("Hello, " + name + "!")
    
    # Ask for the user's age
    age = input("Hi " + name + ", what is your age? ")
    
    # Print the age in the desired format
    print(name + ", your age is " + age + ".")

# Call the function with the direct value "Ram"
greet_and_ask_age("Ram")









'''
Return Statement
Definition:

The return statement is used in a function to send back a value to the caller. It ends the function's execution.

'''

def add(a, b):
    return a + b

result = add(5, 3)  # result is now 8


'''
Usage:

The value returned can be stored in a variable or used directly in expressions.
'''

'''
Direct Function Call
Definition:

A direct function call involves invoking a function and passing values (arguments) without storing them in variables first.
Example:
'''
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")  # Outputs: Hello, Alice!

'''
Usage:

This method is useful for quick, one-time usage of constants or literals.
'''

'''
Key Differences
Return Statement:

Allows for outputting values from functions to be used later. Essential for calculations or data processing within a program.
Direct Function Call:

Simplifies code when the values are constant or known. It avoids unnecessary variable declarations for single-use cases.'''










def calc_average(a,b,c):
    sum=a+b+c
    avg=sum / 3
    print(avg)
    return sum

print(calc_average(3,5,5))







#default parameters :      if no value is give in arguments it will give that default value to that parameters .

def calc_mul(a=2,b=2):                  #here 2,2 is default value 
    c=a*b
    print(c)
    return c

calc_mul()





cities= ["chennai", "delhi " , " mumbai ","pune","gurgaon","noida"]
vowels=["a","e","i","o","u"]

def list_len(list):
    print(len(list))

list_len(cities)
list_len(vowels)





3#usd to inr converter

def usd_inr(usd):
    usd_inr=usd*83
    print(usd,"USD =",usd_inr ,"INR")
usd_inr(10)


#even odd finder

def even_odd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")


even_odd(4)
even_odd(53)






#reborg's world  website


'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def Walk():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(6):
    walk()



# longer method:

    def flag():
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
for i in range(6):
    flag()

    '''







# arguments in python 
a=input("enter your name: ")
def greet(a):
    print(f"hii{" "}{a}")
    print("what are you doing")
greet(a)










def add(a,b):
    c=a+b
    print(c)
add(5,8)






a=int(input("enter first number: "))
b=int(input("enter second number: "))
c= f"sum is {a+b}"
def sum(c):
    print(c)
sum(c)






#types of arguments in python

'''
1.default
2.positional
3.keyword
4.arbitrary/ variable length'''






