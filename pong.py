import turtle
import os

wn = turtle.Screen()
wn.title("Pong by @dzape")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.tracer(0)

# Pedal_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)

# Pedal_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Pedal_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(" Player A : 0 Player B : 0", align ="center",font=("Courier",24,"normal"))

# score
socre_a = 0
socre_b = 0

# func paddle a 

def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

# func paddle b

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)

# key binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main
while True:
	wn.update()

	#move ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border 
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		os.system("aplay Lightsaber.wav&")

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		os.system("aplay Lightsaber.wav&")

	if ball.xcor() > 390:
		ball.setx(0)
		ball.dx *= -1
		socre_a += 1
		os.system("aplay Lightsaber.wav&")
		pen.clear()
		pen.write(" Player A : {} Player B : {}".format(socre_a, socre_b), align ="center",font=("Courier",24,"normal"))


	if ball.xcor() < -390:
		ball.setx(0)
		ball.dx *= -1
		socre_b += 1
		os.system("aplay Lightsaber.wav&")
		pen.clear()
		pen.write(" Player A : {} Player B : {}".format(socre_a, socre_b), align ="center",font=("Courier",24,"normal"))


	#collison
	if (ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40)):
		ball.setx(-340)
		ball.dx *= -1

	if (ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40)):
		ball.setx(340)
		ball.dx *= -1