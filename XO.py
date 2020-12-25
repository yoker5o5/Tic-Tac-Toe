#This is just fun project created by yoker5o5 to learn python

import sys
from tkinter import *
import random

class Player:
    def __init__(self, name, znak):
        self.name = name
        self.znak = znak
        # self.table = []
        self.score = 0

class Tabla:
    def __init__(self, players, boja):
        self.pro = Toplevel()
        self.players = players
        self.boja = boja
        self.igra = self.players[0] if self.players[0].znak == "X" else self.players[1]
        self.ucitajpolja()
        #self.pro.mainloop()

    def ucitajpolja(self):
        # for pl in self.players:
        #     for ta in pl.table:
        #         if (self, pl.score) in ta:
        #             pl.table.remove((self, pl.score))
        #         pl.table.append((self, pl.score))
        self.polja = []
        self.frame = Frame(self.pro, bg=self.boja)
        self.frame.grid(column=0, row = 0)
        for i in range(3):
            for j in range(3):
                self.polja.append(Polje((i,j), " ", self))

        L2 = Label(self.frame, text="{} - {}".format(self.players[0].score, self.players[1].score), height=5, width=12)
        L2.grid(row=9, column=1)

        L2 = Label(self.frame, text="{}\n{}".format(self.players[0].name, self.players[0].znak), height=5, width=12)
        L2.grid(row=9, column=0)

        L3 = Label(self.frame, text="{}\n{}".format(self.players[1].name, self.players[1].znak), height=5, width=12)
        L3.grid(row=9, column=2)

    def Polja(self):
        return self.polja
    
    def checkwinner(self):
        zbir = [0]*8
        poljaint = []
        for polje in self.polja:
            poljaint.append(polje.znakint)
            for j in range(2):
                for i in range(3):
                    if polje.pos[j] == i:
                        i = i + 3 if j == 1 else i
                        zbir[i] += polje.znakint
            if polje.pos[0] == polje.pos[1]:
                zbir[6] += polje.znakint
            if polje.pos[0]+polje.pos[1] == 2:
                zbir[7] += polje.znakint
        for i in range(8):
            if zbir[i] == 3:
                self.showwinner("X")
            elif zbir[i] == 6:
                self.showwinner("O")
        if 10 not in poljaint:
            self.showwinner("No-one")
    def showwinner(self, znak):
        win = znak
        for pl in self.players:
            if pl.znak == znak:
                win = pl.name
                pl.score += 1
            pl.znak = "O" if pl.znak == "X" else "X"
        window = Frame(self.pro,bg=self.boja)
        window.place(relx=0,rely=0,relheight=1,relwidth=1)
        L = Label(window, text="Winner is: {}".format(win), height=1, width=5)
        L.place(relx=0.1,rely=0.1,relheight=0.5,relwidth=0.8)
        back = Button(window, text ="Back", height=1, width=2, command= lambda: self.ucitajpolja()) # command=self.__init__(self.pro, self.pos, self.players, self.boja)
        back.place(relx=0.4,rely=0.5,relheight=0.1,relwidth=0.2)
        
        


class Polje:
    def __init__(self, pos, znak, tabla):
        self.pos = pos
        self.znak = znak
        self.tabla = tabla
        self.createbutton()
    def createbutton(self):
        self.button = Button(self.tabla.frame, text = self.znak, command=self.update, height=10, width=24)
        self.button.grid(row=self.pos[0], column=self.pos[1])
    def update(self):
        if self.znak == " ":
            self.znak = self.tabla.igra.znak
            self.button.configure(text = self.tabla.igra.znak)
            self.tabla.igra = self.tabla.players[1] if self.tabla.igra == self.tabla.players[0] else self.tabla.players[0]
            self.tabla.checkwinner()
    
    @property
    def znak(self):
        return self._znak
    
    @znak.setter
    def znak(self, znak):
        self._znak = znak
        if znak == " ":
            self.znakint = 10
        elif znak == "X":
            self.znakint = 1
        elif znak == "O":
            self.znakint = 2


class CreatingTable:
    def __init__(self):
        root = Tk()
        root.geometry("500x500")
        root.title("TIC-TAC-TOE")
        window = Frame(root)
        window.place(relx=0.2,rely=0.2,relheight=0.5,relwidth=0.8)
        L = Label(window, text = "Unesi imena igrača:", font=("Century", 24))
        L.grid(row=0, column=0)
        E = Entry(window, width=10, bd=5, font=("Century", 24))
        E.grid(row=1, column=0)
        E2 = Entry(window, width=10, bd=5, font=("Century", 24))
        E2.grid(row=2, column=0)
        B = Button(window, text="Submit", command=lambda: self.createtable(E, E2), height=2, width=20)
        B.grid(row=3, column=0)
        root.mainloop()
    def createtable(self, e, e2):
        colors= ["blue", "red", "lightblue", "pink", "black"]
        players = []
        players.append(Player(e.get(), "X"))
        players.append(Player(e2.get(), "O"))
        Tabla(players, random.choice(colors))
        e.delete(0, END)
        e2.delete(0, END)

