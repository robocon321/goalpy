from datetime import datetime
import time
import random as rd
from tkinter import *

g = 0
widthScreen = 500
heightScreen = 500
pipeSwitch = True
spacePipe = 100
maxHeightPipe = 400
minHeightPipe = 200
widthPipe = 50
secondGeneratePipe = 12
message = ""
isGameover = False
score = 0
jump = 10

root = Tk()
root.minsize(widthScreen, heightScreen)
canvas = Canvas(root, bg = "white", width = widthScreen, height = heightScreen)
canvas.pack()

ball = canvas.create_oval((100, 100, 115, 115), fill = "green")
pipes = []
scoreCanvas = canvas.create_text(100,10, text="Score: {}".format(score), anchor="nw", fill="black", font =("Helvetica", 15))

def generatePipe():
    height = rd.randint(minHeightPipe, maxHeightPipe)
    pipes.append((canvas.create_rectangle((widthScreen, 0, widthScreen + widthPipe, height), fill = "red"), canvas.create_rectangle((widthScreen, height + spacePipe, widthScreen + widthPipe, heightScreen), fill = "red")))

def removePipe():
    pipes.pop()

def movePipes():
    for pipe in pipes:
        for i in pipe:
            canvas.move(i, -1, 0)

def moveBall():
    global g
    g += 2
    for i in range(g):
        canvas.move(ball, 0, 1)

def jumpUp():
    global g
    g = 0
    for i in range(jump):
        canvas.move(ball, 0, -i)

def checkGameOver():
    global isGameover
    if(canvas.coords(ball)[1] <= 0 or canvas.coords(ball)[1] >= heightScreen):
        isGameover = True

def keyPress(event):
    if(event.keysym == "space"): jumpUp()

def checkCrossPipe():
    for pipe in pipes:
        if(canvas.coords(ball)[2] >= canvas.coords(pipe[0])[0] and canvas.coords(ball)[0] <= canvas.coords(pipe[0])[2]):
            if(canvas.coords(ball)[1] < canvas.coords(pipe[0])[3] or canvas.coords(ball)[3] > canvas.coords(pipe[1])[1]):
                global isGameover
                isGameover = True
                break
            if(canvas.coords(ball)[0] == canvas.coords(pipe[0])[2]):
                global score
                print(score)
                score += 1
                break

def findXCenter(canvas, item):
    coords = canvas.bbox(item)
    xOffset = (widthScreen / 2) - ((coords[2] - coords[0]) / 2)
    return xOffset

def drawScore():
    canvas.itemconfigure(scoreCanvas, text = "Score: {}".format(score))

canvas.bind_all("<KeyPress>", keyPress)

while not isGameover:
    checkCrossPipe()
    drawScore()
    checkGameOver()
    moveBall()
    movePipes()

    canvas.update()
    time.sleep(0.05)
    if(datetime.now().second % secondGeneratePipe == 0):
        if(pipeSwitch):
            generatePipe()
            pipeSwitch = False
    else: pipeSwitch = True
else:
    canvas.delete("all")
    text = canvas.create_text(0,0, text="Game over", anchor="nw", fill="black", font =("Helvetica", 20))
    xOffset = findXCenter(canvas, text)
    canvas.move(text, xOffset, 0)

root.mainloop()
