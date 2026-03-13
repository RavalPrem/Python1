from tkinter import *
window = Tk()

window.title('For loop used')
window.geometry('500x450')

def number():
    a = int(e1.get())
    b = int(e2.get())

    for i in range(a,b+1):
        print(i, end=" ")

    print('\n')

lb1 = Label(window,text="Enter num1")
lb1.grid(row=0,column=0)

e1 = Entry(window)
e1.grid(row=0,column=1)

lb2 = Label(window,text="Enter num2")
lb2.grid(row=1,column=0)

e2 = Entry(window)
e2.grid(row=1,column=1)

btn = Button(window,text="Register Numbers",command=number)
btn.grid(row=2,column=3)

window.mainloop()