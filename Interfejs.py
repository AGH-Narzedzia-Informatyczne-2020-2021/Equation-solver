import tkinter as tk
import tkinter.font as font
import main

saved_list=[]


def change(number):
    current = []

    current.append(entry.get())
    if number == '=':
        save(current)
        clear()

    else:
        entry.delete(0, tk.END)
        entry.insert(0, str(current[0]) + str(number))
        print(current)

    if number=='-' or number=='+' or number==',':
        button3_1["state"] = tk.DISABLED
        button6_1["state"] = tk.DISABLED
        button_comma["state"] = tk.DISABLED
        button1["state"] = tk.NORMAL
        button2["state"] = tk.NORMAL
        button3["state"] = tk.NORMAL
        button4["state"] = tk.NORMAL
        button5["state"] = tk.NORMAL
        button6["state"] = tk.NORMAL
        button7["state"] = tk.NORMAL
        button8["state"] = tk.NORMAL
        button9["state"] = tk.NORMAL
        button0["state"] = tk.NORMAL
        button_x["state"] = tk.NORMAL
        button_y["state"] = tk.NORMAL
        button_z["state"] = tk.NORMAL
        if number==',':
            button_x["state"] = tk.DISABLED
            button_y["state"] = tk.DISABLED
            button_z["state"] = tk.DISABLED
            button_comma["state"] = tk.DISABLED
    if number!='-'and number!='+' and number!=',':
        button3_1["state"] = tk.NORMAL
        button6_1["state"] = tk.NORMAL
        button_comma["state"] = tk.NORMAL
        button_x["state"] = tk.NORMAL
        button_y["state"] = tk.NORMAL
        button_z["state"] = tk.NORMAL

    if number=='x' or number=='y' or number=='z':
        button1["state"]= tk.DISABLED
        button2["state"]= tk.DISABLED
        button3["state"]= tk.DISABLED
        button4["state"]= tk.DISABLED
        button5["state"]= tk.DISABLED
        button6["state"]= tk.DISABLED
        button7["state"]= tk.DISABLED
        button8["state"]= tk.DISABLED
        button9["state"]= tk.DISABLED
        button0["state"]= tk.DISABLED
        button_comma["state"]= tk.DISABLED
        button_x["state"]= tk.DISABLED
        button_y["state"]= tk.DISABLED
        button_z["state"]= tk.DISABLED

    if number=='':
        button1["state"] = tk.NORMAL
        button2["state"] = tk.NORMAL
        button3["state"] = tk.NORMAL
        button4["state"] = tk.NORMAL
        button5["state"] = tk.NORMAL
        button6["state"] = tk.NORMAL
        button7["state"] = tk.NORMAL
        button8["state"] = tk.NORMAL
        button9["state"] = tk.NORMAL
        button0["state"] = tk.NORMAL
        button_comma["state"] = tk.DISABLED
        button_x["state"] = tk.NORMAL
        button_y["state"] = tk.NORMAL
        button_z["state"] = tk.NORMAL

def clear():
    entry.delete(0,tk.END)
    button1["state"] = tk.NORMAL
    button2["state"] = tk.NORMAL
    button3["state"] = tk.NORMAL
    button4["state"] = tk.NORMAL
    button5["state"] = tk.NORMAL
    button6["state"] = tk.NORMAL
    button7["state"] = tk.NORMAL
    button8["state"] = tk.NORMAL
    button9["state"] = tk.NORMAL
    button0["state"] = tk.NORMAL
    button_comma["state"] = tk.NORMAL
    button_x["state"] = tk.NORMAL
    button_y["state"] = tk.NORMAL
    button_z["state"] = tk.NORMAL


root=tk.Tk()
myFont = font.Font(size=16)
root.title("Kalkulator")
label=tk.Label(root, width=35, text="").grid(row=0, column=0, columnspan=3)
entry=tk.Entry(root, width=59, borderwidth=1,)




label=tk.Label(root, width=35, text="").grid(row=2, column=0, columnspan=3)

