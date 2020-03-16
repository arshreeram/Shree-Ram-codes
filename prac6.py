from tkinter import*
root=Tk()
var=IntVar()
var.set(0)
lang_list=[("Python",0), ("WP",1), ("jQuery",2),("Javascript",3)]
def ShowChoice() :
    print ("You selected choice number: ", var.get() )
l=Label(root, text="Select your favourite programming language: ")
l.pack()
for txt,val in lang_list:
    r=Radiobutton(root, text=txt, variable=var,
                  command=ShowChoice, value=val)
    r.pack()
