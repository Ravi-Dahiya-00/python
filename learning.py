


from builtins import complex, input, int, len, print
from typing import TYPE_CHECKING, SupportsComplex                           #this are inbuilt function in  python  and used for not showing an error.





































#indexing in python
#in python,string is like an array of characters.(array=collection of items)
#we can access parts of string by using its index which starts from 0.
#square brackets can be used to access elements of the string.


#example of indexing
name="ravi"
print(name[0])
print(name[1])
print(name[2])
print(name[3])


#print(name[4]) 
#throws an error because index 4 doesnot exist in this name.

#looping through the string
#we can loop through string using a for loop like this:
#example of looping through the string

print("lets use a for loop\n")

name="ravi"

for character in name:
    print(character)


#slicing string and operation on string
#what is string slicing????
#length of a string can be found using len() function.
#we can find the length of a string using len() function.

#example of string slicing
name="ravi"
print(len(name))

#counting in python starts from 0 not from 1 .


fruit="mango"
len1=len(fruit)
print("mango is a ",len1,"letter word.")

#string as an array
#a string is essentially a sequence of characters also called an array.
#thus we can access the elements of this array.
#example of string as an array
pie="applepie"
print(pie[0:5])  #this will print the first 5 letters of the string.
#including 0 but not 5.



print(pie[:5])    # it is not neccesary to write 0 in the starting.
#python automattically adds 0 in the starting.


print (pie[1:5])   #it will not print the 0th letter that is A .
#it  will print the first letter that is P.
#including 1 but not 5.


print(pie[6])    #this will only print the 6th letter of the string.



#negative slicing in python
#we can also use negative slicing in python.
#it is similar to positive slicing.
#but the counting in negative slicing starts from the end and -1 is added in the ending.



#example of negative slicing
pie="applepie"


print(pie[0:-3]) #it will subtract the 3 letters from the end of the string.

#python will consider it like this:
print(pie[0:len(pie)-3])


# both the  above things are same and have same output.


#when we will change sign of both the numbers.

print(pie[-1:-3])   

#python will consider it like this:
#6:3
#there is no sense in this.
#so python will not print anything.



#if if interchange the numbers.

print(pie[-3:-1])
#python will consider it like this:
#3:6
#so python will print the letters from 3 to 6.
#but it will not print the 6th letter that is E because
#it is not included because of the negative slicing.

nm="harry"
print(nm[-4:-2])

#if it is positive slicing or negative slicing 
#python will print the first number written but not the second number written.
#it uses n-1 for writting the second number.


#strings are immutable
#a string in python cannot be changed.
#but strings can be replaced by new strings.
#it can be done by using string methods.


#string methods in python:
#python provides a set of built-in methods that we can use to alter and modify the strings.

#there are various types of string methods in python.
#they are as follows:

#1.   upper()
#2.   lower()
#3.   strip()
#4.   rstrip()
#5.   lstrip()
#6.   replace()
#7.   split()
#8.   capitalize()
#9.   center()
#10.   count()
#11.  ends with()
#12.  find()
#13.  index()
#14.  isalnum()
#15.  isalpha()
#16.  islower()
#17.  isprintable()
#18.  isspace()
#19.  istitle()
#20.  isupper()
#21.  startswith()
#22.  swapcase()
#23.  title()
#24.  isdigit()
#25. istitle()

#example of string methods


#1.   upper()
a="Ravi"
print(a.upper())    #it will print the string in upper case.


#2.   lower()
a="Ravi"
print(a.lower())     # it will print the string in lower case.


#3.   strip()
a="Ravi!!!!!!!"
print(a.strip("!"))    #it will remove the trailing characters.
# it will not remove the leading characters.
#it removes spaces,tabs,new lines,carrige returns,vertical tabs and form feed characters.
a="Ravi@@@"
print(a.strip("@"))  


#4.   rstrip()
a="!!Ravi!!!!!"
print(a.rstrip("!"))  #it will remove the trailing characters from right side of string.


#5.   lstrip()
a="!!!Ravi!!!!!"
print(a.lstrip("!"))    #it will remove the leading characters from left side of string.


#6.   replace()
a="Ravi"
print(a.replace("Ravi","rao"))   #it will replace the string with another string.


#7.   split()
#the split() method splits the given string at the specified instance and returns the separated string as list items.


a="Ravi-is a good boy"
print(a.split("-"))   #it will split the string into a list.
#it will split the string from the given character we have given between the split().



#8.   capitalize()
#the capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.
#the string has no effect if the first character is already uppercase.
#it also changes middle of the string if uppercase then it will change to lowercase.


blogheading="inTroDuctIon to PythOn"
print(blogheading.capitalize())



#9.   center()
#the centre() method aligns the string to the center as per the parameters given by the user.

str1="welcome to the console!!!"
print(str1.center(50))

