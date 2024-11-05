#basic syntax of for loop

'''for var_name in sequence:
      statement(s)      '''

names = [ "ravi","rahul","jatin","ram"]
for name in names :
    print(name)
    if name:
        print(f"hii {name}")


#it will print name in systematic order one by one and not randomly.
#this is known as iteration.



numbers=[2,3,4,5,6]
squares=[]
for i in numbers:
    square=i**2
    squares.append(square)
    print(squares)                     #this will print one by one with every condition 
print("the list of squares is : ",squares)                         #this will print only one time after completion of for loop.











# for_else in python 

#it is not same to if_else in python because in if_else only one condition is executed
#  it may be if condition or else condition depending on the statement given.  



#but in for_else condition both the condition are executed first complete for condition's loop  will be executed
#  then else condition will be executed .


tuple1= (2,56,76,45,0,34,45,-1,3)

for i in tuple1:
    print(i)
else:
    print("for loop is executed completely.")


#if can also break the for condition in between 

for i in tuple1:
    print(i)
    if i==0 :
        break
else:
    print("for loop is executed completely byy.")

#this time else condition will not be printed because the for loop is not completed it has been break in between.

tuple1= (2,56,76,45,0,34,45,-1,3)

for i in tuple1:
    if i%13==0 :
        print(i)
        
else:
    print("there is no number divisible by 6.")
#now else statement will be executed because for statement is completed successfully.
