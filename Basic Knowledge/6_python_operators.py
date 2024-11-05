#using python to perform mathematical computation.

#print(x+y)                          #for addition
#print(x-y)                          #for subtraction
#print(x*y)                          #for multiplication
#print(x/y)                          #for division

#python can be used  for addition,subtraction,multiplication and division.





#precedence and associativity in python 

#  operators have different levels of precedence, which determine the order in which they are evaluated. 

#PEM-DAS        it is the algorithm to calculate the mathematical operations 
#1.     ()                                parenthesis
#2.     **                                power operator                                                          right<--left
#3.     *  /   //   %                    multiplication,division,floor division,modules                           left-->right
#4.     +   -                             addition,subtraction                                                    left-->right



#associativity in python
print(5+2*3-1+10/5)
#here both multiplication and division are present in the same statement. now we will use associativity here.

#we will move left to right in 3rd and 4th 
#we will move right to left in 2nd 

#which will come first it will be operated first.
#in that first               multiplication  >>  division  >>  addition  >>  subtraction

 



#the best way is to use parenthesis after every operator it will be time consuming but give less errors.
#if we need some fix output from the same digits parenthesis will be required.


#if we want 11 from the same digits we will use it like this:
print(((((10+5)/3)+5)+2)-1)










#for addition we use + sign in between the two numbers.
print(5 + 6)

x=int(input("enter your first number:"))
y=int(input("enter your second number:"))
print(x+y)



#this + is used to concatenate a string and a number here.
# + can also be used for concatenate a string and a number.
b="1"
print("b=" + b)








#for subtraction we use - sign in between the two numbers.
print(7 - 3)

p=int(input("enter your first number:"))
q=int(input("enter your second number:"))
print(p-q)              

#we should take different variable for different calculation of different numbers.
#we can continue with same variable if want all calculation for the same number.



#for multiplication we use * sign in between the two numbers.
print(34 * 56)
print(p*q)




#for division we use / sign in between the two numbers.
print(32 / 4)
print(p / q)

#compute expression
#computeExpression.py

print((10.5 + 2*3) / (45 - 3.5))

print(2 + 8)  #addition of two numbers. +
print(9 - 5)  #subtraction of two numbers. -
print(5 * 3)  #multiplication of two numbers. *
print(5 / 3)  #division of two numbers. /
print(
    7 // 2                                #output=3
)  #floor division of two numbers. //    used to calculate approx division of two numbers.  
print(
    5 % 3                                 #output=2
)  #modulus of two numbers. %    used to calculate reminder of two numbers.
print(
    5**3                                  #output=125
)  #exponential of two numbers. **    used to calculate power of two numbers.














#assignment operator
a=5
a=a+2
a+=2       #it is same as a=a+2

a=a/2
a/=2       #it is same as a=a/2


a,b,c,d=2,3,4,5
print(a,b,c,d)







 
#conditional operators or comparison operators

# > , < , >= , <= , == , !=
a=18
print(a>18)        #it is true only when a is greater then 18.
print(a<18)        #it is true only when a is smaller then 18.
print(a<=18)       #it is true only when a is less than or equal to 18.
print(a>=18)       #it is true only when a is greater than or equal to 18.
print(a==18)       # it is true only when a  is equal to 18.
print(a!=18)       # it is true only when a is not equal to 18.
print((a+2)!=18)   #we can also add something to it while giving an operation.















#logical operators
#Python logical operators are used to combine conditional statements, allowing you to perform operations based on multiple conditions.
#1. and 
#2. or 
#3. not 



#and 
a,b=5,4
print(a>4 and b<10)    #true
print(a>4 and b<3)     #false

#for and operator if all the statement are true then it will give true,
#if one of them is false then it will give false.



#or
a,b=5,4
print(a>4 or b<10)    #true
print(a<4 or b<13)    #true

#for or operator when 1 or more statement is true it will give true.
#if no statement is true only when it will give false.

#not 
a=False
print(not(a))    #print true.


''' X                       Y                       X and Y               X or Y                 not(X)                    not(Y)
    
1.  true                   true                      true                  true                  false                     false
2.  true                   false                     false                 true                  false                     true
3.  false                  true                      false                 true                  true                      false
4.  false                  false                     false                 false                 true                      true  '''













#number conversion binary to decimal and vice-versa


#decimal number is having base = 10   ex=(123)10

#binary number is having base = 2     ex=(123)2



#formula
#   N...........16        8          4             2            1



#we have to write this series of this formula upto when the digits of the binary number is not finished.
#we have to ignore all the numbers of the series which is getting 0 under this series.
#we have to take all the numbers of series of only one.
#then take all the numbers of the series which is getting one.
#now sum all the numbers of the series which are above one.


#binary to decimal

#convert 1101010 to decimal 

# (1101010)2=  ()10



#now solve this 

#  1            1              0          1            0               1                 0
#  64           32             16         8            4               2                 1


#now forget all the numbers of series which are getting zero above it.
#take all the numbers of series of one and sum all the numbers.

#  64+32+8+2=106 
#the decimal of 1101010 is 106.











#decimal to binary.

#convert 16 to binary


#    16            8            4             2              1
#    1             0            0             0              0

