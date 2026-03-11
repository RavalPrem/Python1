import tkinter as tk
window = tk.Tk()

window.title('All things')
window.geometry('500x450')

#label
lb1 = tk.Label(window,text='This is text from label')
lb1.pack()

btn = tk.Button(window,text="Just click Here")
btn.pack()

#event with button
def printInTerminal():
    print('\nThe text printed in the terminal \n')

btn2 = tk.Button(window,text="Just click for see change in the terminal",command=printInTerminal)
btn2.pack()

#checkButton
checkBtn = tk.Checkbutton(window,text="I agree terms and conditions")
checkBtn.pack(side='bottom')
# checkBtn.grid(row=10,column=35)

window.mainloop()