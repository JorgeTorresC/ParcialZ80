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
    # print arg
    if arg[0] == '-':
        return '1'+ arg[3:]
    elif len(arg) == 11:
        return arg[2:]
    elif len(arg)==10:
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

# Pasar de Hexademal a Binario de 8 y 16 8bits
def hexa_transform(arg):
    l = len (arg)
    aux1 = ''
    aux2 = ''
    result = ''
    if l == 5:
        aux1 = bin(int(arg[1:3], 16))
        aux2 = bin(int(arg[3:5], 16))
        result = Rell_Zeros(aux1) + Rell_Zeros(aux2)
        return result
    elif l == 3:
        aux1 = Rell_Zeros(bin(int(arg[1:3], 16)))
        result = aux1
        return result

#Toma un decimal y lo convierte en binario de 8 o 16 bits
def bin_trasnform(arg):
    aux = bin(int(arg))
    #print aux
    if len(aux) > 10:
        v1 = Rell_Zeros(aux[0:10])
        v2 = Rell_Zeros(aux[10:len(aux)])
        result = ''
        result = v1 + v2
        return result
    else:
        return Rell_Zeros(aux)

def add_registros(varA, varB):
    if len(varA) == 8 and len(varB) == 8:
        aux = int(varA,2) + int(varB,2)
        varA = Rell_Zeros(bin(aux))
        return varA
    elif len(varA) == 16 and len(varB) == 8:
        p1 = varA[0:8]
        P2 = varA[8:16]
        aux1 = int(p2,2) + int(varB,2)
        p2 = Rell_Zeros(bin(aux1))
        aux2 = int(p1,2) + int('1',2)
        p1 = Rell_Zeros(bin(aux2))
        varA = ''
        varA = p1 + p2
        return varA
    elif len(varA) == 16 and len(varB) == 16:
        p1 = varA[0:8]
        P2 = varA[8:16]
        q1 = varB[0:8]
        q2 = varB[8:16]
        aux1 = int(p2,2) + int(q2,2)
        if aux1 > 255:
            p2 = Rell_Zeros(bin(aux1))
            aux2 = int(p1,2) + int('1',2)
            aux2 = aux2 + int(q1,2)
            p1 = Rell_Zeros(bin(aux2))
        else:
            p2 = Rell_Zeros(bin(aux1))
            aux2 = aux2 + int(q1,2)
            p1 = Rell_Zeros(bin(aux2))
        varA = ''
        varA = p1 + p2
        return varA

def res_registros(var1, var2):
    aux = hex(int(varA,2) - int(varB,2))
    #aux2 = hexa_transform(aux[2:len(aux)])
    l=len(aux)
    if l == 3 or l == 4:
        aux2 = hexa_transform(aux[2:l])
        return Rell_Zeros(aux2)
    elif l == 5 or l == 6:
        p1 = Rell_Zeros(hexa_transform(aux[2:4]))
        p2 = Rell_Zeros(hexa_transform(aux[4:l]))
        return p1 + p2
