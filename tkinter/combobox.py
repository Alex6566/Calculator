import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
root = tk.Tk()
root.geometry('200x200')
root.resizable(False, False)
root.title('Combobox expert')
def categorychanged(event):
    msg = f'You selected {cmbCategories.get()}!'
    showinfo(title='Result', message=msg)
categories = ['ARM','AVR','Medical Equipment','Programming','Software','Analog','Digital']
lblCategory = ttk.Label(text="Please select a category: ")
lblCategory.place(height=20,width=150,x=20,y=50)
strCategory = tk.StringVar()
cmbCategories = ttk.Combobox(root, textvariable=strCategory)
cmbCategories.place(height=30,width=150,x=20,y=80)
cmbCategories['values'] = categories
cmbCategories.bind('<<ComboboxSelected>>', categorychanged)
cmbCategories.current(5)
root.mainloop()