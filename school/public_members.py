#public methods

class test:
    def __init__(self):
        self.x=10
        
    def m1(self):
        print("public M1 method")
        
    def m2(self):
        print(self.x)
        self.m1()
    
t=test()
t.m2()
print(t.x)
t.m1()


#private method

class student:
    def __init__(self,name,roll_no):
        self.__name=name
        self.__roll_no=roll_no
        
    def m1(self):
        print(self.__name)
        print(self.__roll_no)
        

    
s= student("Ravi",35)

s.m1()
s.__name











