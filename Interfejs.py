import tkinter as tk
import tkinter.font as font
import main

#FUNKCJE ZWRACAJACE WYNIK | POCZATEK
#ZMIENNE NA DANE | SAVED_LIST - LISTA NA ROWNANIA | VECTOR - LISTA NA WYRAZY WOLNE
vector = []
saved_list=[]
macierz_do_licz_wyznacznika = []


alf_table = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ROZMIAR_MACIERZY = len(saved_list)


def wyzeruj_macierz_do_licz_wyznacznika():
    for j in range(ROZMIAR_MACIERZY):
        pomoc = []
        for i in range(ROZMIAR_MACIERZY): pomoc.append(0)
        macierz_do_licz_wyznacznika.append(pomoc)
        del pomoc


def is_letter(letter):
    if ( letter >= 'A' and letter <= 'Z' ) or ( letter >= 'a' and letter <= 'z' ): return True
    return False


def is_number(character):
    if character <= '9' and character >= '0': return True
    return False


def change_to_big(char):
    if ord(char) > 96: return chr(ord(char) - 32)
    return char


def create_matrix():
    counter = 1
    for row in range(len(saved_list)):
        for element in range(len(saved_list[row])):
            if is_letter(saved_list[row][element]) and saved_list[row][element] != '+' and \
                    saved_list[row][element] != '-' and saved_list[row][element] != '=':
                #ZAPAMIETUJE W KTORYM MIEJSCU W MACIERZY WSAWIC WSPOLCZYNNIK
                actual_letter = change_to_big(saved_list[row][element])
                if alf_table[ord(actual_letter)-65] == 0: 
                    alf_table[ord(actual_letter)-65] = counter
                    counter+=1

                #ZAPAMIETUJE MIEJSCE WYSTAPIENIA ZMIENNEJ I OD TEGO MOMENTU COFA SIE DOPOKI NAPOTYKA INT
                remember_position_of_element = element
                element -= 1
                if saved_list[row][element] == '+' or element<0:
                    result = 1
                elif saved_list[row][element] == '-':
                    result = -1
                else:
                    #ZMIENNE DO TWORZENIA WSPOLCZYNNIKA PRZY ZMIENNEJ
                    multipler = 1
                    result = 0
                    #OBLICZANIE WSPOLCZYNNIKA PRZY ZMIENNEJ
                    while is_number(saved_list[row][element]):
                        result += (int(saved_list[row][element])*multipler)
                        multipler *= 10
                        element -= 1
                    if saved_list[row][element] == '-': result = -result
                #POWROT ELEMENTU DO MIEJSCA WYSTAPIENIA ZMIENNEJ
                element = remember_position_of_element
                macierz_do_licz_wyznacznika[row][alf_table[ord(actual_letter)-65]-1] = result


def change_column(column_to_change):
    for i in range(len(macierz_do_licz_wyznacznika)):
        macierz_do_licz_wyznacznika[i][column_to_change] = vector[i]


def dodaj_kolumny(kolumna, kolumna_0):

    for i in range(ROZMIAR_MACIERZY):
        macierz_do_licz_wyznacznika[i][kolumna_0] += macierz_do_licz_wyznacznika[i][kolumna]


def odejmij_wektory(wektor_modyfikowany, wektor_bazowy, mnoznik):

    assert len(wektor_modyfikowany) == len(wektor_bazowy)

    for i in range(len(wektor_modyfikowany)):
        wektor_modyfikowany[i] -= mnoznik * wektor_bazowy[i]


