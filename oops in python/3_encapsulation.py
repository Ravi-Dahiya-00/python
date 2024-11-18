# what are instance variable ??
# instance variable are those variables of class whose value for every object is different.
#variables that we make in the constructor (__init__) are called instance variable because its value changes for every new object(variable).


'''
    there are something that we want to hide or make it private as no body can use or change that thing outside the class,
        example:    
                when we make a class for ATM we have balance and pin public so anyone can change its value .
                so we can make any method private by using __ two underscore in front of it while declaring any object or data or function.
                
                
    here we are setting updating is not allowed but if you want some changes you have to pass all the condition that are set by me .
    
           '''
           
        

class Atm :
    
    def __init__(self):
        self.__pin=""
        self.__balance=0                # thats how we made these data private .
     
     
     
        
    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin
            print("pin set successfully.")
        else:
            print("only password in string is allowed.")
    
    def get_balance(self):
        return self.__balance
    def set_balance(self):
        return "cannot change the balance"    
    
'''these above all is called encapsulation in python 
    we are doing same thing giving option to other programmer to change the data but by encapsulation method we are giving some condition 
        that will make our code to save from crashes like we have put a condition the pin should be in the the string only.
        
    and in the new function we have made a function to get balance but we made another function to change the balance and here
    we have write balance cannot be changed '''
    
    
sbi=Atm()
sbi.__balance="gvt"
'''
        if we will update like this sbi.__balance="gvt" this will create a new variable name as __balance .
        and that private data will be automatically made like this _Atm__balance by python so there will be no effect on this.
        but if we will update like this sbi._Atm__balance then our code will crash.
        
            conclusion : 
                    nothing in python is truly private.
                    
                python community said this language is made for senior programmers.
                
                                                                    ''' 
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
# reference variable 
'''
    when we are making a variable of sbi=Atm() we say sbi as a object but this statement is not correct 
    
    here sbi is a reference and Atm() is the object and sbi is addressing on the Atm() where actual address is present.
     
    conclusion : 
            while making a object where we store the object in any variable this variable is called as the reference variable.'''