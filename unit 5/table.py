from tkinter import *
window = Tk()

window.title('For loop used')
window.geometry('500x450')

def number():
    a = int(e1.get())

    for i in range(1,11):
        print(f'\n{a} * {i} = {a * i}')
    print('\n')

lb1 = Label(window,text="Enter num1")
lb1.grid(row=0,column=0)

e1 = Entry(window)
e1.grid(row=0,column=1)

btn = Button(window,text="Generate the Table",command=number)
btn.grid(row=1,column=3)

window.mainloop()