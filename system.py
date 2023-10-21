import tkinter as tk
from datetime import datetime
import webbrowser

def notepad():
    root1 = tk.Tk()
    root1.title("Notepad")
    root1.geometry("640x480")
    tk.Entry(root1, width=105).grid(column=0, row=1)
    tk.Entry(root1, width=105).grid(column=0, row=2)
    tk.Entry(root1, width=105).grid(column=0, row=3)
    tk.Entry(root1, width=105).grid(column=0, row=4)
    tk.Entry(root1, width=105).grid(column=0, row=5)
    tk.Entry(root1, width=105).grid(column=0, row=6)
    tk.Entry(root1, width=105).grid(column=0, row=7)
    tk.Entry(root1, width=105).grid(column=0, row=8)
    tk.Entry(root1, width=105).grid(column=0, row=9)
    tk.Entry(root1, width=105).grid(column=0, row=10)
    tk.Entry(root1, width=105).grid(column=0, row=11)
    tk.Entry(root1, width=105).grid(column=0, row=12)
    tk.Entry(root1, width=105).grid(column=0, row=13)
    tk.Entry(root1, width=105).grid(column=0, row=14)
    tk.Entry(root1, width=105).grid(column=0, row=15)
    tk.Entry(root1, width=105).grid(column=0, row=16)
    tk.Entry(root1, width=105).grid(column=0, row=17)
    tk.Entry(root1, width=105).grid(column=0, row=18)
    tk.Entry(root1, width=105).grid(column=0, row=19)
    tk.Entry(root1, width=105).grid(column=0, row=20)
    tk.Entry(root1, width=105).grid(column=0, row=21)
    tk.Entry(root1, width=105).grid(column=0, row=22)
    tk.Entry(root1, width=105).grid(column=0, row=23)
    tk.Entry(root1, width=105).grid(column=0, row=24)
    tk.Entry(root1, width=105).grid(column=0, row=25)
    tk.Entry(root1, width=105).grid(column=0, row=26)

def clock():

        root2 = tk.Tk()
        root2.title("")
        root2.geometry("150x100")
        t1 = datetime.now().time()
        tk.Label(root2,text=t1).grid(row=0, column=0)

        root2.mainloop()

def turnoff():
    root3 = tk.Tk()
    root3.title("turn off")
    root3.geometry("800x600")
    tk.Label(root3,text="Turn-Off your computer").grid(row=15, column=15)

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
    root4 = tk.Tk()
    root4.title("About OpenKunix")
    root4.geometry("350x100")
    tk.Label(root4, text="Open Kunix 2.0").grid(row=0, column=0)
    tk.Label(root4, text="DephiSoft 2023-2099").grid(row=1, column=0)
    tk.Label(root4, text="All systems here>https://sites.google.com/view/dephisoft").grid(row=2, column=0)

root = tk.Tk()
root.title("Open Kunix 2.0")
root.geometry("800x600")

tk.Button(root,text="Notepad", command=notepad).grid(column=2, row=2)
tk.Button(root,text="Clock", command=clock).grid(column=2, row=3)
tk.Button(root,text="Turn-Off", command=turnoff).grid(column=2, row=4)
tk.Button(root,text="PaintBrush", command=paint).grid(column=2, row=5)
tk.Button(root,text="Internet", command=browser).grid(column=2, row=6)
tk.Button(root,text="About", command=about).grid(column=2, row=7)





root.mainloop()