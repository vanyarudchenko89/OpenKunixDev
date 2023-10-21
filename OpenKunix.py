
import webbrowser
import time
name = input("Welcome to the OpenKunix .Enter your name.>")
print("Loading...")
time.sleep(5.5)
print("Loding Complete")
time.sleep(1.0)
print("Hello",name)

while 1:
    command = input(">>")

    if command=="help":
       print("'Commands'")
       print("notepad")
       print("internet")
       print("settings")
       print("turn-off")
       print("paint")

    if command=="notepad":
      input("")

    if command=="internet":
       url = input("URL")
       webbrowser.open(url=url)

    if command=="Vip":
        webbrowser.open(url="https://drive.google.com/file/d/1PstWpofInkwsCFxxZnZcEcI0Kh6sDCbJ/view?usp=sharing")


    if command=="turn-off":
       print("turn-off your computer")


    if command=="paint":
       import turtle
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

       turtle.onkey(mU,"Up")
       turtle.onkey(mD,"Down")
       turtle.onkey(mL,"Left")
       turtle.onkey(mR,"Right")
       turtle.onkey(cL(),"space")






        





