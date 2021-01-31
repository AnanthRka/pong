# Pong Game

import turtle
import winsound


def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def paddle_B_up():
    x = paddle_B.ycor()
    x += 20
    paddle_B.sety(x)

def paddle_B_down():
    x = paddle_B.ycor()
    x -= 20
    paddle_B.sety(x)

try:
    window = turtle.Screen()
    window.title("Pong by Ananth")
    window.bgcolor("black")
    window.setup(width=800, height=600)
    """
    center = 0,0
    top center = 300,300
    bottom center = 0,-300
    left center = -400,0
    right center = 400,0
    left top = -400,300

    """

    window.tracer(0)

    #Score Sheet
    score_A = 0
    score_B = 0



    # Paddle A

    paddle_A = turtle.Turtle()
    paddle_A.speed(0)
    paddle_A.shape("square")
    paddle_A.color("white")
    paddle_A.shapesize(stretch_wid=5, stretch_len=1)
    paddle_A.penup()
    paddle_A.goto((-350,0))



    # Paddle B

    paddle_B = turtle.Turtle()
    paddle_B.speed(0)
    paddle_B.shape("square")
    paddle_B.color("white")
    paddle_B.shapesize(stretch_wid=5, stretch_len=1)
    paddle_B.penup()
    paddle_B.goto((350,0))

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto((0 , 0))
    ball.dx = 0.1
    ball.dy = 0.1

    #Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("Player A: 0 Player B: 0", align="center", font=("Arial", 15 , "normal"))


    #Keyboard Binding
    window.listen()
    window.onkey(paddle_A_up, "w")
    window.onkey(paddle_A_down, "s")
    window.onkey(paddle_B_up, "Up")
    window.onkey(paddle_B_down,"Down")


    #Main Game Loop

    while True:

        window.update()

        #Move the Ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #Border Checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1
            score_A += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_A, score_B), align="center",
                    font=("Arial", 15, "normal"))

        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1
            score_B += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_A, score_B), align="center",
                    font=("Arial", 15, "normal"))

        #Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 60 and ball.ycor() > paddle_B.ycor() - 60):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() <paddle_A.ycor() + 60 and ball.ycor() > paddle_A.ycor() - 60):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
except:
    print()
    print('Thank you playing the game.')
    print()