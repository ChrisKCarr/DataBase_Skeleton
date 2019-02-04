from tkinter import Tk, StringVar, ttk, messagebox
from tkinter import *
import time
import datetime
#-----------------------------Frames-----------------------------------
root = Tk()
root.title("Efficency Tracker")
root.geometry('1350x650+0+0')
root.configure(background='black')

LeftFrame = Frame(root, width=1000, height=650, bd=8, relief='raise')
LeftFrame.pack(side=LEFT)         
RightFrame = Frame(root, width=350, height=650, bd=8, relief='raise')
RightFrame.pack(side=RIGHT)   

LeftFrame1 = Frame(LeftFrame, width=1000, height=100, bd=8, relief='raise')
LeftFrame1.pack(side=TOP) 
LeftFrame2 = Frame(LeftFrame, width=1000, height=550, bd=8, relief='raise')
LeftFrame2.pack(side=TOP)

RightFrame1 = Frame(RightFrame, width=350, height=215, bd=8, relief='raise')
RightFrame1.pack(side=TOP) 
RightFrame2 = Frame(RightFrame, width=350, height=415, bd=8, relief='raise')
RightFrame2.pack(side=TOP)
#-----------------------------Variables---------------------------------
DateofOrder = StringVar()
value0 = StringVar()
value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
value4 = StringVar()
value5 = StringVar()
value6 = StringVar()
value7 = StringVar()
value8 = StringVar()
value9 = StringVar()
value10 = StringVar()
value11= StringVar()
value12= StringVar()

def Register():
    if value0.get() == "/":
        value0.set('/')
        value1.set("/")
        value2.set(" ")
        value3.set("/")
        value4.set("/")
        value5.set("/")
        value6.set("/")
        value7.set("/")
        value8.set("/")
        value9.set("/")
        value10.set("/")
        value11.set("/")
        value12.set("/")
    elif value0.get() == "Business":
        value0.set("Business")
        value1.set("Business")
        value2.set("Business")
        value3.set("Business")
        value4.set("Business")
        value5.set("Business")
        value6.set("Business")
        value7.set("Business")
        value8.set("Business")
        value9.set("Business")
        value10.set("Business")
        value11.set("Business")
        value12.set("Business")
    elif value0.get() == "Code":
        value0.set("Code")
        value1.set("Code")
        value2.set("Code")
        value3.set("Code")
        value4.set("Code")
        value5.set("Code")
        value6.set("Code")
        value7.set("Code")
        value8.set("Code")
        value9.set("Code")
        value10.set("Code")
        value11.set("Code")
        value12.set("Code")
    elif value0.get() == "Gym":
        value0.set("Gym")
        value1.set("Gym")
        value2.set("Gym")
        value3.set("Gym")
        value4.set("Gym")
        value5.set("Gym")
        value6.set("Gym")
        value7.set("Gym")
        value8.set("Gym")
        value9.set("Gym")
        value10.set("Gym")
        value11.set("Gym")
        value12.set("Gym")
    elif value0.get() == "Relax":
        value0.set("Relax")
        value1.set("Relax")
        value2.set("Relax")
        value3.set("Relax")
        value4.set("Relax")
        value5.set("Relax")
        value6.set("Relax")
        value7.set("Relax")
        value8.set("Relax")
        value9.set("Relax")
        value10.set("Relax")
        value11.set("Relax")
        value12.set("Relax")
    elif value0.get() == "Work":
        value0.set("Work")
        value1.set("Work")
        value2.set("Work")
        value3.set("Work")
        value4.set("Work")
        value5.set("Work")
        value6.set("Work")
        value7.set("Work")
        value8.set("Work")
        value9.set("Work")
        value10.set("Work")
        value11.set("Work")
        value12.set("Work")

def Reset():
    value0.set("")
    value1.set("")
    value2.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")
    value8.set("")
    value9.set("")
    value10.set("")
    value11.set("")
    value12.set("")

