#type casting in python
#the conversion of one data type into the another data type is known as type casting in python or type conversion in python.

#python supports a wide variety of functions or method like: int(),float(),str(),ord(),hex(),oct(),tuple(),set(),list(),dict(),etc for the type casting in python.

#two types of type casting in python:
#1.explicit conversion
#2.implicit conversion

# what is explicit type casting????
#the conversion of one data type into another data type,done via developer or programmer`s intervention or manually as per the requirment,is known as explicit type casting.

#example of explicit type casting
a = "1"
b = "2"
print(
    a + b
)  #it will not add the numbers because these are string and these are printed in a line.
print(
    int(a) + int(b)
)  # A and B are string and these are converted into ineger by using int() function.






#how to write int in between the strings.
#convert the int value into string value.
length=len("ravi yadav")
print(length)
print("your name has"+str(length)+"characters")

print(type(length))    #int value


new_length=str(length)
print(type(new_length))

#for conerting into different data types we have different types.
#1. float()
#2.str()
#3.int()


print(10+float(10))





#what is implicit type casting????
#data types in python do not have the same level i.e. ordering of data types is not the same in python.
#some of the data types have higher order and some have lower order.while performing any operation on varibles with different data types in python ,
#one of the variable data types will be changed to the higher data type.
#according to the level,one data type is converted into other by the python interpreter itself(automatically) in the background.
#this is called implicit type casting in python.

#example of implicit type casting
a = 1.9
b = 8
print(a + b)


string = "15"
number = 7
string_number = int(
    string)  #throws an error if the string is not a valid integer
sum = number + string_number
print("the sum of both the numbers is:", sum)