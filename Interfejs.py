from tkinter import *
import tkinter.font as font

root=Tk()
root.title("Kalkulator")
#root.geometry("500x200")
myFont = font.Font(size=16)

label=Label(root, width=35, text="").grid(row=0, column=0, columnspan=3)
entry=Entry(root, width=59, borderwidth=1,).grid(row=1, column=0, columnspan=4)

label=Label(root, width=35, text="").grid(row=2, column=0, columnspan=3)

button_next=Button(root, text="Następne równanie", fg="#ffed7a", bg="#a16d00", activeforeground="#431800", activebackground="#e49f33", padx="14", pady="10", font=myFont).grid(row=3, column=0, columnspan=2)
button_clear=Button(root, text="Kasuj", fg="#875c00", bg="#e6d047", activeforeground="#ffed7a", activebackground="#bf1717", padx="27", pady="10", font=myFont).grid(row=4,column=0)
button_x=Button(root, text="x", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="51", pady="10", font=myFont).grid(row=4,column=1)
button_y=Button(root, text="y", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="51", pady="10", font=myFont).grid(row=4,column=2)
button_z=Button(root, text="z", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="51", pady="10", font=myFont).grid(row=4,column=3)

button1=Button(root, text="1", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont).grid(row=5,column=0)
button2=Button(root, text="2", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont).grid(row=5,column=1)
button3=Button(root, text="3", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont).grid(row=5,column=2)
button3=Button(root, text="-", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="52", pady="20", font=myFont).grid(row=5,column=3)

button4=Button(root, text="4", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont).grid(row=6,column=0)
button5=Button(root, text="5", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont).grid(row=6,column=1)
button6=Button(root, text="6", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont).grid(row=6,column=2)
button6=Button(root, text="+", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="47", pady="20", font=myFont).grid(row=6,column=3)

button7=Button(root, text="7", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont).grid(row=7,column=0)
button8=Button(root, text="8", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont).grid(row=7,column=1)
button9=Button(root, text="9", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont).grid(row=7,column=2)
button9=Button(root, text="=", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="47", pady="58", font=myFont).grid(row=7, rowspan=2, column=3)

button0=Button(root, text="0", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="110", pady="20", font=myFont).grid(row=8,columnspan=2)
button_comma=Button(root, text=",", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="53", pady="20", font=myFont).grid(row=8,column=2)


root.mainloop()
