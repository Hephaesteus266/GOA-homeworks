from turtle import *

#we want to build a house

#step1: draw a square
speed(30)
width(7)
color("indigo")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("pink")
begin_fill() #this line of code fills in the shape with colour, although two different shapes have the same colour does not mean we can use this once since it will make a mess of triangles
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill() #ends the process of filling the empty space with colour

penup()
goto(200, 200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
end_fill()

#HOMEWORK: draw windows and fill in with colour + the door (LETS DO THIS YE)

#done in homework file