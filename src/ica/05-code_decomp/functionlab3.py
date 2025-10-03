import turtle
import math

win = turtle.Screen()
win.bgcolor("light sky blue")

sepalTurtle = turtle.Turtle()
sepalTurtle.speed(0)
sepalTurtle.color("dark green", "spring green")
sepalTurtle.hideturtle()

petalTurtle = turtle.Turtle()
petalTurtle.speed(0)
petalTurtle.color('dark red', 'light coral')
petalTurtle.hideturtle()

centerTurtle = turtle.Turtle()
centerTurtle.speed(0)
centerTurtle.color('purple4')
centerTurtle.hideturtle()

stampTurtle = turtle.Turtle()
stampTurtle.color("gold")
stampTurtle.speed(0)
stampTurtle.shape("turtle")
stampTurtle.hideturtle()

def drawfivecircles(turt,radius,centreX,centreY):
    turt.up()
    turt.goto(centreX, centreY)
    turt.down()
    for i in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)

def drawfivecenters(turt,centreX,centreY):
    centerTurtle.goto(centreX, centreY)
    centerTurtle.down()
    centerTurtle.begin_fill()
    centerTurtle.circle(15)
    centerTurtle.end_fill()

def drawfivestamps(turt,centreX,centreY):
    stampTurtle.up()
    stampTurtle.goto(centreX, centreY)
    stampTurtle.down()
    stampTurtle.stamp()

drawfivecircles(sepalTurtle,50,0,0)

drawfivecircles(petalTurtle,25,0,0)

drawfivecenters(centerTurtle, 0, -15)

drawfivestamps(stampTurtle,-2,0)

drawfivecircles(sepalTurtle,50,0,220)

drawfivecircles(petalTurtle,25,0,220)

drawfivecenters(centerTurtle, 0, 205)

drawfivestamps(stampTurtle,-2,220)

drawfivecircles(sepalTurtle,50,220,0)


drawfivecircles(petalTurtle,25,220,0)

drawfivecenters(centerTurtle, 220, -15)

drawfivestamps(stampTurtle,218,0)

drawfivecircles(sepalTurtle,50,0,-220)

drawfivecircles(petalTurtle,25,0,-220)

drawfivecenters(centerTurtle, 0, -235)

drawfivestamps(stampTurtle,-2,220)

drawfivecircles(sepalTurtle,50,-220,0)

drawfivecircles(petalTurtle,25,-220,0)

drawfivecenters(centerTurtle, -220, -15)

drawfivestamps(stampTurtle,-222,0)

win.exitonclick()