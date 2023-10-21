import tkinter as tk
from datetime import datetime
import webbrowser

def notepad():
    window1 = tk.Tk()
    window1.title("Notepad")
    window1.geometry("640x480")
    tk.Entry(window1, width=105).grid(column=0, row=1)
    tk.Entry(window1, width=105).grid(column=0, row=2)
    tk.Entry(window1, width=105).grid(column=0, row=3)
    tk.Entry(window1, width=105).grid(column=0, row=4)
    tk.Entry(window1, width=105).grid(column=0, row=5)
    tk.Entry(window1, width=105).grid(column=0, row=6)
    tk.Entry(window1, width=105).grid(column=0, row=7)
    tk.Entry(window1, width=105).grid(column=0, row=8)
    tk.Entry(window1, width=105).grid(column=0, row=9)
    tk.Entry(window1, width=105).grid(column=0, row=10)
    tk.Entry(window1, width=105).grid(column=0, row=11)
    tk.Entry(window1, width=105).grid(column=0, row=12)
    tk.Entry(window1, width=105).grid(column=0, row=13)
    tk.Entry(window1, width=105).grid(column=0, row=14)
    tk.Entry(window1, width=105).grid(column=0, row=15)
    tk.Entry(window1, width=105).grid(column=0, row=16)
    tk.Entry(window1, width=105).grid(column=0, row=17)
    tk.Entry(window1, width=105).grid(column=0, row=18)
    tk.Entry(window1, width=105).grid(column=0, row=19)
    tk.Entry(window1, width=105).grid(column=0, row=20)
    tk.Entry(window1, width=105).grid(column=0, row=21)
    tk.Entry(window1, width=105).grid(column=0, row=22)
    tk.Entry(window1, width=105).grid(column=0, row=23)
    tk.Entry(window1, width=105).grid(column=0, row=24)
    tk.Entry(window1, width=105).grid(column=0, row=25)
    tk.Entry(window1, width=105).grid(column=0, row=26)

def clock():

        window2 = tk.Tk()
        window2.title("")
        window2.geometry("150x100")
        t1 = datetime.now().time()
        tk.Label(window2,text=t1).grid(row=0, column=0)

        window2.mainloop()

def turnoff():
    window3 = tk.Tk()
    window3.title("turn off")
    window3.geometry("800x600")
    tk.Label(window3,text="Turn-Off your computer").grid(row=15, column=15)

def paint():
    import turtle
    turtle.title("PaintBrush")
    def mU():
        pos = turtle.pos()
        turtle.goto(pos[0], pos[1] + 5)

    def mD():
        pos = turtle.pos()
        turtle.goto(pos[0], pos[1] - 5)

    def mR():
        pos = turtle.pos()
        turtle.goto(pos[0] + 5, pos[1])

    def mL():
        pos = turtle.pos()
        turtle.goto(pos[0] - 5, pos[1])

    def pD():
        if turtle.isdown() == 1:
            turtle.penup()
        else:
            turtle.pendown()

    def cL():
        turtle.clear()

    turtle.onkey(mU, "Up")
    turtle.onkey(mD, "Down")
    turtle.onkey(mL, "Left")
    turtle.onkey(mR, "Right")
    turtle.onkey(cL, "0")
    turtle.onkey(pD, "space")

    turtle.listen()
    turtle.mainloop()

def browser():
    webbrowser.open(url="www.google.com")

def about():
    window4 = tk.Tk()
    window4.title("About OpenKunix")
    window4.geometry("350x100")
    tk.Label(window4, text="Open Kunix 3.0 Developer Version 1").grid(row=0, column=0)
    tk.Label(window4, text="DephiSoft").grid(row=1, column=0)
    tk.Label(window4, text="https://sites.google.com/view/dephisoft").grid(row=2, column=0)

system = tk.Tk()
system.title("Open Kunix 3.0")
system.geometry("800x600")

tk.Button(system,text="Notepad", command=notepad).grid(column=2, row=2)
tk.Button(system,text="Clock", command=clock).grid(column=2, row=3)
tk.Button(system,text="Turn-Off", command=turnoff).grid(column=2, row=4)
tk.Button(system,text="PaintBrush", command=paint).grid(column=2, row=5)
tk.Button(system,text="Internet", command=browser).grid(column=2, row=6)
tk.Button(system,text="About", command=about).grid(column=2, row=7)





system.mainloop()