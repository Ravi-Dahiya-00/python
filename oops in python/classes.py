
# we need class to define the different functionalities of our project in different classes.

''' object is always of a class.

  in python , data type is a class 
            and the variable of that data type is a object  of that class .'''
L=[1,2,3,4]                   #this L is a object of the (List) class.
 
 
'''
Class is a blueprint, blueprint of how an object will behave.

        CLASS consist of two things :
                1. Data or Property or attribute   :: description of the object.
                2. Functions or behavior or method'''

# syntax of class
class example :                  #here class is to define class and example is the name of the class
    pass



#basic structure of Class

class Car :
    color="blue"               #data
    model="sports"            #data
    
    def calculateAvgSpeed(km,time):          #function or its behavior
        pass
        #some code 
        
        
''' while making a Class name should be in Pascal Case
 ThisIsPascalCase
 
 function name and data name must be in snake case
 this_is_snake_case
 
 '''

'''
making a class
   Class
   Attributes
   Methods
   
   in general method is data so it is private on;y to the class.    representation(-)
   methods are public to the whole code.     representation(+)'''
   
   
'''
 Object is an Instance of the Class.
 
 Examples of Object : 
    Car(class)---------------->   swift(object)   //  swift=Car()
    Sports(Class)-------------->   cricket(object)    // cricket=Sports()
    
    Dog=Animal()     this is how objects are created in python'''



'''
Functions vs Methods
           1. methods are the special function thar are written inside the class.
            
           2. len(L)        this is a normal function anyone can use this function
              L.append(1)    this append is the function that is defined under the List class.
              
            Function is generally available for everyone and anyone can call it.
            Method is a function that is particularly defined in class and only the object of that class can access it. '''
            
            

def my_skills1():
    print("we can access it directly by calling the function")
my_skills1()


#but we can not directly access a function or anything that is defined in the class 

# first we to create the variable of the class and then access that  variable.

class my_class :
    class_var = "this is without function so this called as data"
    def welcome_msg1(self):
        print("welcome to oops")
# while writing a function in a class we have to assign a pointer or a reference
# here self is referring to itself here self is a pointer
# It represents the instance of the class itself and allows access to its attributes and other methods
# self is not a keyword this is used by python community
 
b = my_class()    
# this b is variable.
# this is called as instance or object of my_class class.
# by this we can access anything from the function.
# without making object we cannot access anything.

n= my_class()
# we can make unlimited variables. 
 
print9=(b.welcome_msg1())
print(n.class_var)
# this () is used only while calling something like function.
a = 10
# in this a is variable or instance or a object of a integer class .





'''while declaring a variable inside the class we always do __init__ 
and in input it gets self and then we declare our variables 
    
    class A:
    def __init__(self):
        self.pin=""
        self.balance=0             '''


class course:
    
    def __init__(self,course_name,duration,mentor):
        self.course_name= course_name
        self.duration= duration
        self.mentor= mentor
    def show_mentor(self):
            print(f"mentor name is {self.mentor}")
            
            
        # here self is a pointer and we have made 3 variables here.
''' __init__ is a inbuilt variable it work is to provide data this is called as a constructor.
        it will provide data to class
        
        constructor is a special method in which the code automatically executes when the object of that class is made.
        
        __init__ is a magic method. if in the starting we have __ and at end also we have __ so this magic method for python.
        these are automatically called , these are not called by any any object.
        
        
        here constructor is called when a object is being created.
        
        like in the below example we have all the methods of data1 to call but do not have the method to call the constructor.
        because user is not having the control or button to constructor.
        
        in constructor we will write that code when we do not want to rely on the user for some task ,
        we will do it automatically.
        
        like to connect to gps,location,internet in any app without asking user because these are necessary task to run our app,
        when user will open the app the constructor code automatically runs.
          
        '''
        
'''
self :
    everything in python is object so self must also be a object.
    if we will see id(self) and id(data1) these will be same means :
                            data1 is self.
                            data1 hi self hai
                            
    
    self address will change every time for different data.
    
    conclusion:
            with that object currently we are working that is self.
            
    why self is required??
    when we call something like data1.course_name() it takes data1 as an argument,
    but in real we have not provided any argument to it , so in the place of self data1 will be passed ,
    so self is required.
    
            
'''
    
'''
in class data and methods can only be accessed by object,means one method also can not access any method from that class. 

so we need a object for it , when the object is taking data1.course_name it is taking through self.
    '''

data1 = course("CSE",4,"Devansh")
data2 = course("MBA",2,"Ravi")
'''
if we are declaring constructor . so we have to remember that which parameters we are providing to __init__
we have to provide the value of all the parameters while calling that class'''
#constructor : through which we can pass data whenever the object of that class is declared or created.


print(data1.course_name)
print(data2.course_name)
# we can call the different data by providing its variable with the parameter name.

'''
if i will change the name self.course1 and call as self.course it will give an error.
it will understand only that thing that is associated to self.
'''

# we can access a functions data in another function.
data1.show_mentor()
data2.show_mentor()  

# while calling a function inside the class we will use (self.variable).
# while calling we will just pass object and  the name of the variable (object.variable).

