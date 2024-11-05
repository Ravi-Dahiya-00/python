import random


print("welcome to the password generator!")
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y,''Z']

numbers=['1','2','3','4','5','6','7','8','9','0']

symbols=['!','@','#','$','%','^','&','*','(',')','~','+','/']


a=int(input("how many letters would you like to add in your password?\nEnter:"))
b=int(input("how many symbols would you like to add in your password?\nEnter:"))
c=int(input("how many numbers would you like to add in your password?\nEnter:"))

password=[]                           #this will make it to the list if we will take string directly we cannot
                                      # shuffle the password.




# for letter selection

for i in range(1,a+1):
    letter_selection=random.choice(letters)
    password+= letter_selection



# for number selection 

for i in range(1,b+1):
    number_selection=random.choice(numbers)
    password+= number_selection



# for symbol selection

for i in range(1,c+1):
    symbol_selection=random.choice(symbols)
    password+=  symbol_selection



# for shuffling the list
random.shuffle(password)


new_pass=""                      #new empty variable for converting the list into the string.


for character in password:
    new_pass+= character

#in this for loop all the characters of the list one by one will be taken and will be converted to the string and added to the new_pass fas a string.

print(new_pass)