def zeruj_kolumne(gorny_wiersz, lewa_kolumna):

    kolumna_bez_0 = lewa_kolumna
    while kolumna_bez_0 < ROZMIAR_MACIERZY and macierz_do_licz_wyznacznika[gorny_wiersz][kolumna_bez_0] == 0:
        kolumna_bez_0 += 1

    if kolumna_bez_0 < ROZMIAR_MACIERZY:
        if kolumna_bez_0 > lewa_kolumna:
            dodaj_kolumny(kolumna_bez_0, lewa_kolumna)

        for wiersz in range(gorny_wiersz + 1, ROZMIAR_MACIERZY):
            if macierz_do_licz_wyznacznika[wiersz][gorny_wiersz] != 0:
                mnoznik = macierz_do_licz_wyznacznika[wiersz][gorny_wiersz] / \
                          macierz_do_licz_wyznacznika[gorny_wiersz][lewa_kolumna]
                odejmij_wektory(macierz_do_licz_wyznacznika[wiersz], macierz_do_licz_wyznacznika[gorny_wiersz], mnoznik)


def licz_wyznacznik(gorny_wiersz, lewa_kolumna):

    for nr_wiersza in range(ROZMIAR_MACIERZY):
        assert ROZMIAR_MACIERZY == len(macierz_do_licz_wyznacznika[nr_wiersza])

    if lewa_kolumna == ROZMIAR_MACIERZY and gorny_wiersz == ROZMIAR_MACIERZY:
        return macierz_do_licz_wyznacznika[0][0]
    else:
        zeruj_kolumne(gorny_wiersz, lewa_kolumna)
        return macierz_do_licz_wyznacznika[gorny_wiersz][lewa_kolumna] * \
                  licz_wyznacznik(gorny_wiersz + 1, lewa_kolumna + 1)


#FUNKCJE ZWRACAJACE WYNIK | KONIEC

var = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'x', 'y', 'z']

def numbers_active(num):
    if (num):
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
    else:
        button1["state"] = tk.DISABLED
        button2["state"] = tk.DISABLED
        button3["state"] = tk.DISABLED
        button4["state"] = tk.DISABLED
        button5["state"] = tk.DISABLED
        button6["state"] = tk.DISABLED
        button7["state"] = tk.DISABLED
        button8["state"] = tk.DISABLED
        button9["state"] = tk.DISABLED
        button0["state"] = tk.DISABLED

def vector_fun(list):
    a=0
    c=''
    for element in list:
        for i in element:
            for sign in i:
                if a==1:
                    c+=sign
                if sign=='=':
                    a=1
    vector.append(c)
    #print("Wektor: ", vector)

def variables(list):
    for i in list:
        for sign in i:
            if sign == 'x':
                button_x["state"] = tk.DISABLED
            if sign == 'y':
                button_y["state"] = tk.DISABLED
            if sign == 'z':
                button_z["state"] = tk.DISABLED

            if list=='j':
                button_x["state"] = tk.NORMAL
                button_y["state"] = tk.NORMAL
                button_z["state"] = tk.NORMAL
                numbers_active(1)

def change(number):
    current = []
    for_vector = []


    current.append(entry.get())
    if number == '=':
        save(current)

    if number == 'n':
        for_vector.append(current)
        vector_fun(for_vector)
        numbers_active(1)
        clear()
        variables('j')



    else:
        entry.delete(0, tk.END)
        entry.insert(0, str(current[0]) + str(number))


    if number=='-' or number=='+' or number==',':
        numbers_active(1)
        button3_1["state"] = tk.DISABLED
        button6_1["state"] = tk.DISABLED
        button_comma["state"] = tk.DISABLED
        button_x["state"] = tk.NORMAL
        button_y["state"] = tk.NORMAL
        button_z["state"] = tk.NORMAL
        variables(current)


        if number==',':
            variables(current)
            button_comma["state"] = tk.DISABLED


    if (number=='='):
        numbers_active(1)
        variables(current)
        button_x["state"] = tk.DISABLED
        button_y["state"] = tk.DISABLED
        button_z["state"] = tk.DISABLED
        button_comma["state"] = tk.DISABLED
        button3_1["state"] = tk.DISABLED
        button6_1["state"] = tk.DISABLED

    if number!='-'and number!='+' and number!=',' and number!='=' and number!='n':
        variables(current)
        button3_1["state"] = tk.NORMAL
        button6_1["state"] = tk.NORMAL
        button_comma["state"] = tk.NORMAL


    if number in var:
        numbers_active(0)
        button_comma["state"]= tk.DISABLED
        button_x["state"]= tk.DISABLED
        button_y["state"]= tk.DISABLED
        button_z["state"]= tk.DISABLED



