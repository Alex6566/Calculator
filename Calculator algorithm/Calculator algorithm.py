from tkinter import * 

sobhan = Tk()
sobhan.geometry("500x500")
sobhan.title("sobhan")
sobhan.resizable(False,False)
sobhan.configure(background="lightblue")
def number ():
    z = intvar1.get() + intvar2.get()
    label.configure(text= f"my number is : {z}")

label1 = Label(sobhan,text="Welcome My App")
label1.pack()
intvar1 = IntVar()
intvar2 = IntVar()
entry1 = Entry(sobhan, textvariable=intvar1)
entry1.pack()
entry2 = Entry(sobhan, textvariable=intvar2)
entry2.pack()
button1 = Button(sobhan,text="click me " , command=number)
button1.pack()
label = Label(sobhan, text="number is :")
label.pack()


sobhan.mainloop()