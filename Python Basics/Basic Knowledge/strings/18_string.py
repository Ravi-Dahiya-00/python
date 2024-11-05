#what are string in python????
#in python, anything that you enclose between single and double quotation marks is considered as string.
#a string is essentially a sequence or array of textual data.
#strings are used when working with unicodes characters.


#example of string
name="ravi"
friend="rohan"
another_friend="lovish"

x=input("enter friend name:")

print("hello"+name)

print("your friend is " + x)





#talk="he said "he wants to eat an apple""

#this line will show an error because we cannot use double cot in double cot.


#1st
#method to resolve this error
#so we use escape sequence character.

talk="he said \"he wants to eat an apple\""

print(talk)


#2nd 
#method to resolve this same error
#so we can enclose our string in single cot.

talk='he said "he wants to eat an apple"'

print(talk)


#3rd
#method to resolve this same error
#so we can use single triple cot.

talk='''he said "he wants to eat an apple"'''

print(talk)



#4th
#method to resolve this same error
#so we can use double triple cot.
talk="""he said "he wants to eat an apple" """

print(talk)


#basically we use triple cot for multiline string.
#this help in copy and paste the string.

apple='''hi Ravi,
how are you doing
i am good
call me later '''

print(apple)

#this is main use of triple single cot.
#we can also use triple double cot for this purpose.