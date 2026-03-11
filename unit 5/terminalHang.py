#I want to hack your window terminal
import tkinter as tk
window = tk.Tk()

window.title('Here click')
window.geometry('500x450')

def somethingIsHere():
    for i in range(1,100000000000):
        print('There is a text')

btn1 = tk.Button(window,text="Click Here please",command=somethingIsHere)
btn1.pack()

window.mainloop()