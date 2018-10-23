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
        lbl = Label(text = 'Comando: ' + instruccion,
        bg = 'grey').place(x = 18, y = 50)
        #print(type(instruccion))
        aux=start_ins(instruccion)
#
        lprint=show_z80()
        if len(lprint)==2:
            l1 = Label(text = str(lprint[1])).place(x = 18, y = 70)
        else:
            l1 = Label(text = str(lprint[1])).place(x = 18, y = 70)
            l2 = Label(text = str(lprint[2])).place(x = 18, y = 90)
            l3 = Label(text = str(lprint[3])).place(x = 18, y = 110)

#Main_temp
def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
