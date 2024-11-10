# we need class to define the different functionalities of our project in different classes.

# syntax of class
class example :                  #here class is to define class and example is the name of the class
    pass


def my_skills1():
    print("we can access it directly by calling the function")
my_skills1()


#but we can not directly access a function or anything that is defined in the class 

# first we to create the variable of the class and then access that  variable.

class my_class :
    class_var = "this is without function"
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
 
b.welcome_msg1()
b.class_var
# this () is used only while calling something like function.
a = 10
# in this a is variable or instance or a object of a integer class .







class course:
    
    def __init__(self,course_name,duration,mentor):
        self.course_name= course_name
        self.duration= duration
        self.mentor= mentor

        # here self is a pointer and we have made 3 variables here.
        ''' __init__ is a inbuilt variable it work is to provide data this is called as a constructor.
        it will provide data to class
        '''
    def show_mentor(self):
        print(f"mentor name is {self.mentor}")

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

