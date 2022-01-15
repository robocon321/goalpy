from tkinter import *

a = 1
root = Tk()

# Create Title
root.title("Paint App ")

# specify size
def keyup(e):
    global a
    a+=1
    print('up', a)

frame = Frame(root, width=100, height=100)
frame.bind("<KeyRelease>", keyup)
frame.pack()
frame.focus_set()
root.mainloop()