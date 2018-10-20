# -*- coding: utf-8 -*-
# *************************
# 11 De Octubre del 2018
# Emulador Procesador Z80
# Jorge Ivan Torres
# *************************
import Funcions
import Z80
#num_bytes=int(input('cuantos bytes tiene la instruccion'))
#while num_bytes!=0 and num_bytes <=4:
#    inst=str(input('ingrese la instruccion'))
inst=str(input('ingrese la instruccion '))
opcode=Funcions.take_opcode(inst)
print(opcode)

Z80.LD_01('0000000010101111')
localbc=Z80.INC_03()
print (localbc)
