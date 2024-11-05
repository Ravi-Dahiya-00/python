# #we have to take a two or more digit number from the user and add all the digits of the number by using addition.

x=input("enter a two digit number:")
a=x[0]
b=x[1]

sum=int(a)+int(b)
print(sum)








# # BMI calculator using for finding underweight or overweight.



# #formula=(weight/height**2)

# #taking users weight and height input
weight=float(input("enter your body weight in kilograms:"))
height=float(input("enter your body height in meter:"))

# #now we have both value of weight and height but remember that these values are in string . first convert them into int value .
# #we can also convert  them directly using int while making BMI operator 
BMI=weight/height**2
print(BMI)

if BMI <18.5:
    print(f"your BMI is {BMI} and you are underweight.")
elif BMI<25 :
    print(f"your BMI is {BMI} and you have normal weight.")
elif BMI<30 :
    print(f"your BMI is {BMI} and you are overweight.")
elif BMI<35 :
    print(f"your BMI is {BMI} and you are obese.")
else:
    print(f"your BMI is {BMI} and you are clinically obese.")








#finding leap year using if elif and else condition.

#input of  a year
#if year is divisible 4.
     #if it is divisible 4 
     # then check it is it divisible by 100 or not.
     #if no then it is nota ;leap year.
     #if yes then check is it divisible by 400.
     #if no then not a leap year
     #if yes then it is a leap year.
#if year is not completely divisible by 4 then print it is not a leap year.

year=int(input("enter a year : "))
if year%4==0 :
    if year%100==0 :
        if year%400==0 :
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("not a leap year")
else:
    print("not a leap year")
    










#pizza ordering program
size=input("which pizza do you want to take?? S/M/L")
bill=0
if size=="S":
    print("price for small pizza is 100rs")
    bill=100
elif size=="M":
    print("price for medium pizza is 200rs")
    bill=200
else:
    print("price for large pizza is 300")
    bill=300
peprino=input("do you want to add peprino?? yes/no")
if peprino=="yes":
     if size=="S":
       print("extra charges for peprino is 30rs for small")
       bill=bill+30
     else:
         print("extra charges for peprino is 50rs for medium and large")
         bill=bill+50
cheese=input('do you want extra cheese?? yes/no')
if cheese=='yes':
    print("extra charge for cheese is 20rs for small medium and large pizza")
    bill=bill+20
print(bill)
    

















#Love calculator

a=input("enter your name : ")
b=input("enter your crush name : ")

a=a.lower()
b=b.lower()

c=(a+b)

d=c.count('t')
e=c.count('r')
f=c.count('u')
g=c.count('e')

true= d+e+f+g


h=c.count('l')
i=c.count('o')
j=c.count('v')
k=c.count('e')

love=h+i+j+k

love_score=str(true)+str(love)
print(f"you are in {love_score} percent love with your partner.")
if love_score<40:
   print('this is not good.')
   print('increase your love towards your partner.')
elif love_score<80:
   print('you are in good in love with your partner.')
else:
   print("you have true love with your partner.")