#binary of 16 is 10000




#convert 19 to binary


#    16             8              4                2                1
#     1             0              0                1                1

#binary of 19 is 10011

#we have to put one on those numbers that can make the sum equal to that number which we are converting to binary.





#bitwise operators

# Bitwise operators are used to compare (binary) numbers:

'''Operator	Name	                Description	                                                               Example	


& 	AND	                              Sets each bit to 1 if both bits are 1                                    x & y	
                                       if one is zero then it will give zero.

|	OR	                              Sets each bit to 1 if one of two bits is 1                    	         x | y	
                                        only give 0 when both are zero.

^	XOR	                              Sets each bit to 1 if only one of two bits is 1	                         x ^ y	
                                        it will give zero when both are 0 or 1 in same row

~	NOT(Compliment)                              	Inverts all the bits	                                       ~x	
                                                   0 to 1 and 1 to 0

<<	Zero fill left shift          	  Shift left by pushing zeros in from the right and 
                                      let the leftmost bits fall off	                                         x << 2	

>>	Signed right shift	          Shift right by pushing copies of the leftmost bit in from the left,
                                    and let the rightmost bits fall off                                       	x >> 2	'''





#1. AND bitwise operator

a=5
b=4
print(a&b)

#let's see how this print statement will be calculated.

#firstly this are converted into binary
#     a   =    0   1    0    1                #5 in binary form
#     b   =    0   1    0    0                #4 in binary form

#    a&b  =    0   1    0    0                a&b in binary form
'''only the place where a and b are having 1 that will be written as 1
 and where in only 1 is there that place is written 0 '''

#now convert this 0100 into decimal form 
# 8          4         2             1
# 0          1         0             0

#decimal form of this 0100 is 4.
# so the output of the print(a&b) will be 4.







#2. OR bitwise operator
a=5
b=4
print(a|b)

#let's see how this print statement will be calculated.

#firstly this are converted into binary
#     a   =    0   1    0    1                #5 in binary form
#     b   =    0   1    0    0                #4 in binary form

#    a|b  =    0   1    0    1                a|b in binary form
'''if only place is having 1 then it will be written as zero
  zero will be return only when there are both zeroes in same line'''

#now convert this 0101 into decimal form 
# 8          4         2             1
# 0          1         0             1

#decimal form if this 0101 will be 5
# so the output of the print(a|b) will be 5.





#3. XOR bitwise operator
a=5
b=4
print(a^b)

#let's see how this print statement will be calculated.

#firstly this are converted into binary
#     a   =    0   1    0    1                #5 in binary form
#     b   =    0   1    0    0                #4 in binary form

#    a^b  =    0   0    0    1                a^b in binary form
'''it will give one only when both bits are different in same row.
gives zero when both are same bits '''
#now convert this 0001 into decimal form 
# 8          4         2             1
# 0          0         0             1

#decimal form if this 0001 will be 1
# so the output of the print(a^b) will be 1.







# in binary form 

#   0+0=0
#   0+1=1
#   1+0=1
#   1+1=0 with carry remain 1 and it is added in the next.




#4. NOT(compliment) bitwise operator
a=5
print(~a)

#let's see how this print statement will be calculated.

#   5    =   0     1        0          1
#  ~5    =   1     0        1          0

# 2's = 1's + 1   (2's is compliment of 2)
#2's because 6 in binary form is written as          0    1     1     0
#1's in binary form will be written as               1    0     0     1
#one will also be added because 1 is also is 2's                      1
                                            
#this is - 6 stored in binary form                   1   0      1      0




#short trick is that always add 1 in a and put - sign this will be NOT of that a.
# a=8
# print(-8)   #this will give -9.





































#identity operators 
''' identity operators are used to compare the objects, not if they are equal, but if they are actually the same object,
 with the same memory location:'''



'''Operator              	Description                                                                     	Example	
  is             	          Returns True if both variables are the same object	                               x is y	
  is not	                  Returns True if both variables are not the same object	                           x is not y	'''



a=5
b=5
        #python will make same memory location for both a and b because they are containing same value.

print(a is b)         #returns true because these are same objects
print(id(a))
print(id(b))          #id of a and b will be same.


a=5
b="5"
print(a is b)          #returns false because a is int and b is str and have different id.
print(a is not b)      #returns true because these are not same.


a=5
print(id(a))
a=8
print(id(a))
print(a is a)          # it will give true because it will not compare 1st a with 2nd a.
                       # it will compare a with itself.











#Membership Operators
'''Membership operators are used to test if a sequence is presented in an object:

Operator                     	Description	                                                                   Example	
in                            	Returns True if a sequence with the specified value
                                 is present in the object	                                                     x in y	

not in	                        Returns True if a sequence with the specified value
                                is not present in the object                                                 	x not in y	'''


str="jenny"
print('y' in str)                   #true
print('nny' in str)                 #true
print('Y'  in str)                  #false
print('Y' not in str)               #true
print('e' not in str)               #false





list=['hello',10,5,9]
print('e' in list)                #false because it will check only elements in list that is hello,10,5,9
print('hello' in list)            #true
print(10 in list)                 #true
print(4 not in list)              #true because for is not present in list
print(8 in list)                  #false