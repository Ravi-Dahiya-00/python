#assignment statement:
                    #the statement for assigning a value to variable is called an assignment statement.

#assignment operator:(=) is used as assignment operator in python.

#the syntax for assigning statements is as follows:
variable ="expression"


#an expression represents a computation involving values,variables,and operators that, taken together,evaluate to a value.

y=1                                        #assign 1 to variable y
radius=1.0                                 #assign 1.0 to variable radius
x=5*(3/2) + 3*2                            #assign the value of the expression to x
x=y+1                                      #assign the addition of y and 1 to x
area=radius*radius*3.14159                 #computing area


#variable can be used in both side of the = operator
x=x+1



#1=x #wrong method

#in mathematics it is equation    x=2*x+1
#in python, x=2*x+1 is an assignment statement that evalutes the expression 2*x+1 and assigns the result to x.


#if a value is assigned to multiple variables,you can use a syntax like this:
i=j=k=1










#scope of a variable:
                   #the scope of a variable is the part of the program where the variable can be referenced(used).
#variable must be defined before the use.




#simultaneous assignment:
                    #python also supports simultaneous assignment in syntax like this:
#var1,var2,var3,....,varn = exp1,exp2,exp3,....,expn
                 #it tells python to evaluate all the expressions on the right and assign them to the corresponding variable on left.



#simultaneous assignment can also be used to obtain multiple input in one statement 

#computeaveragewithsimultaneousassignment.py

#prompt the user to enter three numbers
number1,number2,number3=eval(input("enter three numbers seperated by commas:"))


#compute average
average=(number1+number2+number3)/3

#display result
print("the average of",number1,number2,number3,"is",average)