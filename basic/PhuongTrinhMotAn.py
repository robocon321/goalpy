from tkinter import *

root = Tk()
root.title("Giải phương trình")
root.minsize(400, 300)
root.resizable(True, True)

a = StringVar()
b = StringVar()
result = StringVar()

Label(root, text = "Phương trình bậc 1", fg = "red", font = ("tohama", 16), justify = CENTER).grid(row = 0, columnspan = 2)

Label(root, text = "Hệ số a: ").grid(row = 1, column = 0)
Entry(root, width = 30, textvariable = a).grid(row = 1, column = 1)

Label(root, text = "Hệ số b: "). grid(row = 2, column = 0)
Entry(root, width = 30, textvariable = b).grid(row = 2, column = 1)

def doExcute():
    numA = float(a.get())
    numB = float(b.get())
    if numA == 0 and numB == 0:
        result.set("Vô số nghiệm")
    elif numA == 0 and numB !=0:
        result.set("Vô nghiệm")
    else:
        result.set("x=" + str((-numB/numA)))

def doExit():
    root.destroy()

def doClear():
    a.set("")
    b.set("")

frameButton = Frame()
Button(frameButton, text = "Giải", command = doExcute).pack(side = LEFT)
Button(frameButton, text = "Tiếp", command = doClear).pack(side = LEFT)
Button(frameButton, text = "Thoát", command = doExit).pack(side = LEFT)
frameButton.grid(row = 3, columnspan = 2)

Label(root, text = "Kết quả: ").grid(row = 4, column = 0)
Entry(root, width = 30, textvariable = result).grid(row = 4, column = 1)

root.mainloop()
