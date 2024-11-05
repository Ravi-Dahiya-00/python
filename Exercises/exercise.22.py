def paint_mug(height,width,area_covering):
    print((height*width)/area_covering)
paint_mug(10,20,1)






# prime_number checker
n=int(input("enter a number : "))
if n%2!=0 and n%3!=0 and n%5!=0 or n==2 or n==3 or n==5:
    print("prime number")
else:
    print("not a prime number")

def prime_checker(n):
    if n%2!=0 and n%3!=0 and n%5!=0 or n==2 or n==3 or n==5:
        print("prime number")
    else:
        print("not a prime number")


prime_checker(11)









#printing name with using loop and manually 

count=1
def printer(name):
    global count
    if count<=10:
        print(name)
        count=count+1
        printer(name)
printer("ravi")