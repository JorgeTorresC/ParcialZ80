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

def start_ins(ins):
    #print (ins)
    toUser = list()
    itx = list()
    l = ALZ80.lector(ins)
    #print(itx, len(itx))
    #print(l)
    ALZ80.Lexema(l, itx)
    #print ("ITX",itx)
    LToCpu = EnlzCarg.enlazador(dicFunciones, registros, itx)
    #print(LToCpu)
    if LToCpu[0] == 0:
        toUser.append(0)
        toUser.append(LToCpu[1])
        return toUser
    else:
        if len(LToCpu) == 3:
            operar(LToCpu[1],LToCpu[2],'')
        elif len(LToCpu) == 2:
            operar(LToCpu[1],'','')
        else:
            #print("paso por aquí")
            operar(LToCpu[1],LToCpu[2],LToCpu[3])
