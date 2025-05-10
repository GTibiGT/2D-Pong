import turtle
import time

#Create Screen
scrn = turtle.Screen()
scrn.title("Pong game")
scrn.bgcolor("black")
scrn.setup(width=500, height=680)

#Gun(turtle)
gun = turtle.Turtle()
gun.speed(0)
gun.shape("turtle")
gun.color("lime")
gun.tilt(90)
gun.shapesize(stretch_wid=2, stretch_len=2)
gun.penup()
gun.goto(0, -280)

#Enemy(centipede)
enemy = turtle.Turtle()
enemy.speed(30)
enemy.shape("circle")
enemy.color("red")
enemy.penup()
enemy.goto(0, 260)
enemy.dx = 7
enemy.dy = -7

#Score
score = 0

#display score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("lime")
sketch.penup()
sketch.hideturtle()
sketch.goto(-240, 320)
sketch.write("Score: 0", align="left", font=("Courier", 14, "normal"))

#functions to move gun
def up():
    y = gun.ycor()
    if y < -170: #limit movement
        y += 20
        gun.sety(y)

def down():
    y = gun.ycor()
    if y > -300: #limit movement
        y -= 20
        gun.sety(y)

def right():
    x = gun.xcor()
    if x < 230: #limit movement
        x += 20
        gun.setx(x)

def left():
    x = gun.xcor()
    if x > -250: #limit movement
        x -= 20
        gun.setx(x)

#binds
scrn.listen()
scrn.onkeypress(up ,"w")
scrn.onkeypress(down, "s")
scrn.onkeypress(right ,"d")
scrn.onkeypress(left, "a")

#main game loop
while True:
    scrn.update()
    time.sleep(0.01) # add delay to make game smoother

    enemy.setx(enemy.xcor() + enemy.dx)
    enemy.sety(enemy.ycor() + enemy.dy)

    #collision of enemy with wall
    if enemy.xcor() > 230:
        enemy.setx(230)
        enemy.dx *= -1

    if enemy.xcor() < -230:
        enemy.setx(-230)
        enemy.dx *= -1

    if enemy.ycor() < -260:
        enemy.dy *= -1
        score += 1
        sketch.clear()
        sketch.write("Score: {}".format(score), align="left", font=("Courier", 14, "normal"))

    if enemy.ycor() > 300:
        enemy.sety(300)
        enemy.dy *= -1

    #paddle ball collision
    if (enemy.ycor() > -280 and enemy.ycor() < -270) and (enemy.xcor() < gun.xcor() + 50 and enemy.xcor() > gun.xcor() - 50):
        enemy.sety(-270)
        enemy.dy *= -1
