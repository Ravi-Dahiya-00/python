#range() function

#range(star,stop,step size)

#start is automatically from zero.
#we need to specify where to stop.#if we provide a range 6 it will print upto 5 only.
#step size is default 1 if want a step size of 2 we can directly put here 2.



a=range(2,20,2)
print(a[0])


for i in a:
    print(i)
    

a=range(20,-20,-2)
for i in a:
    print(i)

a="ravi"
print(a[-1,-4])
# this will give empty because we cannot do negative slicing both
a=range(-1,-10,-2)
for i in a:
    print(i)
#step size cannot be zero.



b=range(1,101)
total=0
for i in b:
    
    total=total+i

print(total)








total=0
for i in range(1,101):
    if i%2==0:
        total=total+i
print(total)
