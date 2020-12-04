import sys
import os
from tkinter import *

def main(*args):
    global root, pl, prvi
    pl = [0]*2
    root = Tk()
    root.title("X O")
    prvi = 1
    page1()
    root.mainloop()

def page1():
    global P, B, igrac, prvi
    root.geometry("532x600")
    window = Frame(root,bg='lightblue')
    window.place(relx=0,rely=0,relheight=1,relwidth=1)
    B = [[0]*3]*3
    P = [[10]*3]*3
    igrac = 0
    #photo = PhotoImage(file = r"O.png") 
    prvi = 0 if prvi == 1 else 1
    for i in range(3):
        B[i] = [0]*3
        P[i] = [10]*3
        for j in range(3):
            B[i][j] = Button(window, text =" ", command=lambda x=[i, j]: XO(x), height=10, width=24) #10 24
            B[i][j].grid(row=i, column=j)

    window2 = Frame(window,bg='lightblue')
    window2.grid(row=9, column=1)

    L=[0]*len(pl)
    for i, _ in enumerate(pl):
        L[i] = Label(window2, text="{}".format(pl[i]), height=5, width=12)
        L[i].grid(row=1, column=i)    

    znak=[""]*len(pl)
    if prvi == 0:
        znak[0] = "X"
        znak[1] = "O"
    else: 
        znak[0] = "O"
        znak[1] = "X"
    window3 = Frame(window,bg='lightblue')
    window3.grid(row=9, column=0)
    L2 = Label(window3, text="Player 1\n{}".format(znak[0]), height=5, width=12)
    L2.grid(row=0, column=0)

    window4 = Frame(window,bg='lightblue')
    window4.grid(row=9, column=2)
    L3 = Label(window4, text="Player 2\n{}".format(znak[1]), height=5, width=12)
    L3.grid(row=0, column=0)

def XO(x):
    global igrac
    i = x[0]
    j = x[1]
    if B[i][j]["text"] == " ":
        if igrac == 0:
            #photo = PhotoImage(file = r"X.png") 
            B[i][j].configure(text="X")
            P[i][j] = 1
            igrac = 1
        elif igrac == 1:
            #photo = PhotoImage(file = r"X.png") 
            B[i][j].configure(text="O")
            P[i][j] = 2
            igrac = 0

        zbir = [0]*8
        P2 = []
        for j in range(3):
            for i in range(3):
                P2.append(P[i][j])
                zbir[j] += P[i][j]
                zbir[j+3] += P[j][i]
                if i == j:
                    zbir[6] += P[i][j]
                if (i+j) == 2:
                    zbir[7] += P[i][j]

        for i in range(8):
            if zbir[i] == 3:
                page2("X")
                pl[prvi] += 1
            elif zbir[i] == 6:
                page2("O")
                pl[abs(prvi-1)] += 1
            elif 10 not in P2:
                page2("No-one")

def page2(winner):
    window = Frame(root,bg='lightblue')
    window.place(relx=0,rely=0,relheight=1,relwidth=1)
    L = Label(window, text="Winner is: {}".format(winner), height=1, width=5)
    L.place(relx=0.1,rely=0.1,relheight=0.5,relwidth=0.8)
    back = Button(window, text ="Back", command=page1, height=1, width=2)
    back.place(relx=0.4,rely=0.5,relheight=0.1,relwidth=0.2)

if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)