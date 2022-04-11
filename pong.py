import turtle
import os

wn = turtle.Screen()
wn.title("pong - Sebas")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()
wn.addshape("images/btc_logo.gif")

score_b = 0
score_r = 0

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_wid=8, stretch_len=1)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=8, stretch_len=1)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('images/btc_logo.gif')
#ball.shape("circle")
#ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = 5


#Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("Blue player: 0 -- Red player: 0", align="center", font=("currier", 24, "normal"))

#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y = y + 20
    paddle_a.sety(y)
    return None
def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)
    return None
def paddle_b_up():
    y = paddle_b.ycor()
    y = y + 20
    paddle_b.sety(y)
    return None
def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)
    return None

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



while True:
    wn.update()
    
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Bounce at the borbers
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    #Score on the right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -ball.dx
        score_b += 1
        pen.clear()
        pen.write("Blue player: {} -- Red player: {}".format(score_b, score_r), align="center", font=("currier", 24, "normal"))
        
    #Score on the left
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = -ball.dx
        score_r += 1
        pen.clear()
        pen.write("Blue player: {} -- Red player: {}".format(score_b, score_r), align="center", font=("currier", 24, "normal"))
    
    #Set a floor for the paddles
    flor_paddle_a_condition = (paddle_a.ycor() < -200)
    flor_paddle_b_condition = (paddle_b.ycor() < -200)
    if flor_paddle_a_condition:
        paddle_a.sety(-200)
    if flor_paddle_b_condition:
        paddle_b.sety(-200)


    #Set a ceiling for the paddles
    flor_paddle_a_condition = (paddle_a.ycor() > 200)
    flor_paddle_b_condition = (paddle_b.ycor() > 200)
    if flor_paddle_a_condition:
        paddle_a.sety(200)
    if flor_paddle_b_condition:
        paddle_b.sety(200)
           
    #paddle and ball collisions
    x_conditionr = (ball.xcor() > 340 and ball.xcor() < 350)
    y_conditionr = (ball.ycor() < paddle_b.ycor() + 70 and ball.ycor() > paddle_b.ycor() - 70)
    if x_conditionr and y_conditionr:
        ball.setx(340)
        ball.dx  = -ball.dx
        os.system("afplay sounds/bounce.mp4&")
        
    x_conditionl = (ball.xcor() < -340 and ball.xcor() > -350)
    y_conditionl = (ball.ycor() < paddle_a.ycor() + 70 and ball.ycor() > paddle_a.ycor() - 70)
    if x_conditionl and y_conditionl:
        ball.setx(-340)
        ball.dx  = -ball.dx
        os.system("afplay sounds/bounce.mp4&")
