from tkinter import *


def Hello(event):
    print("Hello world")
    text.insert(INSERT, "Hello.....")


def Bye(event):
    print("Good bye!")
    root.destroy()


root = Tk()

text = Text(root)
text.pack()

btn1 = Button(root, text="Click me", width=30, height=5, bg="white", fg="black")
btn1.bind("<Button-1>", Hello)
btn1.pack()

btn2 = Button(root, text="Exit", width=30, height=5, bg="red", fg="black")
btn2.bind("<Button-1>", Bye)
btn2.pack()

root.mainloop()