def qExit():
    qExit = messagebox.askyesno("Exit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return
#-----------------------------Components--------------------------------
DateofOrder.set(time.strftime("%d/%m/%Y"))
#-----------------------------LeftFrame1-----------------------------------
lblNo = Label(LeftFrame1, font=('arial',10,'bold'), text='No.', bd=16)
lblNo.grid(row=0, column=0, sticky=W)
lblUserId = Label(LeftFrame1, font=('arial',10,'bold'), text='User Id', bd=16)
lblUserId.grid(row=0, column=1, sticky=W)
lblUserName = Label(LeftFrame1, font=('arial',10,'bold'), text='User Name', bd=16)
lblUserName.grid(row=0, column=2, sticky=W)
lblCode = Label(LeftFrame1, font=('arial',10,'bold'), text='Code', bd=16)
lblCode.grid(row=0, column=3, sticky=W)

box = ttk.Combobox(LeftFrame1, textvariable=value0, state='readonly')
box['values'] = ('/','Business','Code','Gym','Relax','Work')
box.current(0)
box.grid(row=0, column=4)
DateofOrder.set(time.strftime("%d/%m/%Y"))

btnFill = Button(LeftFrame1, text='Fill', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=12, height=1, command= Register).grid(row=0, column=5)
btnReset = Button(LeftFrame1, text='Reset', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=12, height=1, command=Reset
                  ).grid(row=0, column=6)
btnExit = Button(LeftFrame1, text='Exit', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=12, height=1, command=qExit
                 ).grid(row=0, column=7)

lblDateofOrder = Label(LeftFrame1, font=('arial',10,'bold'),textvariable=DateofOrder,
                       padx=2, pady=2, bd=2, fg='black', bg='white', relief='sunken')
lblDateofOrder.grid(row=0, column=8, sticky=W)
#-----------------------------LeftFrame2 Row1-----------------------------------
lblNo = Label(LeftFrame2, font=('arial',10,'bold'), text='1', bd=16)
lblNo.grid(row=0, column=0, sticky=W)

lblUser_ID = Label(LeftFrame2, font=('arial',10,'bold'), text='1234',padx=2,
                  pady=2, bd=2, fg='black', width=18)
lblUser_ID.grid(row=0, column=1, sticky=W)
lblUser_Name = Label(LeftFrame2, font=('arial',10,'bold'), text='Chris Carr',padx=2,
                  pady=2, bd=2, fg='black', width=12)
lblUser_Name.grid(row=0, column=2, sticky=W)
lbl_Code = Label(LeftFrame2, font=('arial',10,'bold'), text='13431',padx=2,
                  pady=2, bd=2, fg='black', width=12)
lbl_Code.grid(row=0, column=3, sticky=W)

box = ttk.Combobox(LeftFrame2, textvariable=value1, state='readonly')
box['values'] = ('/','Business','Code','Gym','Relax','Work')
box.current(0)
box.grid(row=0, column=4)

btnSpace = Button(LeftFrame2, text='', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=12, height=1).grid(row=0, column=5)
btnSpace = Button(LeftFrame2, text='', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=11, height=1).grid(row=0, column=6)
btnSpace = Button(LeftFrame2, text='', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=11, height=1).grid(row=0, column=7)
btnSpace = Button(LeftFrame2, text='', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=11, height=1).grid(row=0, column=8)
#-----------------------------LeftFrame2 Row2-----------------------------------
lblNo = Label(LeftFrame2, font=('arial',10,'bold'), text='2', bd=16)
lblNo.grid(row=1, column=0, sticky=W)
lblUser_ID = Label(LeftFrame2, font=('arial',10,'bold'), text='4231',padx=2,
                  pady=2, bd=2, fg='black', width=18)
lblUser_ID.grid(row=1, column=1, sticky=W)
lblUser_Name = Label(LeftFrame2, font=('arial',10,'bold'), text='Nati Wales',padx=2,
                  pady=2, bd=2, fg='black', width=12)
lblUser_Name.grid(row=1, column=2, sticky=W)
lbl_Code = Label(LeftFrame2, font=('arial',10,'bold'), text='1005',padx=2,
                  pady=2, bd=2, fg='black', width=12)
lbl_Code.grid(row=1, column=3, sticky=W)

box = ttk.Combobox(LeftFrame2, textvariable=value1, state='readonly')
box['values'] = ('/','Business','Code','Gym','Relax','Work')
box.current(0)
box.grid(row=1, column=4)

btnSpace = Button(LeftFrame2, text='', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=12, height=1).grid(row=1, column=5)
btnSpace = Button(LeftFrame2, text='', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=11, height=1).grid(row=1, column=6)
btnSpace = Button(LeftFrame2, text='', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=11, height=1).grid(row=1, column=7)
btnSpace = Button(LeftFrame2, text='', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=11, height=1).grid(row=1, column=8)
#-----------------------------LeftFrame2 Row3-----------------------------------
lblNo = Label(LeftFrame2, font=('arial',10,'bold'), text='3', bd=16)
lblNo.grid(row=2, column=0, sticky=W)
lblUser_ID = Label(LeftFrame2, font=('arial',10,'bold'), text='4231',padx=2,
                  pady=2, bd=2, fg='black', width=18)
lblUser_ID.grid(row=2, column=1, sticky=W)
lblUser_Name = Label(LeftFrame2, font=('arial',10,'bold'), text='Mis',padx=2,
                  pady=2, bd=2, fg='black', width=12)
lblUser_Name.grid(row=2, column=2, sticky=W)
lbl_Code = Label(LeftFrame2, font=('arial',10,'bold'), text='1005',padx=2,
                  pady=2, bd=2, fg='black', width=12)
lbl_Code.grid(row=2, column=3, sticky=W)

box = ttk.Combobox(LeftFrame2, textvariable=value1, state='readonly')
box['values'] = ('/','Business','Code','Gym','Relax','Work')
box.current(0)
box.grid(row=2, column=4)

btnSpace = Button(LeftFrame2, text='', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=12, height=1).grid(row=2, column=5)
btnSpace = Button(LeftFrame2, text='', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=11, height=1).grid(row=2, column=6)
btnSpace = Button(LeftFrame2, text='', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=11, height=1).grid(row=2, column=7)
btnSpace = Button(LeftFrame2, text='', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=11, height=1).grid(row=2, column=8)



root.mainloop()


