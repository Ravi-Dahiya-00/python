
#convert fahrenhit to celsius:
print("fahrenhit 35 is celsius degree")
print("celsius degree is" ,5/9 * (35-32))       #correct method it will show 1.6667



#but if use wrong operator it will show different answer:
print("fahrenhit 35 is celsius degree")
print("celsius degree is" ,5 / 9 * 35 - 32)        #wrong method it will show -12.55 because we didn't tell which calculation is to be done first.






#something intersting:
                #if we want something in design and in more than one line we can write it by using some logic.

#let's see:
          #python program to display patterns:


print(" FFFFFFFFFF      UU            UU        NN            NNN ")
print(" FF              UU            UU        NN N          NN  ")
print(" FF              UU            UU        NN   N        NN  ")
print(" FFFFFFFFF       UU            UU        NN     N      NN  ")
print(" FF               UU          UU         NN       N    NN  ")
print(" FF                UU        UU          NN         N  NN  ")
print(" FF                  UUUUUUUU           NNN           NNN  ")

#this was only for fun purpose but it also provided one different logic to think it about.











#we can also create a table using print statement.

print("A Program To Display The Table: ")
print("a", 
             "a^2",
                         "a^3")         #written in different line for spacing in between the characters a, a^2;a^3.
print(1,         1*1,       1*1*1)
print(2,         2*2,       2*2*2)
print(3,         3*3,       3*3*3)
print(4,         4*4,       4*4*4)












print((9.5*4.5-2.5*3)/(45.5-3.5))









#calculate summation of series
print("summation of series",1+2+3+4+5+6+7+8+9)









print("Compute the pi value using the formula")
print(4.0 * (1 - (1.0/3) + (1.0/5) - (1.0/7) + (1.0/9) - (1.0/11)))

print(4.0 * (1 - (1.0/3) + (1.0/5) - (1.0/7) + (1.0/9) - (1.0/11) + (1.0/13)-(1.0/15)))












radius=5.5
area=radius*radius*3.14
perimeter=2*radius*3.14
print("area of circle is",area,"of",radius)
print("perimeter of circle is",perimeter,"of",radius)










#Calculate the area of rectangle with the width and height
area = 4.5 * 7.9
#Calculate the perimeter of rectangle with the width and height
perimeter = (2 * 4.5) + (2 * 7.9)
#display the area
print("area of rectangle:", area)
#display the perimeter
print("perimeter of rectangle:",  perimeter)













kilometers=14
miles=kilometers/1.6
distance=miles
time=45.5/60
averagespeed=distance/time
print(averagespeed)












currentpopulation=312032486

#seconds in 1 year
secondsin1year=365*24*60*60

#  1 birth in every 7second.             add one birth in every 7seconds.
#  1 death in every 13seconds.           subtract one death in every 13seconds.
#  1 immigration in every 45seconds.     add one immmigrant every 45seconds.


#total seconds in 1 year
secondsin1year=365*24*60*60


#after 1 year,number of births(7seconds = 1birth/plus)
birthsperyear=secondsin1year//7
print("birthsperyear",float(birthsperyear))


#after 1 year,number of deaths(13seconds= 1death/minus)
deathsperyear=secondsin1year//13
print("deathperyear",float(deathsperyear))


#after 1 year,number of immigrations(45seconds=1immigration/plus)
immigrationperyear=secondsin1year//45
print("immigrationperyear",float(immigrationperyear))


#rate per year
rateperyear=birthsperyear-deathsperyear+immigrationperyear
print("rateperyear",float(rateperyear))


total=rateperyear + currentpopulation
print(total)            #1st year 
print("populationafter2year",int(rateperyear*2)+int(currentpopulation))
print("populationafter3year",int(rateperyear*3)+int(currentpopulation))
print("populationafter4year",int(rateperyear*4)+int(currentpopulation))
print("populationafter5year",int(rateperyear*5)+int(currentpopulation))















#circlearea.py


#assign a value to radius
radius=20               #radius is now 20

#compue area
area=radius*radius*3.14159

#display results
print("the area of circle of radius",radius,"is",area)

#radius is a variable that has a fix value 20 that is stored in computers memory and can be used anytime when the program needs variable.
#python automatically figures out the data type according to the value assigned to the variable.we need not to specify what types of values are being used.









width=5.5
height=2
print("area is ", width * height)












miles=100
kilometers=miles*1.609
print("100miles have",kilometers,"kilometers")













#prompt the user to enter a radius
radius=eval(input("enter a value for radius:"))                     #eval converted the string to number


#compute area
area=radius*radius*3.14159


#display results
print("the area for the circle of radius",radius,"is",area)








# BMI calculator



#formula=(weight/height**2)

#taking users weight and height input
weight=input("enter your body weight:")
height=input("enter your body height")

#now we have both value of weight and height but remember that these values are in string . first convert them into int value .
#we can also convert  them directly using int while making BMI operator 
BMI=(int(weight)/(int(height)**2))
print(BMI)









#how many days,weeks,months do we have left if we will die at the age of 90


year_days=365
year_months=12
year_weeks=52

#firstly enter your current age
a=input("enter your current age in years:")

#months of your life you have completed 
completed_month=int(a)*12
print(completed_month)
#total months
total_months=90*12
print(total_months)
#remaining months
remaining_months=int(total_months)-int(completed_month)

print(f"remaining months of your life are:",remaining_months)

#days left
total=90*365
completed=int(a)*365
remaining=total-completed
print("your left days are:",remaining)


#weeks left
total=90*52
completed=int(a)*52
remaining=total-completed
print("your weeks left are :",remaining)
