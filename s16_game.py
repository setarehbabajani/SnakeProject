import turtle
import time
import random

def set_screen():
    r = turtle.Screen()
    r.title("snake game")
    r.bgcolor("blue")
    r.setup(width=600 , height= 600)
    r.tracer(0)
    return  r   

def set_head():
    t = turtle.Turtle()
    t.speed(1)
    t.shape("square")
    t.color("gray")
    t.penup()
    t.forward(100 )
    t.direction = "stop"
    return t

def add_snake_lenght():
    t = turtle.Turtle()
    t.speed(0)
    t.shape("square")
    t.color("black")
    t.penup()
    tikeha.append(t)

def move(h):
    x , y = h.position()
    if h.direction == "up":
        h.setposition(x , y+20)
    
    if h.direction == "down":
        h.setposition(x , y-20)
    
    if h.direction == "right":
        h.setposition(x+20 , y)
    
    if h.direction == "left":
        h.setposition(x-20 , y)

def keyboard_listening(r):
    r.listen()
    r.onkey(go_up , "Up")
    r.onkey(go_down , "Down")
    r.onkey(go_right , "Right")
    r.onkey(go_left , "Left")

def go_up():
    if h.direction != "down":
        h.direction = "up"

def go_down():
    if h.direction != "up":
        h.direction = "down"

def go_right():
    if h.direction != "left":
        h.direction = "right"

def go_left():
    if h.direction != "right":
        h.direction = "left"


def set_food():
    m = turtle.Turtle()
    m.speed(0)
    m.shape("circle")
    m.color("red")
    m.penup()
    m.shapesize(0.50, 0.50)
    m.setpos(0, 0)
    return m

def check_food(m, h):
    xm , ym = m.position()
    xh , yh = h.position()
    return abs(xm - xh )<15 and abs(ym -yh)<15 

def reposition_food(m):
    new_x = random.randint(-290 , 290)
    new_y = random.randint(-290 , 290)
    m.setpos(new_x , new_y)

def move_tikeha():
    if len(tikeha)>0 :
        for i in range( len(tikeha)-1 , 0 , -1):
            x_prev_tike , y_prev_tike = tikeha[i-1].position()
            tikeha[i].setpos(x_prev_tike , y_prev_tike)
        
        xh , yh = h.position()
        tikeha[0].setpos(xh ,yh)

def check_border_collision():
    xh , yh = h.position()
    if xh >290 or xh <-290 or yh >290 or yh <-290 :
        return True

def check_self_collision():
    for u in range(len(tikeha)) :
        if tikeha[u].distance(h)<10 :
            return True
    return False


def update_score():
    score_writer.undo()
    score_writer.hideturtle()
    score_writer.setpos(0 , 260)
    score_writer.write("Score: {} High Score: {}".format(score , high_score), align="center", font=("Courier", 24, "normal"))

def clear_tikeha():
    for t in tikeha:
        t.setpos(1000 , 0)
    tikeha.clear()
    f.setpos(0 , 0)
    h.setpos(0 , 100)
    h.direction = "stop"


def reset_score():
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    return pen

scrn = set_screen()
h = set_head()
f = set_food()
keyboard_listening(scrn)
tikeha = []
score = 0
high_score = 0

score_writer = reset_score()



while True :
    move_tikeha()
    move(h)
    if check_border_collision() or check_self_collision():
        if score > high_score :
            high_score = score
        score = 0
        clear_tikeha()
    if check_food(f , h):
        reposition_food(f)
        add_snake_lenght()
        score = score + 10
    

    update_score()
    reset_score()
    scrn.update()
    time.sleep(0.2)
