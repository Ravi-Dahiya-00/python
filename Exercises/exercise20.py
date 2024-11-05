row1=[1,1,1]
row2=[1,1,1]
row3=[1,1,1]
matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("enter the position where you want to hide your money: ")
row_number=int(position[0])
column_number=int(position[1])
row_selected=matrix[row_number-1]
column_selected=row_selected[column_number-1]='x'
print(f"{row1}\n{row2}\n{row3}")










# rock paper scissor

import random
a= " 0 for scissor"
b="  1 for paper"
c="  2 for rock"
print(a,b,c)
user=int(input("enter a number among 0,1,2:"))

comp= random.randint(0,2)
print("computer choices :",comp)

if user==comp:
    print("match draws.play again")
elif user==0 and comp==2:
    print("computer wins")
elif user==0  and comp==1:
    print("user wins")
elif user==1 and comp==0:
    print("computer wins")
elif user==1 and comp==2:
    print("user wins")
elif user==2 and comp==0:
    print("user wins")
elif user==2 and comp==1:
    print("computer wins")
else:
    print("wrong output select only 0,1,2")










total=0
for i in range(0,101):
    if i%2==0:
        total=total+i
    elif i==1:
        total=total+i
    elif i==100:
        total=total+i
print(total)