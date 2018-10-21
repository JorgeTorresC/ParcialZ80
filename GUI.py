#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import getpass


auxY=50
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
        global auxY, instruccion
        instruccion = self.into.get()
        lbl=Label(text = 'Comando: ' + instruccion,
        bg='grey').place(x=18, y=auxY)
        auxY = auxY + 20
        #print(type(instruccion))
        if auxY >330:
            auxY = 50

#Main_temp
def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
