#2.
tuple1 = ('parrot', 'sparrow')
print(type(tuple1))

print(tuple1)
#tuple is a ordered collection of different data types.it can be changed these are immutable.
#we cannot compare any element in the mix tuple like using minimum or maximum function

print(len(tuple1))

tuple2=(11,"ravi",10.23,True,11)
print(tuple2[1])    #indexing any element 
print(tuple2[-2])   # negative indexing
print(tuple2[1:])   #tuple slicing
print(tuple2[::2])


#occurrence of any element in any tuple:
print(tuple2.count(11))


print(tuple2.index(11))

tuple3=(tuple1,tuple2)
print(tuple3)
print(tuple3[1])


tuple7=tuple1 + tuple2
print(tuple7)               #for concatenating tuple1 and tuple2 elements in a single tuple.

tuple4=("ravi")       #this is not a tuple this is a string 
print(type(tuple3))

tuple5=("ravi",)      #if want it to convert into a tuple we have to put 1 comma after this.
print(type(tuple4))


tuple11=(10,)*5        
print(tuple11)        #print 10 5 times.




#converting of a list into a tuple
list1=[1,2,3,5,6,78,9,7]
print(tuple(list1))


#sorted()
# to sort elements based on default natural sorting

t=(59,29,49,29,52,56)
t1=sorted(t)
print(t1)           #converted into ascending order


t1=sorted(t,reverse=True)
print(t1)

print(min(t))        #29
print(max(t))        #59


#tuple packaging and unpackaging

a=13
b=34
v=34
d=13

t=a,b,v,d                   #packi+ng a tuple
print(t)              



t=(10,34,2,23)
a,b,c,d=t
# print(t(a,b,c,d))

a=eval(input("enter numbes:" ))
print(a)
l=len(a)
sum=0
for i in a:
    sum=sum+i
    print(sum)
    print(sum/l)













#tuple objects can be used as key for dictionaries because key should be hashable and immutable
#if content is fixed and can never be changed we should go for tuples.
#tuples objects are immutable we can create  tuple objects we cannot change its content\