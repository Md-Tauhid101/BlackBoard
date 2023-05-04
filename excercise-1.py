import turtle as t
import random as r

tur=t.Turtle()
win=t.getscreen()
win.bgcolor("black")
win.title("First_Project")
tur.speed(0)


color_list=["white","blue","red","green","yellow"]

while True:
    x=10
    for i in range(50):
        tur.hideturtle()
        tur.lt(90)
        temp=r.choice(color_list)
        tur.color(temp)
        tur.fd(x)
        x+=10
    tur.penup()
    tur.home()
    tur.pendown()

# win.mainloop()