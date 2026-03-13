from tkinter import *
window = Tk()

window.title('ArithMetic Operations')
window.geometry('600x450')

def arithAddition():
    #the non readable code when uncommented
    # print(f'\n{int(e1.get())} + {int(e2.get())} = {int(e1.get()) + int(e2.get())}')
    # print(f'\n{int(e1.get())} - {int(e2.get())} = {int(e1.get()) - int(e2.get())}')
    # print(f'\n{int(e1.get())} * {int(e2.get())} = {int(e1.get()) * int(e2.get())}')
    # print(f'\n{int(e1.get())} / {int(e2.get())} = {int(e1.get()) / int(e2.get())}')

    a = int(e1.get())
    b = int(e2.get())

    #readable code (for me)
    print(f'\n{a} + {b} = {a+b}')
    print(f'\n{a} - {b} = {a-b}')
    print(f'\n{a} * {b} = {a*b}')
    print(f'\n{a} / {b} = {a/b}')

lb1 = Label(window,text="Enter num1")
lb1.grid(row=0,column=0)

e1 = Entry(window)
e1.grid(row=0,column=1)

lb2 = Label(window,text="Enter num2")
lb2.grid(row=1,column=0)

e2 = Entry(window)
e2.grid(row=1,column=1)

btn = Button(window,text="Register Numbers",command=arithAddition)
btn.grid(row=2,column=3)


window.mainloop()