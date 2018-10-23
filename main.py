# -*- coding: utf-8 -*-
# *************************
# 11 De Octubre del 2018
# Emulador Procesador Z80
# Jorge Ivan Torres
# Daniel Caita
# *************************

import Funcions
from Z80CPU import dicFunciones, registros, operar
import EnlzCarg
import os
import ALZ80
#from GUI import *

def start_ins(ins):
    for line in ins:
        toUser = list()
        itx = list()
        linea = line
        l = ALZ80.lector(linea)
        #print(l)
        if ALZ80.Lexema(l, itx) == -1:
            break
        #print(itx, len(itx))
        LToCpu = EnlzCarg.enlazador(dicFunciones, registros, itx)
        if LToCpu[0] == 0:
            toUser.append(0)
            toUser.append(LToCpu[1])
            return toUser
        else:
            if len(LToCpu) == 3:
                operar (LToCpu[1],LToCpu[2],'')
            else:
                operar (LToCpu[1],LToCpu[2],LToCpu[3])


"""
f = sys.stdin.readlines()
for line in f:
    itx = list()
    linea = line
    l=lector(linea)
    #print(l)
    if Lexema(l) == -1:
        break
    print(itx, len(itx))
"""
