# all the functions in ATM we will make will be methods

class Atm :
    
    counter=1          #static/class variable 
    
    
    def __init__(self):
        self.pin=""
        self.balance=0  
        
        
        Atm.__counter+=1
        
        print(id(self))
        

    @staticmethod
    def get_counter():
        return Atm.__counter
    
    @staticmethod                                                      #this signify's that to run these functions we does not require any objects
    def set_counter(new):
        if type(new)==int:
             Atm.__counter=new
        else:
            print("only int objects are allowed.")
        
        
        
        
        
        
        
    
    
    
    
        self.menu()
    
    def menu(self):
        user_input = int(input('''
                           Hello, how would like to proceed ?
                           1. Enter 1 to Create a Pin.
                           2. Enter 2 to deposit.
                           3. Enter 3 to withdraw.
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
                           '''))
        if user_input==1:
            self.create_pin()
        elif user_input==2:
            self.deposit()
        elif user_input==3:
            self.withdraw()
        elif user_input==4:
           self.check_balance()
        elif user_input==5:
            self.exit()

            
            
        
    
    def create_pin(self):
        self.pin = input("Enter your pin :")
        print("pin set successfully")
        
        self.menu()
        
    def deposit(self):
        pin_check=input("enter your pin")
        if pin_check==self.pin:
            deposit_amount=int(input("enter the amount to deposit"))
            self.balance+=deposit_amount
            print("Deposit Successful")
        else :
            print("invalid PIN")
            
        self.menu()
        
    print(id(deposit))
    def withdraw(self):
        pin_check=input("enter your pin")
        if pin_check==self.pin:
                withdraw_amount=input("enter the amount to withdraw")
                if withdraw_amount <= self.balance:
                    self.balance-=withdraw_amount
                    print("Withdrawal Successful")
                else:
                    print("amount is greater then your balance")
        else:
            print("invalid PIN")
        
        self.menu()
        
        
        
    def check_balance(self):
        pin_check=input("enter your pin")
        if pin_check==self.pin:
            print(self.balance)
        else:
            print("invalid PIN")
            
        self.menu()
    
    def exit(self):
        print("thankyou visit again")
    
sbi=Atm()   
# sbi

list1=[]
for i in range(1,11):
    list1.append(i)
    


list2=[1,2,3,4,5,6,8,9,10]

for i in list1:
    if i not in list2:
        print(i)