import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.speed(0)

def move_up():
    t.setheading(90)
    t.forward(50)

def move_left():
    t.setheading(180)
    t.forward(50)

def move_down():
    t.setheading(270)
    t.forward(50)

def move_right():
    t.setheading(0)
    t.forward(50)

def restart():
    t.reset()
    t.shape("turtle")
    t.color("green")

screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(restart, "Escape")

screen.mainloop()
