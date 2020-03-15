from tkinter import *
root = Tk()
def callback():
    print("Click!")
button1= Button(root, text="ONE",
                command=callback, bg="Green",
                fg="RED")
button2= Button(root, text="TWO",
                command=callback,
                bg="Red", fg="Green")
button1.pack(side=LEFT)
button2.pack(side=RIGHT)
