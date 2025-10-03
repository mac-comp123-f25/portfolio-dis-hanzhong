import turtle
turt=turtle.Turtle()
win=turtle.Screen()
turt.begin_fill()
for i in range(2):
    turt.forward(100)
    turt.right(120)
turt.end_fill()
win.exitonclick()