#main.py
import turtle, random, time, colorsys, os

os.chdir("C:/Users/Bonnie/PycharmProjects/tens/venv")
mywindow = turtle.Screen()
mywindow.setup(1309,783)
mywindow.bgpic("arcade.gif")
mywindow.title("sneksss")

#---------TITLE SCREEN----------

colorboy = turtle.Turtle()
colorboy.penup()
colorboy.hideturtle()
colorboy.shape("square")
colorboy.goto(-320,-10)
colorboy.pencolor("red")
colorboy.pendown()

colorboy.pensize(160)
colorboy.speed(4)
colorboy.goto(-320,365)
colorboy.goto(-320,150)
colorboy.color("white")
colorboy.write("S", font=("Courier", 50, "bold"), align="center")
colorboy.penup()
colorboy.pencolor("#FF8933")
colorboy.goto(-160,400)
colorboy.pendown()
colorboy.goto(-160,-10)
colorboy.goto(-160,150)
colorboy.color("white")
colorboy.write("N", font=("Courier", 50, "bold"), align="center")
colorboy.penup()
colorboy.pencolor("#FFDA33")
colorboy.goto(0,-10)
colorboy.pendown()
colorboy.goto(0,365)
colorboy.goto(0,150)
colorboy.color("white")
colorboy.write("A", font=("Courier", 50, "bold"), align="center")
colorboy.penup()
colorboy.pencolor("green")
colorboy.goto(160,365)
colorboy.pendown()
colorboy.goto(160,-10)
colorboy.goto(160,150)
colorboy.color("white")
colorboy.write("K", font=("Courier", 50, "bold"), align="center")
colorboy.penup()
colorboy.pencolor("blue")
colorboy.goto(320,-10)
colorboy.pendown()
colorboy.goto(320,365)
colorboy.goto(320,150)
colorboy.color("white")
colorboy.write("E", font=("Courier", 55, "bold"), align="center")
colorboy.penup()
colorboy.hideturtle()
colorboy.shape("square")
colorboy.color("black")
colorboy.turtlesize(40,40)
colorboy.goto(0,800)
colorboy.speed(1.5)
colorboy.showturtle()
colorboy.goto(0,400)
colorboy.clear()

borderboy = turtle.Turtle()
borderboy.penup()
borderboy.hideturtle()
borderboy.pencolor("red")
borderboy.speed(0)
borderboy.pensize(3)
borderboy.goto(-370,365)
borderboy.pendown()
borderboy.goto(-370,-10)
borderboy.goto(390,-10)
borderboy.goto(390,365)
borderboy.goto(-370,365)

#-------------TURTLE CREATION------------------
colorboy.hideturtle()
colorboy.goto(0, 330)
colorboy.color("white")
score = 0
colorboy.write("Score: ",score, font=("Courier", 12, "normal"), align="center")

snake = turtle.Turtle()
snake.penup()
snake.goto(0,150)
snake.shape("square")
snake.color("white")
snake.turtlesize(1,1)
snake.speed(1)

point = turtle.Turtle()
point.penup()
point.goto(random.randint(-300, 300), random.randint(30, 300))
point.shape("circle")
point.color("red")
point.turtlesize(1)
point.speed(0)

#-------------FUNCTION---------------
right = True
left = False
up = False
down = False
def goup():
    global right, left, up, down
    right = False
    left = False
    up = True
    down = False
def godown():
    global right, left, up, down
    right = False
    left = False
    up = False
    down = True
def goleft():
    global right, left, up, down
    right = False
    left = True
    up = False
    down = False
def goright():
    global right, left, up, down
    right = True
    left = False
    up = False
    down = False

def scorePoint(snake,sr,p,pr):
    d = snake.distance(p.xcor(), p.ycor())
    if d < sr + (pr * 25):
        global score
        score+=1
        colorboy.clear()
        colorboy.write("Score: "+ str(score), font=("Courier", 10, "bold"), align="center")
        point.goto(random.randint(-330, 330), random.randint(30, 300))
        for i in range(0,len(snakeTail)):
            while point.distance(snakeTail[i].xcor(), snakeTail[i].ycor())<20:
                point.goto(random.randint(-330, 330), random.randint(30, 300))
        createTail()

def crashTail(snake, sr, tail, tr):
    d = snake.distance(tail.xcor(), tail.ycor())
    if d < sr + (tr * 10):
        gameOver()

snakeTail = []
i = -1

def createTail():
    global i
    snakeTail.append(turtle.Turtle())
    i +=1
    snakeTail[i].penup()
    snakeTail[i].hideturtle()
    snakeTail[i].shape("square")
    snakeTail[i].color("white")
    snakeTail[i].turtlesize(1, 1)
    snakeTail[i].speed(0)

def moveTail():
    for j in range(0,len(snakeTail)):
        snakeTail[j].showturtle()
        snakeTail[j].goto(snakeCoordinates[len(snakeCoordinates)-j-2])

def gameOver():
    point.hideturtle()
    snake.hideturtle()
    for i in range(0,len(snakeTail)):
        snakeTail[i].hideturtle()
    colorboy.clear()
    colorboy.goto(0, 150)
    colorboy.write("Good game!", font=("Courier", 30, "bold"), align="center")
    time.sleep(2)
    colorboy.clear()
    colorboy.write("Your final score is " + str(score) + " points", font=("Courier", 20, "bold"),
                   align="center")
    time.sleep(4)
    mywindow.bye()

#----------------INITIALIZING------------------------
mywindow.listen()
mywindow.onkey(goup,'Up')
mywindow.onkey(godown,'Down')
mywindow.onkey(goleft,'Left')
mywindow.onkey(goright,'Right')
die = False
snakeCoordinates = []

FPS = 8  # frames per second
refreshAt = 1/FPS #and so this is the refresh interval
startOfInterval = time.clock()
mywindow.tracer(0,0)
z=0
#---------------------MAIN LOOP-----------------------

while die == False:
    endOfInterval = time.clock()
    if z < 800:
        z += 0.25
        hue = z / 800
        colorTuple = colorsys.hsv_to_rgb(hue, 1, 1)
    elif z >= 800:
        z = 0
    point.color(colorTuple)
    if endOfInterval - startOfInterval >= refreshAt:
        if right == True:
            snake.goto(snake.xcor() + 20, snake.ycor())
        elif left == True:
            snake.goto(snake.xcor() - 20, snake.ycor())
        elif up == True:
            snake.goto(snake.xcor(), snake.ycor() + 20)
        elif down == True:
            snake.goto(snake.xcor(), snake.ycor() - 20)
        scorePoint(snake,1,point,0.8)
        snakeCoordinates.append([snake.xcor(), snake.ycor()])
        moveTail()
        for i in range(0,len(snakeTail)):
            crashTail(snake, 1, snakeTail[i], 1)
        mywindow.update()  # manually draw the screen
        startOfInterval = time.clock()

    if snake.xcor()>370 or snake.xcor()<-340 or snake.ycor()>330 or snake.ycor()<20:
        die = True

#-------------------END-----------------------

gameOver()

