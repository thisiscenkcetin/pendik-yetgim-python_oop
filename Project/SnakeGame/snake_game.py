import turtle 
import time 
import random 

delay = 0.1
score = 0 
high_score = 0
segment_size = 20
screen_width = 600
screen_height = 600

screen = turtle.Screen()
screen.title("Yılan Oyunu")
screen.bgcolor("pink")
screen.setup(width=screen_width,height=screen_height)
screen.tracer()


head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red"),
food.penup()

try:
    max_x_bound_init = int(screen_width /2 - segment_size *2)
    min_x_bound_init = -max_x_bound_init
    max_y_bound_init = int(screen_height / 2 - segment_size *2)
    min_y_bound_init = -max_y_bound_init

    x_init = random.randint(min_x_bound_init,max_x_bound_init)
    y_init = random.randint(min_y_bound_init,max_y_bound_init)


    x_init = round(x_init / segment_size) * segment_size
    y_init = round(y_init / segment_size) * segment_size
    food.goto(x_init,y_init)
except ValueError:
    food.goto(0,100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.speed(0)            
pen.shape("square")
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0,(screen_height / 2) - 40)
pen.write("Skor: 0   En Yüksek Skor: 0", align="center", font=("Courier", 18, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"



def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + segment_size)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - segment_size)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - segment_size)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + segment_size)


screen.listen()

screen.onkeypress(go_up,"Up")
screen.onkeypress(go_down,"Down")
screen.onkeypress(go_left,"Left")
screen.onkeypress(go_right,"Right")

screen.onkeypress(go_up,"w")
screen.onkeypress(go_down,"s")
screen.onkeypress(go_left,"a")
screen.onkeypress(go_right,"d")



while True:

    screen.update()

    if head.xcor() > screen_width / 2 - segment_size or \
       head.xcor() < -screen_width / 2 + segment_size or \
       head.ycor() > screen_height / 2 - segment_size or \
       head.ycor() < -screen_height / 2 + segment_size:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000,1000)
            segments.clear()

            score = 0
            delay = 0.1
            pen.write(f"Skor: {score}   En Yüksek Skor: {high_score}", align="center", font=("Courier", 18, "normal"))

    if head.distance(food) < segment_size:
        try:
            max_x_bound = int(screen_width / 2 - segment_size * 2)
            min_x_bound = -max_x_bound
            max_y_bound = int(screen_height / 2 - segment_size * 2)
            min_y_bound = -max_y_bound

            x = random.randint(min_x_bound, max_x_bound)
            y = random.randint(min_y_bound, max_y_bound)

            x = round(x / segment_size) * segment_size
            y = round(y / segment_size) * segment_size
            food.goto(x,y)
        except ValueError:
            food.goto(0,0)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    
    if delay > 0.03:
        delay -= 0.001

    score += 10 

    if score > high_score:
        high_score = score

    pen.clear()
    pen.write(f"Skor: {score}   En Yüksek Skor: {high_score}", align="center", font=("Courier", 18, "normal")) 


    for index in range(len(segments) - 1,0,-1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)  
    move() 


    for segment in segments:
        if head.distance(segment) < segment_size - 5:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for seg in segments:
                seg.goto(1000,1000)
            segments.clear()

            score = 0
            delay = 0.1 
            pen.clear()
            pen.write(f"Skor: {score}   En Yüksek Skor: {high_score}", align="center", font=("Courier", 18, "normal"))

            time.sleep(delay)