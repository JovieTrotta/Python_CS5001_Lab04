import turtle
pump = turtle.Turtle()

def make_triangle(x, y, color):
  pump.penup()
  pump.goto(x,y)
  pump.begin_fill()
  pump.color(color)
  pump.pendown()

  count = 0
  while count < 3:
    pump.forward(50)
    pump.left(120)
    count +=1

  pump.end_fill()

def make_square(x, y, color):
  pump.penup()
  pump.goto(x,y)
  pump.begin_fill()
  pump.color(color)
  pump.pendown()
  count = 0
  while count < 3:
    pump.forward(50)
    pump.left(90)
    count +=1
  pump.end_fill()

def go():
    pump.penup()
    pump.goto(0,-150)
    pump.color('#ff6600')
    pump.begin_fill()
    pump.circle(150)
    pump.end_fill()
    pump.left(180)
    make_triangle(-35, -20, '#ffffff')
    make_triangle(0, -20, '#ffffff')
    make_triangle(35, -20, '#ffffff')
    pump.left(180)
    make_triangle(-70, 50, '#ffffff')
    make_triangle(0, 50, '#ffffff')
    make_square(-20, 125, '#663300')