#variable naming convention:
                          #use lower case for variable names,as in radius and area.

# using the lowercase and uppercase in betweeen such as numberOFStudents.this naming style is known as camelcase because the uppercase characters in the name resemble a camel's hump.



#camel case:1 word in betwwen is uppercase characters
#myName=ravi     


#snake case: __ this character is used after every character for multiword lines.
#my_name_is_=ravi                    used for multiple words in sn 1 variable


#pascalcase: every character of first word in the line is uppercase character.
# MyNameIsRavi=1



                                  #variables,assignment statements and expressions



#we can name a variable like this :
#1. hello
#2. hello_1
#3. hello1
#4. HELLO
#5. 1 
#6. Roll_No
#7. SL_n6



#we cannot give name to variables like this :
#1. 1hello
#2. 1_hello
#3. no special characters can be used rather than ____ this
   #hello??
   #(hello)
 # roll no
#4. 1=a 
#5. "age"
   
   
   
# there are some reserved words that cannot be used as a variables.
#these are total 33 keywords in python 3.

'''False		class		finally		is			return
None		continue	for			lambda		try
True		def			from		nonlocal	while
and			del			global		not			with
as			elif		if			or			yield
assert 		else		import	 	pass
break		except		in			raise		'''


import keyword	 		# This statement is used to import the keyword module.
print(keyword.kwlist)	# kwlist contains all the keywords of Python

# to check whether a given word is a Python keyword or not, we use a built-in function iskeyword(). This function returns a boolean value, if the given word is a keyword then it returns True as output otherwise returns False.

# Program - 1:
import keyword # This will import the keyword module
print(keyword.iskeyword('and')) # Here 'and' is a keyword so it prints True as output 
Output: True

# Program - 2:
import keyword # This will import the keyword module
print(keyword.iskeyword('python')) # Here 'python' is not a keyword so it prints False as output 
Output: False











#identifiers
#identifiers are the names that identify the elements such as variables and functions in a program.
         #number1,number2,number3,average,input,eval and print are the name of the things that appear in program.

#in programming terminology such names are called identifiers.


    #an identifier is a sequence of characters that consists of letter,digits,and underscores(__).
    #an identifier must start with a letter or an underscore.it cannot start with a digit.
    #an identifier cannot be a keyword.(see appendix A,python keywords,for a list of keywords.)
                    #keywords,also called reserved words.  have special meaning in python.
                    #import is a keyword, which tells the python interpreter to import a module to the program.
   #an identifier can be of any length.


#legal identifiers
               #area, radius and number1.


#whereas 2A and d+4 are not because they don't follow the rules.
                                                   #it is reported as a syntax error.

#note:
    #python is case sensitive language , so area, Area , AREA all are diferent.



#descriptive names:
                 #descriptive identifiers make programs easy to read.
