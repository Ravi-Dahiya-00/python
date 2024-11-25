list1=['a','b','c','d','e']
co="True"
a="abcd"
for i in list1:
    if i in a:
        co="True"
        
    else:
        co="False"
if co == "True":
    print("yes")
else:
    print("No")
