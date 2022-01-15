from tkinter import *

root = Tk()
root.title("tk")
root.minsize(400, 300)
root.resizable(True, True)

entryA = StringVar()
entryB = StringVar()
entryResult = StringVar()

def sum():
    entryResult.set(str(float(entryA.get()) + float(entryB.get())))

def sub():
    entryResult.set(str(float(entryA.get()) - float(entryB.get())))

def mul():
    entryResult.set(str(float(entryA.get()) * float(entryB.get())))

def div():
    entryResult.set(str(float(entryA.get()) / float(entryB.get())))

def exit():
    root.quit()

Label(root, text = "Cộng trừ nhân chia", fg = "blue", font = ("tahoma", 16)).grid(row = 0, columnspan = 3)

Button(root, text = "Cộng", width = 30, command = sum).grid(row = 1, column = 0)
Button(root, text = "Trừ", width = 30, command = sub).grid(row = 2, column = 0)
Button(root, text = "Nhân chia", width = 30, command = mul).grid(row = 3, column = 0)
Button(root, text = "Trừ", width = 30, command = div).grid(row = 4, column = 0)

Label(root, text = "Số a: ").grid(row = 1, column = 1)
Label(root, text = "Số b: ").grid(row = 2, column = 1)
Label(root, text = "Kết quả: ").grid(row = 3, column = 1)

Entry(root, width = 30, textvariable = entryA).grid(row = 1, column = 2)
Entry(root, width = 30, textvariable = entryB).grid(row = 2, column = 2)
Entry(root, width = 30, textvariable = entryResult, state = DISABLED).grid(row = 3, column = 2)
Button(root, text = "Thoát", width = 30, command = exit).grid(row = 4, column = 2)

root.mainloop()
