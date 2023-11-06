# team ashiane is back
from tkinter import *
from tkinter import ttk
root=Tk()


checkbutton=ttk.Checkbutton(root,text='spam ?')
checkbutton.pack()
spam=StringVar()
spam.set('SPAM!')

checkbutton.config(variable = spam,onvalue =' spam hast',offvalue=' spam nist')


def button_callback():
    print(spam.get())

button=ttk.Button(root,text='print spam ',command=button_callback)
button.pack()

root.mainloop()

