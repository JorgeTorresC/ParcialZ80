#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import getpass

# La clase 'Aplicacion' ha crecido. En el ejemplo se incluyen
# nuevos widgets en el método constructor __init__(): Uno de
# ellos es el botón 'Info'  que cuando sea presionado llamará
# al método 'verinfo' para mostrar información en el otro
# widget, una caja de texto: un evento ejecuta una acción:

auxY=50
instruccion = ''
class Aplicacion():
    def __init__(self):

        # En el ejemplo se utiliza el prefijo 'self' para
        # declarar algunas variables asociadas al objeto
        # ('mi_app')  de la clase 'Aplicacion'. Su uso es
        # imprescindible para que se pueda acceder a sus
        # valores desde otros métodos:
        self.auxY=10
        self.raiz = Tk()
        self.raiz.geometry('500x400')

        # Impide que los bordes puedan desplazarse para
        # ampliar o reducir el tamaño de la ventana 'self.raiz':

        self.raiz.resizable(width=False,height=False)
        self.raiz.title('Z80')

        # Define el widget Text 'self.tinfo ' en el que se
        # pueden introducir varias líneas de texto:
        self.into = StringVar()
        self.ctext1 = ttk.Entry(self.raiz, textvariable=self.into,
                                width=45).place(x=18, y=10)
        #self.into.set(getpass.getuser())

        # Sitúa la caja de texto 'self.tinfo' en la parte
        # superior de la ventana 'self.raiz':


        # Define el widget Button 'self.binfo' que llamará
        # al metodo 'self.verinfo' cuando sea presionado

        self.bsend = ttk.Button(self.raiz, text='Enter',
                                command=self.verCOMANDO).place(x=400, y=8)

        # Coloca el botón 'self.binfo' debajo y a la izquierda
        # del widget anterior

        # Define el botón 'self.bsalir'. En este caso
        # cuando sea presionado, el método destruirá o
        # terminará la aplicación-ventana 'self.raíz' con
        # 'self.raiz.destroy'

        self.bsalir = ttk.Button(self.raiz, text='Salir',
                                 command=self.raiz.destroy).place(x=400, y=350)

        # Coloca el botón 'self.bsalir' a la derecha del
        # objeto anterior.

        # El foco de la aplicación se sitúa en el botón
        # 'self.binfo' resaltando su borde. Si se presiona
        # la barra espaciadora el botón que tiene el foco
        # será pulsado. El foco puede cambiar de un widget
        # a otro con la tecla tabulador [tab]

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



def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
