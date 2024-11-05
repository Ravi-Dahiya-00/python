import random

random.randint(1,4)           #all numbers between 1 and 4 included including 1 and 4

random.randrange(1,4)          # 4 is not included

random.random()              #number between 0 to 1 any float number 

random.uniform(1,3)           #float number between range 1 to 3


l=[1,2,4,6,2123,56,43,34,32,34,4334,4,33]
a=random.choice(l)
print(a)


a=random.shuffle(l)
print(a)



num=random.randint(0,1)
print(num)

if num==1 :
    print("heads")
else:
    print("tails")








#random bill paying code
l=input("enter name separated by comma:")

name=l.split(',')
b=random.choice(name)
print(f"{b}will pay the bill")