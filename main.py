# -*- coding: utf-8 -*-
# *************************
# 11 De Octubre del 2018
# Emulador Procesador Z80
# Jorge Ivan Torres
# Daniel Caita
# *************************
import Funcions
import Z80
import os
from ALZ80 import *

f = sys.stdin.readlines()
for line in f:
    itx = list()
    linea = line
    l=lector(linea)
    #print(l)
    if Lexema(l) == -1:
        break
    print(itx, len(itx))
