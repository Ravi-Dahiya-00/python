# from atm_machine import Atm

# reference variable 
'''
    when we are making a variable of sbi=Atm() we say sbi as a object but this statement is not correct 
    
    here sbi is a reference and Atm() is the object and sbi is addressing on the Atm() where actual address is present.
    
    conclusion : 
            while making a object where we store the object in any variable this variable is called as the reference variable.'''
            
# sbi=Atm()                    #sbi is reference variable and Atm() is its object.






# pass by reference
class Customer :
    
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        
        
'''here we are making another function and passing a reference in it with class so this tells us that we can also pass a reference in it
as we pass int,str,list because at last everything in python is object.'''
 
def greet(customer):
    if customer.gender=="Male":
        print("Hello",customer.name,"Sir.")
    elif cus.gender=="Female":
        print("Hello",customer.name,"Ma'am.")
    else:
        print("Hello",cus.name)
        
        
    cust2=Customer("Ravi","Male")
    return cust2
cus = Customer("Amit","Male")
new_cust=greet(cus)

print(new_cust)
'''
    Conclusion:
            we can pass the object made by our class as an argument in the function.
            and function can also return that object'''











class customer1:
    
    def __init__(self,name):
        self.name=name
        
def greet(customer):
    customer.name="Ravi"
    print(customer.name)


cust=customer1("ankita")
greet(cust)
print(cust.name)

# if have pass a object to a function and that function is changing the value of that object.
# this happens because both cust and customer are pointing towards the same object.






 # class objects are also mutable like lists,dictionaries and sets.
 
 
 
#  while giving a list to class always provide by cloning it will not affect the original list.
# L1[:] 

# mutable will change and immutable will not change.