def main(*args):
    CreatingTable()
    # pl1 = Player("Djordje", "X")
    # pl2 = Player("Dragos", "O")
    # pl3 = Player("Boris", "O")
    # pl4 = Player("Davorin", "X")
    # root = Tk()
    # root.geometry("500x500")
    # root.title("TIC-TAC-TOE")
    # window = Frame(root)
    # window.place(relx=0.2,rely=0.2,relheight=0.5,relwidth=0.8)
    # L = Label(window, text = "Unesi imena igrača:", font=("Century", 24))
    # L.grid(row=0, column=0)
    # E = Entry(window, width=10, bd=5, font=("Century", 24))
    # E.grid(row=1, column=0)
    # E2 = Entry(window, width=10, bd=5, font=("Century", 24))
    # E2.grid(row=2, column=0)
    # B = Button(window, text="Submit", command=lambda: createtable(E, E2), height=2, width=20)
    # B.grid(row=3, column=0)
    #root.attributes("-fullscreen", True)
    # Tabla((pl1, pl2), "blue")
    # Tabla((pl3, pl4), "red")
    # root.mainloop()
    #Tabla(root, (1,1), (pl3, pl4),"black")

# def page1():
#     #Loading page where game acually is
#     global P, B, igrac, prvi #Not sure if this is right way
#     root.geometry("532x600")
#     window = Frame(root,bg='lightblue')
#     window.place(relx=0,rely=0,relheight=1,relwidth=1)
#     B = [[0]*3]*3
#     P = [[10]*3]*3
#     igrac = 0
#     prvi = 0 if prvi == 1 else 1
#     for i in range(3):
#         B[i] = [0]*3
#         P[i] = [10]*3 #Not sure why didnt work with just previus assigments
#         for j in range(3):
#             B[i][j] = Button(window, text =" ", command=lambda x=[i, j]: XO(x), height=10, width=24) #10 24
#             B[i][j].grid(row=i, column=j)

#     window2 = Frame(window,bg='lightblue')
#     window2.grid(row=9, column=1)

#     L=[0]*len(pl)
#     for i, _ in enumerate(pl):
#         L[i] = Label(window2, text="{}".format(pl[i]), height=5, width=12)
#         L[i].grid(row=1, column=i)    

#     znak=[""]*len(pl)
#     if prvi == 0:
#         znak[0] = "X"
#         znak[1] = "O"
#     else: 
#         znak[0] = "O"
#         znak[1] = "X"
#     window3 = Frame(window,bg='lightblue')
#     window3.grid(row=9, column=0)
#     L2 = Label(window3, text="Player 1\n{}".format(znak[0]), height=5, width=12)
#     L2.grid(row=0, column=0)

#     window4 = Frame(window,bg='lightblue')
#     window4.grid(row=9, column=2)
#     L3 = Label(window4, text="Player 2\n{}".format(znak[1]), height=5, width=12)
#     L3.grid(row=0, column=0)

# def XO(x): #What button do
# #   It puts X and O one by one
#     global igrac
#     i = x[0]
#     j = x[1]
#     if B[i][j]["text"] == " ":
#         if igrac == 0: 
#             B[i][j].configure(text="X")
#             P[i][j] = 1 #Puts ID of X to Matrix P
#             igrac = 1
#         elif igrac == 1:
#             B[i][j].configure(text="O")
#             P[i][j] = 2 #Puts ID of O to Matrix P
#             igrac = 0

# #   Here we sum all posible 3 in row
#         zbir = [0]*8
#         P2 = []
#         for j in range(3):
#             for i in range(3):
#                 P2.append(P[i][j])
#                 zbir[j] += P[i][j]
#                 zbir[j+3] += P[j][i]
#                 if i == j:
#                     zbir[6] += P[i][j]
#                 if (i+j) == 2:
#                     zbir[7] += P[i][j]

# #   Now check if sum is 3 for X or 6 for O
#         for i in range(8):
#             if zbir[i] == 3:
#                 page2("X")
#                 pl[prvi] += 1
#             elif zbir[i] == 6:
#                 page2("O")
#                 pl[abs(prvi-1)] += 1
#             elif 10 not in P2:
#                 page2("No-one")

# def page2(winner): #declare winner on other page
#     window = Frame(root,bg='lightblue')
#     window.place(relx=0,rely=0,relheight=1,relwidth=1)
#     L = Label(window, text="Winner is: {}".format(winner), height=1, width=5)
#     L.place(relx=0.1,rely=0.1,relheight=0.5,relwidth=0.8)
#     back = Button(window, text ="Back", command=page1, height=1, width=2)
#     back.place(relx=0.4,rely=0.5,relheight=0.1,relwidth=0.2)

if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)