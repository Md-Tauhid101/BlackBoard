import turtle as t
win=t.getscreen()
win.bgcolor("black")
win.title("Ondrag Function")
tur=t.Turtle()
tur.color("white","yellow")
tur.speed(0)
def pencil(x,y):
    tur.ondrag(None)
    tur.seth(tur.towards(x,y))
    tur.goto(x,y)
    tur.ondrag(pencil)
# tur.ondrag(pencil,btn=1)

def move(x,y):
    tur.penup()
    tur.goto(x,y)
    tur.pendown()

def cleaner(x,y):
    tur.clear()

def main():
    win.listen()
    tur.ondrag(pencil)
    win.onclick(move,btn=1)
    win.onclick(cleaner,btn=3)

main()

win.mainloop()

