
import tkinter as tk
from  tkinter import *
root=tk.Tk()
root.geometry("800x600")
root.resizable(False,False)
cv = Canvas(root, bg = "white",bd=2,relief="groove")
cv.place(height=580,width=780,x=10,y=10)
line1 = cv.create_line(10, 10, 100, 200, fill="green", width=4)
line2 = cv.create_line(200, 100, 300, 250, 450, 120, fill="#FF00FF")
box1=cv.create_rectangle(500, 200, 700, 300, outline="#888888")
ovl=cv.create_oval(500, 200, 700, 300, fill="#FFFF00", width=3)
txt=cv.create_text(650,500,fill="blue",font="arial 30 italic bold",text="sobhan")
poly=cv.create_polygon(400,400,500,400,500,500,400,500,300,450,fill="red")
coord = 10, 300, 210, 500
arc = cv.create_arc(coord, start=0, extent=150, fill="cyan")
box2=cv.create_rectangle(coord)
root.mainloop()