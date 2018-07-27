 Assignment-20
                  ------------------



Q1.Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.

from tkinter import *

root = Tk()
root.geometry('300x150')
hwl = Label(root, text='Hello World')
hwl.pack()
exit = Button(root,text='EXIT',width=25,command=root.destroy)
exit.pack(side=BOTTOM)
root.mainloop()



----------------------------------------------------------------------------------------------------------------------------------------------



Q2.Write a python program to in the same interface as above and create a action when the button is click it will display some text. 

from tkinter import *

root=Tk()
root.geometry('300x200')
root.title('GUI')
root.configure(background='black')

def onclick():
    hwp= Label(root,text='you have won a jackpot :D')
    hwp.pack()


hwl= Label(root,text='click below to win a jackpot',bg='white')
hwl.pack()

prnt = Button(root,text='->click here<-',width=12,command=onclick,bg='white')
prnt.place(relx=0.5, rely=0.5,anchor=CENTER)

exitB = Button(root,text='Exit',width=5,bg='WHITE',command=root.destroy)
exitB.pack(side=BOTTOM)

root.mainloop()



-------------------------------------------------------------------------------------------------------------------------------------------


Q3.Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.

 from tkinter import *

root=Tk()
root.geometry('500x200')
root.title('GUI')
root.configure(background='#000000')

def onclick():
    hwp= Label(root,text='you have won a jackpot :D click below again for more info')
    hwp.pack()
    
def new():
    var= 'its a joke :D'
    onclick(var)
    
f1= Frame(root,bg='#C0C0C0')
f1.pack(fill=X)
    
B1= Button(f1,text='->click here first<-',command=onclick)
B1.pack()

f2= Frame(root,bg='#C0C0C0')
f2.pack(fill=X)

B2= Button(f2,text='->click here<-',command=new)
B2.pack()

exitB = Button(root,text='Exit',width=5,bg='WHITE',command=root.destroy)
exitB.pack(side=BOTTOM)
root.mainloop()



------------------------------------------------------------------------------------------------------------------------------------------------



Q4.Write a python program using tkinter interface to take an input in the GUI program and print it.

from tkinter import *
root = Tk()
root.geometry('300x150')
root.configure(background='black')
def onclick():
    print(input1.get())
    
root.title('Window')
frame_ = Frame(root,bg='#778899')
frame_.pack(fill=X)
l1L = Label(frame_,text='Enter name',bg='#DCDCDC')
l1L.pack()

input1 = Entry(root)
input1.pack()
textB = Button(root,text='Click Me',bg='#C0C0C0', command=onclick)
textB.pack()

exitB = Button(root,text='Exit',width=5,bg='WHITE',command=root.destroy)
exitB.pack()
root.mainloop()



----------------------------------------------------------------------------------------------------------------------------------------------