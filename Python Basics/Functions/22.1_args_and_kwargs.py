'''
1.*args:
        it is for arbitrary positional arguments.
 
        
        #in this we can do sum of infinite numbers just by passing * with parameter name.
        def sum(*number):
        
        add(1,2,4,23,724,64)



        # this makes the tuple of the given numbers and we can access the elements from the tuple through for loop.
        
2.**kwargs:
        it is for arbitrary keyword positional arguments.
         
        key:pair
          
           #this makes the dictionary of the given output and we can access the elements from the dicitionary
        
         
        
        def info_person(**information): 
            for key,value in information.items():
                print(key,value)
                
            info_person(name="Ravi",age="17",city="rewari")'''




#for sum of infinite making a function

def sum(*num):
    c=0
    for i in num:
        c=c+i
    print(c)

sum(1,3,2,4,3,4,32,4,2,4,5,3,324,5,4,3,43,34,5,434)






def sum(*num,name1):
    
    print(num)
    print(name1)

sum(1,3,2,4,name1="ravi")











#kwargs function

def user_data(**data1):
    for key,value in data1.items():
        print(key,value)

user_data(name="ram",age="30",dept="cse")
user_data(name="shyam",age="20",dept="llb")




#both args and kwargs
def user_data(*num,**data1):
    for key,value in data1.items():
        print(key,value)
    print(num)
user_data(1,2,3,name="ram",age="30",dept="cse")
user_data(34,54,3,name="shyam",age="20",dept="llb")




#multiply function
def num_multiply(*num11):
    c=1
    for i in num11:
        c=c*i
    print(c)
num_multiply(2,3,-6,8)
num_multiply(2,5,8,9,0,6)