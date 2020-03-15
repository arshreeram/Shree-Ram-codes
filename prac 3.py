from tkinter import  *
root=Tk()
def callback():
    print("Click!")
b=Button(root, text="OK", command=callback, bg="red",
         fg="Green")
b.pack()
