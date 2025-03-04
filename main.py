import turtle

screen = turtle.Screen()
screen.screensize(500, 500)
screen.bgcolor('yellow')

t= turtle.Turtle()
t.speed(0)

t.setheading(135)
# square
t.fillcolor('cyan')
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.goto(0,0)
t.end_fill()

t.setheading(45)
# square
t.fillcolor('brown')
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()

turtle.done()