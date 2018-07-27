Assignment-21
                      ---------------------



Q1. Create a dict with name and mobile number.
#Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.

import tkinter
from tkinter import *
tk=Tk()
tk.geometry('300x100')
tk.configure(background='black')
tk.title("GUI")
data={'Rohan':'8521479063','Ashwani':'9063258741','Kunal':'7041258963','Yash':'8052369147'}
Label(tk,text="Enter your name",fg="white",bg="black").pack()
e1=Entry(tk)
e1.pack()
scrollbar=Scrollbar(tk)
scrollbar.pack(side=RIGHT,fill=Y)
mylist=Listbox(tk,yscrollcommand=scrollbar.set)
for key in data.keys():
    mylist.insert(END,key)
mylist.pack(side=LEFT)
scrollbar.config(command=mylist.yview)
Button(tk,text="Exit",fg="black",bg="white",command=tk.destroy).pack()
tk.mainloop()



------------------------------------------------------------------------------------------------------------



Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.

import tkinter
from tkinter import *
tk=tkinter.Tk()
tk.configure(background='black')
tk.title("update")

label1=Label(tk,text="Enter your name",fg="white",bg="black").grid(row=0)
label2=Label(tk,text="Enter your phone number",fg="white",bg="black").grid(row=1)
x=StringVar()
y=IntVar()
e1=Entry(tk,textvariable=x)
e2=Entry(tk,textvariable=y)
a={'Rohan':'8521479063','Ashwani':'9063258741','Kunal':'7041258963','Yash':'8052369147'}
def insert_items(x,y):
    a.update({x:int(y)})
    print(a)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
Button(tk,text="Execute",fg="black",bg="white",command=lambda :insert_items(x.get(),y.get())).grid(row=3,column=0,sticky=W)
Button(tk,text="Exit",fg="black",bg="white",command=tk.destroy).grid(row=3,column=1,sticky=W)
tk.mainloop()



--------------------------------------------------------------------------------------------------------------------------------------