from tkinter import *
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
import csv
import os

root = Tk()
root.title("Healthcare Management System")
root.title("Book an appointment")
root.configure(bg='white')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1200
height = 600
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

def additem():
    e1=entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    e6=entry6.get()
    if entry1.get()=="" and entry2.get()=="" and entry3.get()=="" and entry4.get()=="" and entry5.get()=="" and entry6.get()=="":

        print("Error")
        tkMessageBox.showerror("error","there is issue with some information")

    else:
        result=tkMessageBox.askquestion("Submit","You are about to enter following details\n" + e1 + "\n" + e2 + "\n" + e3 + "\n" + e4 + "\n" + e5 +"\n" + e6 )
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        if(result =="yes"):
            print("here")
            with open("healthcare.csv", 'a') as csvfile:
                csvfile.write('{0}, {1}, {2}, {3},{4},{5}\n'.format(str(e1),e2,e3,str(e4),str(e5),e6))
                
               
            csvfile.close()
        else:
            entry1.set("")
            entry2.set("")
            entry3.set("")
            entry4.set("")
            entry5.set("")
            entry6.set("")
    
def deleteitem():
##    tree.delete(*tree.get_children())
    e1=entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    e6=entry6.get()
    if entry1.get()=="" and entry2.get()=="" and entry3.get()=="" and entry4.get()=="" and entry5.get()=="" and entry6.get()=="":
        print("Error")
        tkMessageBox.showerror("error","there is issue with some information")
    else:
        result=tkMessageBox.askquestion("Submit","You are about to delete following details\n" + e1 + "\n" + e2 + "\n" + e3 + "\n" + e4 + "\n" + e5 + "\n" + e6)

        if(result =="yes"):
            print("here")
            with open("healthcare.csv", 'r') as f, open("healthcare1.csv",  "w") as w1:
                for line in f:
                    if e1 not in line:
                        w1.write(line)
            os.remove("healthcare.csv")
            os.rename("healthcare1.csv", "healthcare.csv")
            f.close()
            w1.close()
    
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)
def updateitem():
    
    e1=entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    e6=entry6.get()
    if entry1.get()=="" and entry2.get()=="" and entry3.get()=="" and entry4.get()=="" and entry5.get()=="" and entry6.get()=="":

        print("Error")
        tkMessageBox.showerror("error","there is issue with some information")
    else:
        result=tkMessageBox.askquestion("Submit","You are about to update following details\n" + e1 + "\n" + e2 + "\n" + e3 + "\n" + e4 + "\n" + e5 + "\n" + e6)

        if(result =="yes"):
            print("here")
            with open("healthcare.csv","r") as f1 ,open("healthcare1.csv", "w") as working:
                for line in f1:
                    if str(e1) not in line:
                        working.write(line)
                    else:
                        working.write('{0}, {1}, {2}, {3},{4} ,{5}\n'.format(str(e1),e2,e3,str(e4),str(e5),e6))
            os.remove("healthcare.csv")
            os.rename("healthcare1.csv", "healthcare.csv")
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)
                                      

def viewitem():
    tree.delete(*tree.get_children())
    with open('healthcare.csv',"r") as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            Name=row['Name']
            Age =row['Age']
            Gender =row['Gender']
            Contact=row['Contact']
            Date=row['Date']
            Address=row['Address']
            tree.insert("", 0, values=(Name, Age, Gender, Contact, Date, Address ))
    f.close()
    txt_result.config(text="Successfully read the data from database", fg="black")
            
  

def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)

 


Name = StringVar()
Age = IntVar()
Gender = StringVar()
Contact = IntVar()
Date=IntVar()
Address = StringVar()

Top = Frame(root, width=900, height=50, bg="white", background="white")
Top.pack(side=TOP)
Left = Frame(root, width=200, height=1200, bd=25, bg='white',relief="flat")
Left.pack(side=LEFT)
Right = Frame(root, width=200, height=800,bd=10, bg='white',relief="flat")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=200, height=900, bg='white')
Forms.pack(side=TOP)
Buttons = Frame(Left, width=200, height=900, bd=0, bg='white', relief="ridge")
Buttons.pack(side=BOTTOM)

txt_title = Label(Top, width=900, font=('arial', 30),fg='white',text = "Healthcare Management System", padx=10, pady=5, bg='#ffa354')
txt_title.pack()
txt_title = Label(Top, width=800, font=('arial', 20),fg='white',text = "Book an appointment", bg='#ffa354')
txt_title.pack()
label0 = Label(Forms, text="Name:", fg='#32a885',font=('arial', 17), bd=17, bg='white')
label0.grid(row=0, stick="e")
label1 = Label(Forms, text="Age:",fg='#32a885', font=('arial', 17), bd=17, bg='white')
label1.grid(row=1, stick="e")
label2 = Label(Forms, text="Gender:",fg='#32a885', font=('arial', 17), bd=17, bg='white')
label2.grid(row=2, stick="e")
label3 = Label(Forms, text="Contact:",fg='#32a885', font=('arial', 17), bd=17, bg='white')
label3.grid(row=3, stick="e")
label4 = Label(Forms, text="Date:",fg='#32a885', font=('arial', 17), bd=17, bg='white')
label4.grid(row=4, stick="e")
label5 = Label(Forms, text="Address:",fg='#32a885', font=('arial', 17), bd=17, bg='white')
label5.grid(row=5, stick="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)

entry1 = Entry(Forms, textvariable=Name, width=50, relief="solid")
entry1.grid(row=0, column=1) 
entry2 = Entry(Forms, textvariable=Age, width=50, relief="solid")
entry2.grid(row=1, column=1)
entry3 = Entry(Forms, textvariable=Gender, width=50, relief="solid")
entry3.grid(row=2, column=1)
entry4 = Entry(Forms, textvariable=Contact, width=50, relief="solid")
entry4.grid(row=3, column=1)
entry5 = Entry(Forms, textvariable=Date, width=50,relief="solid")
entry5.grid(row=4, column=1)
entry6 = Entry(Forms, textvariable=Address, width=50,relief="solid")
entry6.grid(row=5, column=1)

btn_add = Button(Buttons, width=12, text="ADD", command=additem, foreground='white', background='#32a885' )
btn_add.pack(side=LEFT)
btn_delete = Button(Buttons, width=12, text="DELETE", command=deleteitem, foreground='white', background='#32a885')
btn_delete.pack(side=LEFT)
btn_update = Button(Buttons, width=12, text="UPDATE", command=updateitem, foreground='white', background='#32a885' )
btn_update.pack(side=LEFT)
btn_view = Button(Buttons, width=12, text="VIEW", command=viewitem, foreground='white', background='#32a885')
btn_view.pack(side=LEFT)
btn_clear = Button(Buttons, width=12, text="CLEAR", command=clearitem, foreground='white', background='#32a885')
btn_clear.pack(side=LEFT)

scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=( "Name", "Age", "Gender", "Contact","Date", "Address"),
                    selectmode="extended", height=600, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

tree.heading('Name', text="Name", anchor=W)
tree.heading('Age', text="Age", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Contact', text="Contact", anchor=W)
tree.heading('Date', text="Date", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.column('#0', stretch=NO, minwidth=22, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=80)

tree.pack()


if __name__ == '__main__':
    root.mainloop()
    

#name contactnumber date gender age doctor
