#learn 
''' complexity - time,space big 0 omega'''







a=input("enter your name : ")
def wish(a):
    print("HELLO",a)
wish(a)



def add(x,y):
    return x+y
result=add(10,20)
print("the result is " , result)
print("the sum is " , add(100,200))


def even_odd(num):
    if num%2==o:
        print(num,"is Even number")
    else:
        print(num,"is odd number") 
        




def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y=sum_sub(100,50)
print("the sum is:",x)
print("the sub is:",y)



#VARIABLE LENGTH ARGUMENTS:
def sum(*n):
    total=0
    for n1 in n:
          total =total+n1
          print(total)



def f1(n1,*S):
    print(n1)
    for s1 in S:
        print(s1)


def display(**kwargs):
    for k,v in kwargs.items():
        print(k,"=",v)
display(n1=10,n2=20,n3=30)
display(rno=100,name="durga",marks=70,subject="java")







#function,module,library:
# 1. A group of lines with some name is called a function.
# 2. A group of function saved to a file is called function.
# 3. a group of modules is nothing but library.








#global keyword:
# 1. to declare global variable inside function
# 2. to make global variable available to function so that we can perform required modification.

a=10
def f1():
    a=777
    print(a)


def f2():
    print(a)

f1()
f2()









a= 10
def f1():
    a=777
    print(a)
    print(globals()["a"])












#recursive function
#a function that calls itself is known a recursive Function.


# factorial(3)=3*factorial(2)

def factorial(n):
    if n<0:
        print("factorial is not defined")
    fact = 1
    for i in range(1,n+1):
        fact = fact * 1
    return fact 


#lambda function
n=2
lambda n:n*n 




s=lambda n:n*n
print(s(4))
print(s(5))



s= lambda a,b:a+b
print(s(10,20))
a=int(input())
b=int(input())
print(s(a,b))








# 



l=[0,5,10,15,20,25,30]
l1=list[filter(lambda x:x%2==0,l)]
print(l1)
l2=list(filter(lambda x:x%2!=0,1))
print(l2)






def square(x):
    def cube(y):
        return y**3
    return cube










#recursion function
n=int(input())
def fun1(n):
    if n > 0:
        print("fun1:" , n)
        fun2(n-1)


def fun2(n):
    if n > 0:
        print("fun2:" , n)
        fun3(n-1)

 
def fun3(n):
    if n> 0:
        print("fun3:", n)
        fun1(n-1)






























































































