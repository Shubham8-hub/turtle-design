import turtle
turtle.pensize(2)
turtle.speed(15)
turtle.bgcolor("black")

for i in range(10):
    for colors in ["yellow", "blue", "white", "green", "red", "pink"]:
        turtle.color(colors)
        turtle.circle(180)
        turtle.left(10)
        turtle.hideturtle()

def my_goto(x,y):
    turtle.pencolor("red")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

turtle.pendown()
my_goto(-150,-150)
turtle.done()