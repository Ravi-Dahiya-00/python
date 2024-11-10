D = {"name":"Ravi","gender":"male","age":18}

print(D.items())

D1 = { key:value for key,value in D.items() if len(key)>3}    
print(D1)





l=[1,2,3,4,5,6,7,8,9]

D2 = {item:item**2 for item in l if item%2==0}
print(D2)
