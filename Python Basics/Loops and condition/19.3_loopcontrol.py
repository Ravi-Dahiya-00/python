#break statement :
                #   in this statement if break comes it will stop the for or while loop and come out from the loop
                         #  and in this case no else condition will be printed.

list1=['hii',"hello","welcome"]
names=["ram","krishna","madhav"]

for item in list1:
    for name in names:
        print(item,name)
        if item=="hii" and name=="ram":
            break
    print("out from the inner loop ")
print("out from the outer loop")










#continue statement :
                    #  in this if continue is used the condition then it will restart the loop from the continue it will not execute statement 
                    # below the continue , only one time when the condition is true.
count=1
while count<=10:
    print(count)
    count+=1
    if count==7:
        continue
    print("hii ")
print("out from the  loop")








#pass statement :
                #   null statement

for i in range(1,11):
    pass