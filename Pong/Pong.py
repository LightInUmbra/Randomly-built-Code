# Learning to program games with python
# USE AS TEMPLATE
# Not Object Oriented Programming


import turtle

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Scores!!
score_a = 0
score_b = 0

# bar one
barOne = turtle.Turtle()
barOne.speed(0)
barOne.shape("square")
barOne.color("white")
barOne.shapesize(stretch_wid=5, stretch_len=1)
barOne.penup()
barOne.goto(-350, 0)

# bar two
barTwo = turtle.Turtle()
barTwo.speed(0)
barTwo.shape("square")
barTwo.color("white")
barTwo.shapesize(stretch_wid=5, stretch_len=1)
barTwo.penup()
barTwo.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .07
ball.dy = .07

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions for player One movement up
def barOne_up():
    y = barOne.ycor()
    y += 20
    barOne.sety(y)

# Movement down
def barOne_down():
    y = barOne.ycor()
    y -= 20
    barOne.sety(y)

# Functions for player Two movement up
def barTwo_up():
    y = barTwo.ycor()
    y += 20
    barTwo.sety(y)

# Movement down
def barTwo_down():
    y = barTwo.ycor()
    y -= 20
    barTwo.sety(y)

# Key Bindings (Fancy words for buttons)
# For computer to figure out what key was pressed
win.listen()
# Player 1
win.onkeypress(barOne_up, "w")
win.onkeypress(barOne_down, "s")
# Player 2
win.onkeypress(barTwo_up, "Up")
win.onkeypress(barTwo_down, "Down")

# Main Game Loop
while True:
    win.update()


    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Border Rendering
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    # Bar and Ball collisons
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < barTwo.ycor() + 40 and ball.ycor() > barTwo.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < barOne.ycor() + 40 and ball.ycor() > barOne.ycor() -40):
            ball.setx(-340)
            ball.dx *= -1


# ERRORS DONE IN CODE:
# Line 104 [Temp]: Remember, do not use greater than sign here. First error.