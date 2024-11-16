# using code of one class into the other class without rewriting the code is called as inheritance in oops.
 
class my_skills:
    
    def my_skill1(self):
        print("this is my_skills class method.")
    

class student(my_skills):         # we have to just pass the class name here to use the data of that class
    pass
obj_student = student()          #here we have made the object for student.
obj_student.my_skill1()          # by making the object of the student it has already defined the my_skills class.
#we can directly use this my_skills class function just by putting my_skills in student without writing its code again.

 
'''this complete method is called inheritance 
student(my_skills) here we have inherited my_skills properties or function in student class. 

here my_skills is parent class and student is child class.'''







class mentor :
    class_var = 20
    def __init__(self,mentor_name,mentor_email,mentor_contact):
        self.mentor_name=mentor_name
        self.mentor_email=mentor_email
        self.mentor_contact=mentor_contact
        
    def print_mentor_details(self):
        print(self.mentor_name,self.mentor_email,self.mentor_contact)
        
class cse(mentor) :
    def print_cse(self):
        print("this is my cse class")
        

obj_cse = cse("Devansh","Devansh@lpu.in",332032903)

print(obj_cse.mentor_name) 
print(obj_cse.mentor_email) 
print(obj_cse.mentor_contact) 

obj_cse.print_cse() 

print(obj_cse.class_var)