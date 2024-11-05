class manager:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary


    def data(self):
        print(self.name)
        print(self.department)
        print(self.salary)




data1=manager("Ravi","cse","5000000000000000")
data1.data()








class car:
    def setname(self,name):
        self.name=name


    def getname(self):
        return self.name

car_name=input("car name: ")

honda = car()


honda.setname(car_name)
print(honda.getname())













class student:
    
    def set_data(self,name,age):
        self.name=name
        self.age=age
        
    
    def get_data(self):
        return self.name , self.age
    

student_name=input("student name: ")
student_age=input("student age: ")


student_data= student()

student_data.set_data(student_name,student_age)

print(student_data.get_data())

    
        
    
    
    
    




# class person:
    
#     def setname(self,name):
#         self.name=name
        
        
#     def getname(self):
#         return self.name
    
    
# p1 = person()
# p2 = person()

# name1 = input("p1 : ")
# name2 = input("p2 : ")

# p1.(name1)
# p2.(name2)





    
    
    
    


class car:
    
    def set_engine_model(self,engine):
        self.engine=engine
        
    
    def get_engine_model(self):
        print(self.engine)


class honda(car):
    
    def set_car_model(self,model):
        self.model=model
        
    def get_car_model(self):
        print(self.model)



my_car = honda()



my_car.set_engine_model("sexy_model")
my_car.set_car_model(6969)

print("car details : ")

my_car.get_engine_model()
my_car.get_car_model()
