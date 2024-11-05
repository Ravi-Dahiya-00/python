#getting started with graphics programming:
#TURTLE is python's built in graphics module for drawing lines,circles,and other shapes,including text.
#it is easy to learn and simple to use.


#drawing and adding color to a figure:
#1. open python
#2. import turtle
#3. turtle.showturtle()
#4. to draw a string 
         #turtle.write("welcome to python")
#5. to move the arrowhead 100 pixels forward to draw a line in the direction the arrow is pointing:
         #turtle.forward(100)
#6. to turn the arrowhead 90 degrees to the right:
       #turtle.right(90)
#7. to change the turtle's color to red:
       #turtle.color("red")
#8. to move the arrowhead 50 pixels forward to draw a line :
       #turtle.forward(50)
#9. to change the turtle's color to green:
       #turtle.color("green")
#10. to turn the arrowhead 30 degree to the left:
       #turtle.left(30)
#11. you can now close the turtle graphics windows and exit python.

import turtle
turtle.showturtle()
turtle.write("welcome to python")
turtle.forward(100)
turtle.color("red")
turtle.right(90)
turtle.forward(40)
turtle.left(20)
turtle.forward(100)
turtle.right(45)



#moving pen to any location:

     #when the turtle program starts, the arrowhead is at centre of the screen.
     #coordinates of turtle are(0,0)
     #we use goto() function to move the turtle to any location. specified location(x,y)


turtle.goto(0,50)

#to draw a circle:
                #draw a circle using circle command.

turtle.circle(50)   #50 is radius of circle.


#to draw a dot:
             #draw a dot using dot command.


turtle.dot(50)


# we can also use penup() and pendown() functions to move the turtle without drawing a line.


#penup() function is used to stop drawing.
#pendown() function is used to start drawing.

turtle.penup()
turtle.goto(50,-50)
turtle.pendown()

