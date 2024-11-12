# all the functions in ATM we will make will be methods

class Atm :
    
    def __init__(self):
        self.pin=""
        self.balance=0  
        print(id(self))
        
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
        else:
            print("exit")
        
    
    def create_pin(self):
        self.pin = input("Enter your pin :")
        print("pin set successfully")
        
    def deposit(self):
        pin_check=input("enter your pin")
        if pin_check==self.pin:
            deposit_amount=int(input("enter the amount to deposit"))
            self.balance+=deposit_amount
            print("Deposit Successful")
        else :
            print("invalid PIN")
        
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
        
    def check_balance(self):
        pin_check=input("enter your pin")
        if pin_check==self.pin:
            print(self.balance)
        else:
            print("invalid PIN")
    
sbi=Atm()   
sbi