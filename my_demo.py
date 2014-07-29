__author__ = 'Vector'
import turtle
import math


def vic_forwardr2b(turt, s):
    green = 0.0
    turt.pencolor(1.0,0.0,0.0)
    for i in range(s):
        if 0 == 0:
            blue = float(i)/float(s)
            red = 1.0 - blue
            #turt.pencolor(red,green,blue)
            turt.pencolor(red,green,blue)
            turt.forward(1)
        if i % 30 == 0:
            turt.stamp()

def vic_forwardb2r(turt, s):
    green = 0.0
    turt.pencolor(1.0,0.0,0.0)
    for i in range(s,0,-1):
        if 0 == 0:
            blue = float(i)/float(s)
            red = 1.0 - blue
            turt.pencolor(red,green,blue)
           # turt.pencolor(0.0,red,blue)
            turt.forward(1)
        if i % 30 == 0:
            turt.stamp()

def make_flower(turt,s,angle,count):
      for i in range(count/2):
        turt.right(angle)
        vic_forwardr2b(turt,s)
        turt.right(angle)
        vic_forwardb2r(turt,s)



s = turtle.Shape("compound")
poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
s.addcomponent(poly1, "red", "blue")
poly2 = ((0,0),(10,-5),(-10,-5))
s.addcomponent(poly2, "blue", "red")
turtle.register_shape("myshape", s)



bert=turtle.Turtle()
bert.width(2)
#bert.pencolor("yellow")
bert.home()
#bert should be fabulous
bert.shape("myshape")

window=bert.getscreen()
#window.bgcolor("black")
window.tracer(10)
window.bgpic("bliss.gif")

bert.penup()
bert.write("Hi everybody!")
make_flower(bert,300,125,24)
bert.hideturtle()
window.update()
window.exitonclick()


