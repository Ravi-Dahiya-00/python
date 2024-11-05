d={100:"durga',",200:"ravi",300:"rao"}
print(d)


rec={}
n=int(input())
i=1
while i<=n:
    nmae=input("enter your name: ")
    marks=input("enter %of marks your marks: ")
    rec[nmae]=marks
    i=i+5
print("Name of Student","   ","% of marks")
for x in rec:

    print("     ",x,"   ",rec[x])





#keys()
d={100:"durga',",200:"ravi",300:"rao"}
print(d.keys())
for k in d.keys():
    print(k)











#items
d={100:"durga',",200:"ravi",300:"rao"}
for k,v in d.items():
    print(k,"   ",v)

