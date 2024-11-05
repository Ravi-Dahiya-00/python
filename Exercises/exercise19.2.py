# fizz buzz question

#print 1 to 100 numbers
#for number divisible by 3 print fizz
#for number divisible by 5 print buzz
# for number divisible by both 3 and 5 print fizz buzz


for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
        
