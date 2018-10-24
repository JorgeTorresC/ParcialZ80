# -*- coding: utf-8 -*-
# *************************
# 11 De Octubre del 2018
# Emulador Procesador Z80
# Jorge Ivan Torres
# Daniel Caita
# *************************

from tkinter import *
from tkinter import ttk
import getpass
from main import start_ins
from Z80CPU import show_z80

instruccion = ''

class Aplicacion():
    def __init__(self):

        self.auxY=10
        self.raiz = Tk()
        self.raiz.geometry('500x400')

        self.raiz.resizable(width=False,height=False)
        self.raiz.title('Z80')

        self.into = StringVar()
        self.ctext1 = ttk.Entry(self.raiz, textvariable=self.into,
                                width=45).place(x=18, y=10)

        self.bsend = ttk.Button(self.raiz, text='Enter',
                                command=self.verCOMANDO).place(x=400, y=8)

        self.bsalir = ttk.Button(self.raiz, text='Salir',
                                 command=self.raiz.destroy).place(x=400, y=350)
        self.raiz.mainloop()

    def verCOMANDO(self):
        global instruccion
        instruccion = self.into.get()
        limp = "                                             "
        lbllimpiar1 = Label(text = limp).place(x = 18, y = 50)
        lbllimpiar2 = Label(text = limp).place(x = 18, y = 70)
        lbllimpiar3 = Label(text = limp).place(x = 18, y = 90)
        lbllimpiar4 = Label(text = limp).place(x = 18, y = 110)
        lbllimpiar5 = Label(text = limp).place(x = 18, y = 130)
        lbllimpiar5 = Label(text = limp).place(x = 18, y = 150)
        lbllimpiar5 = Label(text = limp).place(x = 18, y = 170)
        lbllimpiar5 = Label(text = limp).place(x = 18, y = 190)
        lbllimpiar5 = Label(text = limp).place(x = 18, y = 210)
        lbl = Label(text = 'Comando: ' + instruccion,
        bg = 'grey').place(x = 18, y = 50)
        #print(type(instruccion))
        aux=start_ins(instruccion)
#
        lprint=show_z80()
        if len(lprint)==2:
            l1 = Label(text = str(lprint[1])).place(x = 18, y = 70)
        else:
            l3 = Label(text = 'F  ' + str(lprint[1])).place(x = 18, y = 70) #Flags
            l1 = Label(text = 'A ' + str(lprint[2])).place(x = 18, y = 90)
            l2 = Label(text = 'B ' + str(lprint[3])).place(x = 18, y = 110)
            l4 = Label(text = 'C ' + str(lprint[4])).place(x = 18, y = 130)
            l5 = Label(text = 'D ' + str(lprint[5])).place(x = 18, y = 150)
            l6 = Label(text = 'E ' + str(lprint[6])).place(x = 18, y = 170)
            l7 = Label(text = 'H ' + str(lprint[7])).place(x = 18, y = 190)
            l8 = Label(text = 'L ' + str(lprint[8])).place(x = 18, y = 210)

#Main_temp
def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
