            #ONCLICK FUNCTION TUTORIAL

import turtle as t
win=t.getscreen()
win.bgcolor("black")
tur=t.Turtle()
win.title("Onclick_Function")


def square(x,y):
    tur.speed(0)
    tur.penup()
    tur.goto(x,y)
    tur.pendown()
    tur.color("white")
    for i in range(4):
        tur.fd(50)
        tur.lt(90)

def star(x,y):
    tur.speed(0)
    tur.penup()
    tur.goto(x,y)
    tur.pendown()
    tur.color("yellow")
    for i in range(5):
        tur.fd(50)
        tur.lt(144)

win.onclick(square,btn=3)
win.onclick(star,btn=1)
win.mainloop()
