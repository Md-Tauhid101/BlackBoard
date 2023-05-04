import turtle as t
import random as r

win = t.getscreen()
win.bgcolor("black")
tur = t.Turtle()
tur.color("white")
# color_list=["white","blue","red","green","yellow"]
tur.speed(0)

for i in range(10):
    x = r.randint(-200,200)
    y = r.randint(-200,200)
    tur.penup()
    tur.goto(x,y)
    tur.pendown()
    tur.begin_fill()
    for i in range(5):
        # temp=r.choice(color_list)
        # tur.color(temp)
        tur.lt(144)
        tur.fd(20)
    tur.end_fill()

win.mainloop()