def zamiana():
    button1=tk.Button(root, text="a", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="51", pady="20", font=myFont, command=lambda: change('a')).grid(row=5,column=0)
    button2 =tk.Button(root, text="b", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="50", pady="20", font=myFont, command=lambda: change('b')).grid(row=5, column=1)
    button3 = tk.Button(root, text="c", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="50", pady="20", font=myFont, command=lambda: change('c')).grid(row=5, column=2)
    button3_1 = tk.Button(root, text="-", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158",padx="52", pady="20", font=myFont, command=lambda: change('-')).grid(row=5, column=3)
    button4 = tk.Button(root, text="d", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="50", pady="20", font=myFont, command=lambda: change('d')).grid(row=6, column=0)
    button5 = tk.Button(root, text="e", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="50", pady="20", font=myFont, command=lambda: change('e')).grid(row=6, column=1)
    button6 = tk.Button(root, text="f", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="52", pady="20", font=myFont, command=lambda: change('f')).grid(row=6, column=2)
    button6_1 = tk.Button(root, text="+", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158",padx="47", pady="20", font=myFont, command=lambda: change('+')).grid(row=6, column=3)
    button7 = tk.Button(root, text="g", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="50", pady="20", font=myFont, command=lambda: change('g')).grid(row=7, column=0)
    button8 = tk.Button(root, text="h", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="50", pady="20", font=myFont, command=lambda: change('h')).grid(row=7, column=1)
    button9 = tk.Button(root, text="i", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="53", pady="20", font=myFont, command=lambda: change('i')).grid(row=7, column=2)
    button9_1 = tk.Button(root, text="=", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158",padx="47", pady="58", font=myFont, command=lambda: change('=')).grid(row=7, rowspan=2, column=3)
    button0 = tk.Button(root, text="0", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="110", pady="20", font=myFont, command=lambda: change(0)).grid(row=8, columnspan=2)
    button_var = tk.Button(root, text="cyfry", fg="#ffed7a", bg="#a16d00", activeforeground="#431800",activebackground="#e49f33", padx="32", pady="10", font=myFont, command=main).grid(row=3,column=2,columnspan=2)

def save(current):

    saved_list.append(current)
    for i in saved_list:
        print(saved_list)


button1=tk.Button(root, state=tk.NORMAL, text="1", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(1))
button2=tk.Button(root, state=tk.NORMAL, text="2", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(2))
button3=tk.Button(root, state=tk.NORMAL, text="3", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(3))
button3_1=tk.Button(root, state=tk.NORMAL, text="-", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="52", pady="20", font=myFont, command=lambda: change('-'))
button4=tk.Button(root, state=tk.NORMAL, text="4", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(4))
button5=tk.Button(root, state=tk.NORMAL, text="5", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(5))
button6=tk.Button(root, state=tk.NORMAL, text="6", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(6))
button6_1=tk.Button(root, state=tk.NORMAL, text="+", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="47", pady="20", font=myFont, command=lambda: change('+'))
button7=tk.Button(root, state=tk.NORMAL, text="7", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(7))
button8=tk.Button(root, state=tk.NORMAL, text="8", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(8))
button9=tk.Button(root, state=tk.NORMAL, text="9", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(9))
button9_1=tk.Button(root, state=tk.NORMAL, text="=", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="47", pady="58", font=myFont, command=lambda: change('='))
button0=tk.Button(root, state=tk.NORMAL, text="0", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="110", pady="20", font=myFont, command=lambda: change(0))
button_comma=tk.Button(root, state=tk.DISABLED, text=",", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="53", pady="20", font=myFont, command=lambda: change(','))
button_var = tk.Button(root, state=tk.DISABLED, text="zmienne", fg="#ffed7a", bg="#a16d00", activeforeground="#431800",activebackground="#e49f33", padx="14", pady="10", font=myFont, command=zamiana)
button_next=tk.Button(root, state=tk.DISABLED, text="Następne równanie", fg="#ffed7a", bg="#a16d00", activeforeground="#431800", activebackground="#e49f33", padx="14", pady="10", font=myFont)
button_clear=tk.Button(root, text="Kasuj", fg="#875c00", bg="#e6d047", activeforeground="#ffed7a", activebackground="#bf1717", padx="27", pady="10", font=myFont, command=clear)
button_x=tk.Button(root, text="x", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="51", pady="10", font=myFont, command=lambda: change('x'))
button_y=tk.Button(root, text="y", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="51", pady="10", font=myFont ,command=lambda: change('y'))
button_z=tk.Button(root, text="z", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="51", pady="10", font=myFont, command=lambda: change('z'))

button1.grid(row=5,column=0)
button2.grid(row=5,column=1)
button3.grid(row=5,column=2)
button3_1.grid(row=5,column=3)
button4.grid(row=6,column=0)
button5.grid(row=6,column=1)
button6.grid(row=6,column=2)
button6_1.grid(row=6,column=3)
button7.grid(row=7,column=0)
button8.grid(row=7,column=1)
button9.grid(row=7,column=2)
button9_1.grid(row=7,column=3, rowspan=2)
button0.grid(row=8,columnspan=2)
button_comma.grid(row=8,column=2)
button_var.grid(row=3,column=2,columnspan=2)
button_next.grid(row=3,column=0,columnspan=2)
button_clear.grid(row=4,column=0)
button_x.grid(row=4,column=1)
button_y.grid(row=4,column=2)
button_z.grid(row=4,column=3)
#root.geometry("500x200")



button_next=Button(root, text="Następne równanie", fg="#ffed7a", bg="#a16d00", activeforeground="#431800", activebackground="#e49f33", padx="14", pady="10", font=myFont).grid(row=3, column=0, columnspan=2)
button_clear=Button(root, text="Kasuj", fg="#875c00", bg="#e6d047", activeforeground="#ffed7a", activebackground="#000000", padx="27", pady="10", font=myFont).grid(row=4,column=0)
button_x=Button(root, text="x", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="51", pady="10", font=myFont).grid(row=4,column=1)
button_y=Button(root, text="y", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="51", pady="10", font=myFont).grid(row=4,column=2)
button_z=Button(root, text="z", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="51", pady="10", font=myFont).grid(row=4,column=3)






entry.grid(row=1, column=0, columnspan=4)

root.mainloop()

