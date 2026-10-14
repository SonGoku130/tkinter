from tkinter import *
win = Tk() 
win.title("Test window")
win.geometry('300x300')
Lab = Label(text="Hello user", fg="blue", bg="black")
But = Button(text="Click me", fg="yellow", bg="red")
Ent = Entry(fg="red", bg="Blue", width=50)

Lab.pack()
But.pack()
Ent.pack()

win.mainloop()