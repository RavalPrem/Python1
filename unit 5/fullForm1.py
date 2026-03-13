from tkinter import *

window = Tk()

window.title('The Form')
window.geometry('600x550')

def showDetails():
    print('\nAll details down below')
    print(f'name : {nameBox.get()}')
    print(f'age : {ageBox.get()}')
    print(f'gender : {r.get()}')

lb1 = Label(window,text="Enter name")
lb1.grid(row=0,column=0)

nameBox = Entry(window)
nameBox.grid(row=0,column=1)

lb2 = Label(window,text="Enter Your age")
lb2.grid(row=1,column=0)

ageBox = Entry(window)
ageBox.grid(row=1,column=1)

r = StringVar()
r1 = Radiobutton(window,text="Male",variable=r,value="Male")
r1.grid(row=2,column=1)

r2 = Radiobutton(window,text="Female",variable=r,value="FeMale")
r2.grid(row=2,column=2)

regBtn = Button(window,text="Register",command=showDetails)
regBtn.grid(row=3,column=2)

window.mainloop()