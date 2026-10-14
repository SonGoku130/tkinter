from tkinter import *
win = Tk()
win.title("Demo")
win.geometry('400x400')
win.configure(bg="black")

L1 = Label(text="Enter your name below : ", fg="white", bg="light gray")
E1 = Entry(fg="white", bg="black", width=50)
L2 = Label(text="Enter your age below : ", fg="white", bg="light gray")
E2 = Entry(fg="white", bg="black", width=50)

L3  = Label(text="Enter your address below : ", fg="white", bg="light gray")
B1 = Button(text="sumbit", fg="white", bg="light gray")
'''
L1.pack()
E1.pack()
L2.pack()
E2.pack()
L3.pack()
B1.pack()

'''
L1.grid(row=0, column=0)
E1.grid(row=0, column=1, sticky='w')
L2.grid(row=1, column=0)
E2.grid(row=1, column=1, sticky='w')
L3.grid(row=2, column=0)

F = Frame(master=win, relief=GROOVE, borderwidth=15)
F.grid(row=2, column=1)
T1 = Text(master=F, fg='yellow', bg='green', width=50, height=10)
T1.pack()

B1.grid(row=3, column=0)
win.mainloop()