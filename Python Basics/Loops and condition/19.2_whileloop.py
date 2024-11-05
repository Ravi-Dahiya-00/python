# while loop in python


'''while condition/expression:
    statement(s)    
            '''


count=1
while count<=5:
    print(count)                   
    count+=1                          #if we will not use this it will be infinite loop because every time count=1 and statement is always true.

list1=[1,4,2,4,2,1]
while list1:
    print("hii Ravi")
    list1.pop()                     #this will start removing items from the list1 one by one and when the list will be empty statement will be stopped.








#while loop with else

''''

while condition:
    statement(s)
else:
    statement
    
    '''

#this else statement will be executed only if the while condition is false.
#if we break the while loop condition  in between the else block will not be executed.


count=1
while count<=5:
    print(count)
    count+=1
else:
    print("this else statement is printed because count becomes 6 and condition becomes false. ")




count=1
while count<=5:
    print(count)
    count+=1
    if count==3:
        print("this will break the while loop in between.")
        break
else:
    print("this else block will not be executed because we have break the statement in between and the while loop was not completed. ")








total=0
number=int(input("enter a number:"))
while number<=1:
    print()



count=1
while count<1:
    print(count)
    count+=1
else:
    print("hii")
print("hello")