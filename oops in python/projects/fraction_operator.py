class Fraction :
    
    def __init__(self,numerator,denominator):
        self.numerator= int(numerator)
        self.denominator= int(denominator)
    
    def __str__(self):
        return "{}/{}".format(self.numerator,self.denominator)
    
    def __add__(self,other):
        add_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        add_denominator=self.denominator * other.denominator
        return "{}/{}".format(add_numerator,add_denominator)

    def __sub__(self,other):
        sub_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        sub_denominator=self.denominator * other.denominator
        return "{}/{}".format(sub_numerator,sub_denominator)

    def __mul__(self,other):
        mul_numerator=self.numerator * other.numerator
        mul_denominator=self.denominator * other.denominator
        return "{}/{}".format(mul_numerator,mul_denominator)
        
    
    def __truediv__(self,other):
        div_numerator = self.numerator * other.denominator
        div_denominator = self.numerator * other.denominator
        return "{}/{}".format(div_numerator,div_denominator)
        
    
        
input_numerator=input("enter a numerator value : ")
input_denominator=input("enter a denominator value : ")
operation_input=Fraction(input_numerator,input_denominator)

input_numerator1=input("enter a numerator 2 value : ")
input_denominator1=input("enter a denominator 2 value : ")
operation_input2=Fraction(input_numerator1,input_denominator1)
print(type(operation_input))
print(operation_input)

print("addition of fractions",operation_input+operation_input2)
print("subtraction of fractions",operation_input-operation_input2)
print("multiplication of fractions",operation_input*operation_input2)
print("division of fractions",operation_input/operation_input2)

