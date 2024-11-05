#program to calculate average height from a list of heights.

#conditions
'''1. we will take list from user input.
2. we will not use sum() and len() functions.
3. we can use split() and range() functions.'''


heights=input("enter the heights with space :")
# 151 123 245 123
height_list=heights.split( )                         #this split will break the str from the input we will give in split( ).

count=0                                            #this is used to calculate the length of heights input instead of len() function
for height in height_list:
    count=count+1

for i in range(count):                              
    height_list[i]=int(height_list[i])


total=0
for person in height_list:
    total =total+person

avg=total/count
print(round(avg))






numbers=input("enter lists of number :")

number_list=numbers.split( )


count = 0
for i in range(count):
    count+=1

print("the length of the list is",count)