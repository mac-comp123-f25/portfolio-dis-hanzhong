import turtle
def draw_nested_squares(t):
    for size in range(10, 80, 10):
        for _ in range(4):
            t.forward(size)
            t.left(90)
        t.penup()
        t.right(90)
        t.forward(10)
        t.left(90)
        t.backward(10)
        t.pendown()
win = turtle.Screen()
tt = turtle.Turtle()
tt.speed(5)
draw_nested_squares(tt)
win.exitonclick()