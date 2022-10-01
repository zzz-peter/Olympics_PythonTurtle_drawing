import turtle

def olympic_up():

    t = turtle.Pen()
    colors = ['blue', 'black', 'red']
    t.penup()
    t.left(180)
    t.forward(200)
    t.right(180)
    for i in range(0, 3):
        t.penup()
        t.pensize(9)
        t.pencolor(colors[i])
        t.pendown()
        t.circle(80)
        t.penup()
        t.forward(130)

def olympic_down():

    p = turtle.Pen()
    color = ['yellow','green']
    p.penup()
    p.left(180)
    p.forward(160)
    p.right(270)
    p.forward(105)
    p.left(90)
    p.forward(17)
    for x in range(0,2):
        p.penup()
        p.pensize(9)
        p.pencolor(color[x])
        p.pendown()
        p.circle(80)
        p.penup()
        p.forward(130)

olympic_up()
olympic_down()
    