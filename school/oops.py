class classname:
    """documentation string
my class"""
    
print(classname.__doc__)


def new_func(__doc__, classname):
    class classname:
        "this is student class with required data"
    print(classname.__doc__)

new_func(__doc__, classname)





class student:
    def __init__(self,name,rollno,marks) :
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def talk(self):
        print("hello my name is:",self.name)
        print("my roll no is:",self.rollno)
        print("my marks are:",self.marks)

s1=student("ravi",35,85)
s1.talk()




class book():
    def __init__(self,title,author):
        self.title=title 
        self.author=author 
        
    def tell(self):
        print("book title is ",self.title)
        print("this books author is ",self.author)

book1=book("The Power","ravi")
book1.tell()







class employee():
    def __init__(self,employee_name,salary) :
        self.employee_name=employee_name
        self.salary=salary
        
    def data(self):
        print("employee name : ",self.employee_name)
        print("employee salary : ",self.salary)
    
    
    
    
    
    
data1=employee("ravi",999)
data1.data()
        