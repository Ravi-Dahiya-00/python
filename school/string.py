# s=input("enter a name : ")
# i=0
# for x in s:
#     print("the character present at positive index {} and negative index {} is {}".format(i,len(s),i))
#     i=i+1









s="Learning python is very very easy!!"
print(s[1:7:1])
print(s[1:7:2])
print(s[:7])
print(s[7:])
print(s[::])
print(s[:])

print(s[5:-1:-1])



""" 1. s[begin:end:step]
    2. step value can either be positive or negative.
    3. if +ve then it should be forward direction(left to right) and we have to consider begin at end -1.
    4. if -ve then it should be backward direction(right to left) and we have top consider begin at end +1.
    
     
    **note** :
        in the backward direction if end value is -1 then result is always empty.
        i the forward direction if end value is0 then result is always empty .
         
          
    
     # IN Forward direction  :
                                default value begin: 0
                                default value for end : length of string 
                                default value for step: +1  
    
      
        
    # IN backward direction: 
                                default value begin: """




s="Learning python is very very easy!!"
for i in s:
    print(i,end=" ")

for i in s[::]:
    print(i,end="")

for i in s[::-1]:
    print(i,end="")







city = input("enter your city Name:")
scity=city.strip()
if scity=="hyderabad":
    print("hello Hyderabadi..adab")
elif scity=="chennai":
    print("Hello Madrasi...vanakaam")
elif scity=="bangalore":
    print("Hello kannadiga..shubhodaya")
else:
    print("out of range")





s="Learning python is very very easy!!"
print(s.find("python"))
print(s.find("java"))
print(s.find("r"))
print(s.rfind("r"))





s="durgaravipavanshiva"
print(s.find("a")) 
print(s.find('a',7,15))
