__author__ = 'Vector'


import turtle
def draw_square():
  draw=turtle.Turtle()
  for dist in range(90,110):
    for i in range(4):
      draw.forward(dist)
      draw.right(90)
def draw_circle():
  cir=turtle.Turtle()
  for i in range(10):
    cir.circle(90+i)
def draw_triangle():
  triang= turtle.Turtle()
  for j in range(3):
    triang.right(120)
    triang.forward(100)

def main():
  window=turtle.Screen()
  window.bgcolor("red")

  draw_square()
  draw_circle()
  draw_triangle()
  window.exitonclick()

main()