print(len(str1))
print(len(str1.center(50)))

#why we put 50 in bracket of center() function???
#because we want to write in mid of the screen and to find the mid of the screen we can use len() function and use double the number of len() in center().
#it will give mid of the screen.



#10.   count()
#the count() method returns the number of times the given value has occured within the given string.

a= "ravi is a good boy.ravi plays cricket."
print(a.count("ravi"))

#we can count number of word is used and letter also.


#11.   ends with()
#the ends with() method checks if the string ends with a given value.
#if yes then return true,else return false.
a="@Ravi!!!!"
print(a.endswith("@"))  #it will return false.
print(a.endswith("!!!"))  #it will return true. 



#we can also check for a value in between the string by providing start and end index positions.
a=" welcome to the console!!!"
print(a.endswith("to",4,10))  #it will return true.
#it will check whether the string ends with to between 4 and 10.

print(a.startswith("@"),a.endswith("!!!"))



#12.   find()
#the find() methods searches for the first occurence of the given value and returns the index where it is present.
#if given value is absent from the string then return -1.


a="he's name is dan.he is an honest man."


print(a.find("is"))   #gives the index of first occurence of the give value.

print(a.find("ishh"))   #gives -1 because ishh is not present in the string.


#13.   index()
#the index() method searches for the first occurence of the given value and returns the index where it is present.
#if given value is absent from the string then raise an exception.


a="he's name is dan.he is an honest man."
print(a.index("dan"))    #gives the index of first occurence of the give value.

#print(a.index("ishh"))
      #gives an error because ishh is not present in the string.



#14.   isalnum()
#the isalnum() method returns true only if the entire string only consists of A-Z,a-z,0-9.
#if any other character or punctuations are present,then it returns false.


str1="WelcomeToTheConsole123"
print(str1.isalnum())   #it will return true.

str2="Welcome!!!!!!!!!!"
print(str2.isalnum())    #it will return false.



#15.   isalpha()
#the isalpha() method returns true only if the entire string only consists of A-Z,a-z.
#if any other character or punctuations or numbers(0-9) are present,then it returns false.


str1="welcome"
print(str1.isalpha())   #it will reurn true.

str2="welcome123"
print(str2.isalpha())    #it will return false.


#16.   islower()
#the islower() method returns true if all the characters in the string are lower case.
#else it returns false.


str1="hello world"      #it will return true.
print(str1.islower())


str2="Hello World"
print(str2.islower())   #it will return false



#17.   isprintable()
#the isprintable() method returns true if all the values within the given string are printable.
#if not,then return false.

str1="we wish you a merry christmas"
print(str1.isprintable())   #it will return true.


str2="we wish you a merry christmas\n"  #i.e \n is not printable.
print(str2.isprintable())   #it will return false.


#18.   isspace()
#the isspace() method returns true only and only if the string contains white spaces.
#else returns false.

str1="hello world"
print(str1.isspace())   #it will return false.


str2="   "
print(str2.isspace())    #it will return true.


#19.   istitle()
#the istitle() method returns true only if the first letter of each word of the string is capitalized.
#else it reurns false.


str1="World Health Organaization"
print(str1.istitle())   #it will return true.


str2="to kill a Mocking bird"
print(str2.istitle())   #it will return false.



#20.   isupper()
#the isupper() method returns true if all the characters in the string are upper case.
#else it returns false.


str1="WORLD HEALTH ORGANIZATION"
print(str1.isupper())   #it will return true.


str2="WORLD HEALTH organization"  #it will return false.
print(str2.isupper())



#21.   startswith()
#the startswith() method checks if the string starts with a given value.
#if yes then return true,else return false.


str1="python is a interpreted language"
print(str1.startswith("python"))  #it will return true.

print(str1.startswith("hello"))    #it will return false.




#22.   swapcase()
#the swapcase() method changes the character casing of the string.
#upper case are converted to lower case and lowercase are converted to upper case.

str1="HELLO friends ThIs iS a PYTHON program"
print(str1.swapcase())



#23.   title()
#the title() method capitalizes each letter of the word within the string.

str1="hello friends this is a PYTHON PROGRAM"
print(str1.title())




#24.  istitle()
#returns true if string is in title Case
str1="Hello Friends"
print(str1.istitle)



#25. isdigit()
#returns true we all characters are only digits (0-9).
str1="1234"
print(str1.isdigit())






# if else conditional statements


    #sometimes the programmer needs to check the evaluation of certain expression(s).
#whether the expression evaluates to true or false.
#if the expression evaluates to false,then the program execution follows a different path then it would have if the expression evaluates to true.

#conditinal opeartors

# > , < , >= , <= , == , !=
# print(a>18)   #it is true only when a is greater then 18.
# print(a<=18)   #it is true only when a is less than or equal to 18.
# print(a==18) # it is true only when a  is equal to 18.
# print(a!=18)  #







