from tkinter import *
import tkinter as tkinter



window = tkinter.Tk()
window.geometry("400x300")
window.title("login page")
def nextPage():
    window.destroy()
    import projectpython


window.configure(background='#32a885')

lbl1 = Label(window, text="USERNAME", font=("new roman", 15),padx=10, pady=10,  background='#32a885', fg='white')
entry1 = Entry(window)


lbl2 = Label(window, text="PASSWORD", font=("new roman", 15), padx=10, pady=10,  background='#32a885', fg='white')
entry2 = Entry(window)

btn = Button(window,
             text ="Login",
             command = nextPage, background='#ffa354', font=("new roman", 15), fg='white', height=1, width=10)
btn.pack(side=BOTTOM, padx=15, pady=10)
lbl1.pack()
entry1.pack()

lbl2.pack()
entry2.pack()

btn.pack()

window.mainloop()


