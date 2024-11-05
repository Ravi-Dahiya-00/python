#Round function
'''The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.

The default number of decimals is 0, meaning that the function will return the nearest integer.'''


print(round(7))          #no change because it is int. no decimal place is present.
print(round(7,2))        #no change because there is no decimal as it can round off upto 2 points.
print(round(7.61))       #convert it to the nearest int , nearest int of 7.61 is 8
print(round(2.66666,2))        #this 2 is used to define the last digit of round off this will give 2.67
print(round(2.6657,0))         #this will round off upto o decimal place


# when .5 is present in last , in python it will return nearest even number
print(round(7.5))           #give 8 because nearest even int is 8.
print(round(6.5))           #give 6 because nearest even int is 6.




#some points
print(round(674,2))           #no effect returns 674 
print(round(674,0))           #no effect returns 674



print(round(674,-1))          #this negative(-) will effect some changes

#it gives number that is equal to       10^( -- no. of digits )
                    #let's see here
               #  10^(-*-1) = 10^1 = 10
# this will round off to nearest multiple of 10
# it could be 670 or 680 but 670 is closest so it will be right answer.


print(round(674,-2))
#calculate through formula
# 10^(-*-2) = 10^(2) = 100
#this will round off to nearest multiple of 100.
#it could be 600 or 700 this is closest to 700 so this will be right answer.


print(round(674,-3))
#this will return 1000 we can calculate it by formula.

print(round(274,-3))
#this will give zero


print(round(674,-4))
#if it over exceed it will give 0 always.


print(round(665,-1))
#it will give 660 because in 670 , 67 is not even in 660, 66 is even 
#so it will give 660

print(round(675,-1))
#it will give 680 because 67 is not even , and 68 is even 
#so it will give 680

print(round(-8/3))     
#give -3 because right answer will be -2.6666666666 and then it will round off to -3.

print(round(-8/3,2))
#it will give -1.67 because it will round off upto 2 places.

print(round(-1.5))
#it will round off to nearest even int which is -2.

print(round(6.75,1))
#it will give 6.8 because nearest even int is 6.8.

print(round(6.85,1))
#it will give 6.8 because nearest even int is 6.8.

print(round(674.1014,-1))
#all digits after point will be zero and it will give nearest 10 to the power closest digit.
#so, it will give 670.
