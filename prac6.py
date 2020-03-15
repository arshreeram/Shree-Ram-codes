from tkinter import*
root=Tk()
v=IntVar()
v.set(0)
lang_list=[("Python",0), ("WP",1), ("jQuery",2),
           ("Javascript",3) ]
def ShowChoice() :
    print ("You selected choice number: ", v.get() )
l=Label(root, text="Select your favourite programming language: ")
l.pack()
for txt,val in lang_list:
    r=Radiobutton(root, text=txt, variable=v,
                  command=ShowChoice, value=val)
    r.pack()
