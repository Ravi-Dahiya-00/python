''' conditional statements are the statements where we write some condition
 if it happens write these 
 else write this.'''


#it can also be written as
#if(height>3):
if height>3:
    print("buy Token")
    print("now you can in metro")
else:
    print("no token required")
print("this is not the part of indentation so it will be printed if any of statement will be printed")
print("it can not be used in between if and else condition because it will break the condition statement after if condition  and no else condition will be taken after that if.")







number= int(input("enter a number"))

if number%2==0:
    print("it is even number")
else:
    print("it is odd number")







#nested if else and elif

#problem
#can ride if height is greater than 3
#pay 150rs if age is less than 12
#pay 250rs if age is less than or equal to 18
#pay 500rs if age is greater than 18
#if height is less then 3 than cannot ride


height=int(input("Enter your height:"))
if height>3:
    print("you can ride")
    age=int(input("enter your age"))
    if age<12:
        print("pay 150 rs")
    elif age<=18:
        print("pay 250 rs")
    else:
        print("pay 500 rs")
else:
    print("you cannot ride")
print("thank you for visiting our shop")


#we can also make condition under the else part.
#it is not necessary to create the condition under the if part.





#1.we can use as many elif as many condition we want to make under the if condition.

'''2.we can also use as many if condition as many we want to make a condition it will work properly but it is not right way to do this because 
   it will scan all the if conditions and it is not a efficient.'''

number=int(input("enter a number between 1 to 4:"))
if number==1:
    print("one")
if number==2:
    print("two")
if number==3:
    print("three")
if number==4:
    print("four")
else:
    print("you did not enter number between 1 to 4")









a=int(input("enter a number:"))
if a%2==0:
    print("even")
    if a>30:
        print("number is greater than 30....great!!")
print("byy")

#second condition will be checked only if first condition is true.





#multiple if statements
#we can use multiple if statements to evaluate multiple conditions as we have shown in the above problems.
#this if checks the statement in all the conditions so this is not a good method.


#lets see one more problem
height=int(input("Enter your height:"))
bill=0
if height>3:
    print("you can ride")
    age=int(input("enter your age:"))
    if age<12:
        print("ticket price is  150rs")
        bill=150
    elif age<18:
        print("ticket price is 250rs")
        bill=250
    else :
        print("ticket price is 500rs")
        bill=500
    
    photo=input("do you want to take photos yes or no.")
    if photo == "yes":
        bill=bill+50
    print(f"your total bill is {bill}")
else:
    print("cant ride")

    