def clear():
    entry.delete(0,tk.END)
    numbers_active(1)
    button_comma["state"] = tk.DISABLED
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

    button1=tk.Button(root,text="a", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf", padx="51", pady="20", font=myFont, command=lambda: [change('a'), powrot()])
    button2 =tk.Button(root,text="b", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="50", pady="20", font=myFont, command=lambda: [change('b'), powrot()])
    button3 = tk.Button(root,text="c", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="50", pady="20", font=myFont, command=lambda:[change('c'), powrot()])
    button3_1 = tk.Button(root,text="-", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158",padx="52", pady="20", font=myFont, command=lambda: change('-'))
    button4 = tk.Button(root,text="d", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="50", pady="20", font=myFont, command=lambda: [change('d'), powrot()])
    button5 = tk.Button(root,text="e", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="50", pady="20", font=myFont, command=lambda: [change('e'), powrot()])
    button6 = tk.Button(root,text="f", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="52", pady="20", font=myFont, command=lambda: [change('r'), powrot()])
    button6_1 = tk.Button(root,text="+", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158",padx="47", pady="20", font=myFont, command=lambda: change('+'))
    button7 = tk.Button(root,text="g", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="50", pady="20", font=myFont, command=lambda: [change('g'), powrot()])
    button8 = tk.Button(root,text="h", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="50", pady="20", font=myFont, command=lambda: [change('h'), powrot()])
    button9 = tk.Button(root,text="i", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="53", pady="20", font=myFont, command=lambda: [change('i'), powrot()])
    button9_1 = tk.Button(root,text="=", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158",padx="47", pady="58", font=myFont, command=lambda: change('='))
    button0 = tk.Button(root,text="0", fg="#875c00", bg="#ffff9c", activeforeground="#875c00", activebackground="#ffffcf",padx="110", pady="20", font=myFont, command=lambda: change(0))
    button_var = tk.Button(root,text="cyfry", fg="#ffed7a", bg="#a16d00", activeforeground="#431800",activebackground="#e49f33", padx="30", pady="10", font=myFont, command=powrot)
    button_x["state"] = tk.DISABLED
    button_y["state"] = tk.DISABLED
    button_z["state"] = tk.DISABLED

    button1.grid(row=5, column=0)
    button2.grid(row=5, column=1)
    button3.grid(row=5, column=2)
    button3_1.grid(row=5, column=3)
    button4.grid(row=6, column=0)
    button5.grid(row=6, column=1)
    button6.grid(row=6, column=2)
    button7.grid(row=7, column=0)
    button8.grid(row=7, column=1)
    button9.grid(row=7, column=2)
    button0.grid(row=8, columnspan=2)
    button_var.grid(row=3, column=2)
    button_oblicz.grid(row=3, column=3)
def save(list):

    saved_list.append(list)
    #print("Saved list: ", saved_list)

def powrot():
    button1 = tk.Button(root, state=tk.NORMAL, text="1", fg="#875c00", bg="#ffff9c", activeforeground="#875c00",activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(1))
    button2 = tk.Button(root, state=tk.NORMAL, text="2", fg="#875c00", bg="#ffff9c", activeforeground="#875c00",activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(2))
    button3 = tk.Button(root, state=tk.NORMAL, text="3", fg="#875c00", bg="#ffff9c", activeforeground="#875c00",activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(3))
    button4 = tk.Button(root, state=tk.NORMAL, text="4", fg="#875c00", bg="#ffff9c", activeforeground="#875c00",activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(4))
    button5 = tk.Button(root, state=tk.NORMAL, text="5", fg="#875c00", bg="#ffff9c", activeforeground="#875c00",activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(5))
    button6 = tk.Button(root, state=tk.NORMAL, text="6", fg="#875c00", bg="#ffff9c", activeforeground="#875c00",activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(6))
    button7 = tk.Button(root, state=tk.NORMAL, text="7", fg="#875c00", bg="#ffff9c", activeforeground="#875c00",activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(7))
    button8 = tk.Button(root, state=tk.NORMAL, text="8", fg="#875c00", bg="#ffff9c", activeforeground="#875c00",activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(8))
    button9 = tk.Button(root, state=tk.NORMAL, text="9", fg="#875c00", bg="#ffff9c", activeforeground="#875c00",activebackground="#ffffcf", padx="50", pady="20", font=myFont, command=lambda: change(9))
    button0 = tk.Button(root, state=tk.NORMAL, text="0", fg="#875c00", bg="#ffff9c", activeforeground="#875c00",activebackground="#ffffcf", padx="110", pady="20", font=myFont, command=lambda: change(0))
    button_var = tk.Button(root, state=tk.NORMAL, text="zmienne", fg="#ffed7a", bg="#a16d00",activeforeground="#431800", activebackground="#e49f33", padx="11", pady="10", font=myFont,command=zamiana)
    # button_x["state"] = tk.NORMAL
    # button_y["state"] = tk.NORMAL
    # button_z["state"] = tk.NORMAL
    numbers_active(0)


    button1.grid(row=5, column=0)
    button2.grid(row=5, column=1)
    button3.grid(row=5, column=2)
    button3_1.grid(row=5, column=3)
    button4.grid(row=6, column=0)
    button5.grid(row=6, column=1)
    button6.grid(row=6, column=2)
    button7.grid(row=7, column=0)
    button8.grid(row=7, column=1)
    button9.grid(row=7, column=2)
    button0.grid(row=8, columnspan=2)
    button_var.grid(row=3, column=2)


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
button_var = tk.Button(root, state=tk.NORMAL, text="zmienne", fg="#ffed7a", bg="#a16d00", activeforeground="#431800",activebackground="#e49f33", padx="12", pady="10", font=myFont, command=zamiana)
button_next=tk.Button(root, state=tk.NORMAL, text="Następne równanie", fg="#ffed7a", bg="#a16d00", activeforeground="#431800", activebackground="#e49f33", padx="14", pady="10", font=myFont, command=lambda:change('n'))
button_clear=tk.Button(root, text="Kasuj", fg="#875c00", bg="#e6d047", activeforeground="#ffed7a", activebackground="#bf1717", padx="27", pady="10", font=myFont, command=clear)
button_x=tk.Button(root, text="x", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="51", pady="10", font=myFont, command=lambda: change('x'))
button_y=tk.Button(root, text="y", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="51", pady="10", font=myFont ,command=lambda: change('y'))
button_z=tk.Button(root, text="z", fg="#875c00", bg="#e6d047", activeforeground="#431800", activebackground="#f7e158", padx="51", pady="10", font=myFont, command=lambda: change('z'))
button_oblicz=tk.Button(root, text="oblicz", fg="#ffed7a", bg="#a16d00", activeforeground="#431800", activebackground="#e49f33", padx="25", pady="10", font=myFont, command=create_matrix)

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
button_var.grid(row=3,column=2)
button_oblicz.grid(row=3,column=3)
button_next.grid(row=3,column=0,columnspan=2)
button_clear.grid(row=4,column=0)
button_x.grid(row=4,column=1)
button_y.grid(row=4,column=2)
button_z.grid(row=4,column=3)

#root.geometry("500x200")

entry.grid(row=1, column=0, columnspan=4)


root.mainloop()

