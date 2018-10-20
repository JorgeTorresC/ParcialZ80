# -*- coding: utf-8 -*-
# *************************
# 11 De Octubre del 2018
# Emulador Procesador Z80
# Jorge Ivan Torres
# Daniel Caita
# *************************

#Tomar opcode
def take_opcode(instr):
    if len(instr) == 8:
        x = instr[0:2]
        y = instr[2:5]
        z = instr[5:8]
        opcode = hex( int(x,2) )
        print(x)
        print(y)
        print(z)
        return opcode
    elif len(instr) == 16 or len(instr) == 24:
        opcode = hex( int(instr[0:8],2) )
        return opcode
    elif len(instr) == 32:
        opcode = hex(int(instr[0:16],2))
        return opcode

    #print(opcode)
    #print(type(opcode))

def Rell_Zeros(arg):
    aux = ''
    if len(arg)==10:
        return arg[2:10]
    elif len(arg)==9:
        aux = '0' + arg[2:9]
        return aux
    elif len(arg)==8:
        aux = '00' + arg[2:8]
        return aux
    elif len(arg)==7:
        aux = '000' + arg[2:7]
        return aux
    elif len(arg)==6:
        aux = '0000' + arg[2:6]
        return aux
    elif len(arg)==5:
        aux = '00000' + arg[2:5]
        return aux
    elif len(arg)==4:
        aux = '000000' + arg[2:4]
        return aux
    elif len(arg)==3:
        aux = '0000000' + arg[2:3]
        return aux

"""
opd1='01111000'
opd2='0111100011001001'
opd3='011110001100100100000000'
opd4='01111000110010010000000000000000'
take_opcode(opd1)
take_opcode(opd2)
take_opcode(opd3)
take_opcode(opd4)
"""
