#user input in python
#in python,we can take user input directly by using input() function.
#this input function gives a return value as string/character hence we have to pass that int() to the function.

#example of user input
a = input('enter your name:')
print("my name is",a)
X=input("enter first number:")
Y=input("enter second number:")

print((X)+(Y))          #it will concatenate x and y.

print(int(X)+int(Y))         #it will give sum of x and y.


#INPUT function is used for taking user input
variableradius=print(input("enter a value:"))



# Basic usage of eval function.
x = 5
result = eval('x + 10')
print(result)  # Output: 15

eval('3 * (4 + 5)')  # Output: 27


#reading input from the console
#reading console enables the program to accept input from the user.

s=input("enter a value for radius:")                    #read input as a string
radius=eval(s)                                          #convert the string to a number

#int can also be used for converting the string into a number
x=eval(input("enter your first number:"))              #if int is not used it will take it is a string


#if user gives input rather then a number it will give runtime error.








#multiple inputs from the user

#computeaverage.py

#prompt the user to enter three numbers
number1=eval(input("enter the first number:"))
number2=eval(input("enter the second number:"))
number3=eval(input("enter the third number:"))

#compute average
average=(number1+number2+number3)/3

#display results
print("the average of",number1,number2,number3,"is",     #python will find end parenthesis in the end of line.
      average)                                           #if it does not find it will scan next line automatically.
                                                         #because it knows that line has not ended here.