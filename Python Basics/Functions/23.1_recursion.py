#multiply simple  function
def multiply(a,b):
    
    result=0
    
    for  i in range(b):                             # b = 4  range(0,4)
        result=result+a 
    
    print(result)
    
multiply(6,4)



#multiply recursive function 

def multiply(a,b):
    
    if b==1:
        return a
    else:
        return a + multiply(a,b-1)
    
    
print(multiply(4,5))










# palindrome problem using  recursion

#palindrome strings - madam , level , racecar


def palindrome(str):
    
    if len(str)<=1:
        print("palindrome")
    
    else:
        if str[0]==str[-1]:
            palindrome(str[1:-1])
        else:
            print("Not a palindrome")


palindrome("madam")
palindrome("rao")












# the rabbit problem


'''

if 2 new born rabbits are put in a pen , how many rabbits will be in the pen after 1 year ??


assume that the rabbits 
            always produce one male and one female offspring 
            can reproduce once every month 
            can reproduce once they are one month old 
            never die!!!
            
'''

#fibonacci series is used in this 
# next number will be equal to the sum of last two numbers 

import time
def count(a):
    if a==0 or a==1:
        return 1
    else:
        return count(a-1) + count(a-2)
    
start=time.time()
    
print(count(34))


print(time.time()-start)

''' using recursion is not a good sign of programming for  making projects if we will give some large value 
 it will take so much time to complete that it can take upto hours also we must use loops for completing 
 this tasks but we have also a method to solve this issue. '''
 
 
 
#  Memoization - this method is called memoization
'''the method is that storing the value in the dictionary and using it , this will save our time as we need not 
 to calculate the same thing again we can directly use it from the dictionary but this will do memory allocation.'''
 


def memo(m,d):
     
    if m in d:
         return d[m]
    else:
        d[m]=memo(m-1,d) + memo(m-2,d)
        return d[m]
     
d={0:1,1:1}
start=time.time()

print(memo(48,d))

print(time.time()-start)
