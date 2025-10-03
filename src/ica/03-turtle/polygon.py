import turtle
input(n)
turt=turtle.Turtle()
win=turtle.Screen()
turt.begin_fill()
for i in range(n):
    turt.forward(100)
    turt.right(360/n)
turt.end_fill()
win.exitonclick()