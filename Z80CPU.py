# -*- coding: utf-8 -*-
# *************************
# 21 De Octubre del 2018
# Emulador Procesador Z80
# Jorge Ivan Torres
# Daniel Caita
# *************************
add
from Funcions import *

registros = {
    #Registros de Proposito General
    'A'    : '' ,         #8bits -> Acumulador
    'B'    : '',          #8bits
    'C'    : '',          #8bits
    'D'    : '',          #8bits
    'E'    : '',          #8bits
    'H'    : '',          #8bits
    'L'    : '',          #8bits
    'BC'   : '',          #16bits
    'DE'   : '',          #16bits
    'HL'   : '',          #16bits
    'AF'   : '',          #16bits
    'A_p'  : '',          #8bits
    'B_p'  : '',          #8bits
    'C_p'  : '',          #8bits
    'D_p'  : '',          #8bits
    'E_p'  : '',          #8bits
    'H_p'  : '',          #8bits
    'L_p'  : '',          #8bits
    'BC_p' : '',          #16bits
    'DE_p' : '',          #16bits
    'HL_p' : '',          #16bits
    'AF_p' : '',          #16bits
    #Registros de Proposito Especial
    'PC'   : '',          #16bits Program counter
    'SP'   : '',          #16bits Stack Pounter
    'IX'   : '',          #16bits Index Register X
    'IY'   : '',          #16bits Index Register Y
    'R'    : '',          #8bits Refresh
    'I'    : ''           #8bits Interrupciones
}

#Banderas <|S|Z|-|H|-|P|N|C|>
F = '00000000'
F_p = '00000000'  #8bits

memory = {'0':'00000000'}

letters = {
    '111' : 'A',
    '000' : 'B',
    '001' : 'C',
    '010' : 'D',
    '011' : 'E',
    '100' : 'H',
    '101' : 'L',
    '110' : '(HL)'
}

def ld(opA, opB):
    if len(opB) == 3:
        registros[letters[opA]] = registros[letters[opB]]
    elif len(opB) == 8 or len(opB) == 16:
        registros[opA] = opB

def inc(opA):
    varInc = registros[opA]
    if len(varInc) == 8:
        aux = int(varInc,2) + int('1',2)
        varInc = Rell_Zeros(bin(aux))
        registros[apA] = varInc
    elif len(varInc) == 16:
        p1 = varInc[0:8]
        P2 = varInc[8:16]
        if p2 == '11111111':
            p2 = '00000000'
            aux = int(p1,2) + int('1',2)
            p1 = Rell_Zeros(bin(aux))
        else:
            aux = int(p2,2) + int('1',2)
            p2 = Rell_Zeros(bin(aux))
        varInc = ''
        varInc = p1 + p2
        registros[apA] = varInc
    #F[6]='0'
    #F[5]='1'

def dec(opA):
    varDec = registros[opA]
    if len(varDec) == 8:
        aux = int(varDec,2) - int('1',2)
        varDec = Rell_Zeros(bin(aux))
        registros[apA] = varDec
    elif len(varDec) == 16:
        p1 = varDec[0:8]
        P2 = varDec[8:16]
        if p2 == '00000000':
            p2 = '11111111'
            aux = int(p1,2) - int('1',2)
            p1 = Rell_Zeros(bin(aux))
        else:
            aux = int(p2,2) - int('1',2)
            p2 = Rell_Zeros(bin(aux))
        varDec = ''
        varDec = p1 + p2
        registros[apA] = varDec
    #F[6]='0'
    #F[5]='1'

def ex(opA, opB):
    aux = registros[opA]
    registros[opA] = registros[opB]
    registros[opB] = aux
    #flags
    update()

def exx():
    ex('BC', 'BC_p')
    ex('DE', 'DE_p')
    ex('HL', 'HL_p')

# Para que la instruccion sea interpretada como
# una operacion de la ALU, los bits de la instruccion
# deben estar de la forma [0,0,X,X,X,0,0,1]
# donde los bits 2, 3 y 4 son la operacion a realizar.

# Los bits 2, 3 y 4 que corresponden al grupo 'y' de la configuracion
# y son los que se le pasan en el primer parametro.

# Es importante tener en cuenta que esta función
# es la que hace uso de los Flags, segun la operacion que
# este realizando.

# Los operandos de la ALU son el registro 'A', que es el Acumulador
# y el byte que se le pase en el segundo parametro.

#NOTA: Dado que el resultado de la operacion de la ALU se guarda
#      en el registro 'A' el segundo parametro debe ser de 8 Bits.
#      En dado caso de que el resultado tenga un bit de mas se guarda en
#      la bandera Carry.


# registros['A'] = operando1
# arg1 = operador
# arg2 = operando2

def ALU(arg1, arg2):
    op1 = registros['A']
    op2 = arg2

    #Flags
    # F[0] = S
    # F[1] = Z
    # F[3] = H
    # F[5] = P
    # F[6] = N
    # F[7] = C

    if arg1 == '000': #ADD A,
        aux = int(op1, 2) + int(op2, 2)
        F[1] = '1' if aux == '00000000' else '0'
        F[0] = '1' if aux[0] == '1' else '0'
        F[6] = '0'

        if len(aux) > 8:
            F[7] = '1'
            F[5] = '1'
            registros['A'] = aux[1:8]
        else:
            F[7] = '0'
            F[5] = '0'
            registros['A'] = aux

    if arg1 == '001': #ADC A,
        a=0 #solo para dejar compilar

    if arg1 == '010': #SUB
        a=0 #solo para dejar compilar

    if arg1 == '011': #SBC A,
        a=0 #solo para dejar compilar

    if arg1 == '100': #AND
        a=0 #solo para dejar compilar

    if arg1 == '101': #XOR
        a=0 #solo para dejar compilar

    if arg1 == '011': #OR
        a=0 #solo para dejar compilar

    if arg1 == '111': #CP
        a=0 #solo para dejar compilar



def add(opA, opB):
    varA = registros[opA]
    varB = registros[opB]
    if len(varA) == 8 and len(varB) == 8:
        aux = int(varA,2) + int(varB,2)
        varA = Rell_Zeros(bin(aux))
        registros[apA] = varA
    elif len(varA) == 16 len(varB) == 8:
        p1 = varA[0:8]
        P2 = varA[8:16]
        aux1 = int(p2,2) + int(varB,2)
        p2 = Rell_Zeros(bin(aux1))
        aux2 = int(p1,2) + int('1',2)
        p1 = Rell_Zeros(bin(aux2))
        varA = ''
        varA = p1 + p2
        registros[apA] = varA
    elif len(varA) == 16 len(varB) == 16:
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
        registros[apA] = varA
        #hacer update para apA de 16 bits

def rlca():
    aux = registros[A]
    corr = aux[1:8] + aux[0]
    registros[A] = corr
    #aux[1] = F[7]

def rrca():
    aux = registros[A]
    corr = aux[7] + aux[0:7]
    registros[A] = aux
    #aux[1] = F[7]

def rla():
    global F
    aux = registros[A]
    corr = aux[1:8] + F[7]
    F[7] = aux[0]
    registros[A] = corr

def pop(arg):
    ld(arg, 'SP')

def push(arg):
    ld('SP', arg)
#------------------------------------
#------------------------------------
def update():
    registros['BC'] = registros['B'] + registros['C']
    registros['DE'] = registros['D'] + registros['E']
    registros['HL'] = registros['H'] + registros['L']
    registros['AF'] = registros['A'] + F

    registros['BC_p'] = registros['B_p'] + registros['C_p']
    registros['DE_p'] = registros['D_p'] + registros['E_p']
    registros['HL_p'] = registros['H_p'] + registros['L_p']
    registros['AF_p'] = registros['A_p'] + F_p

def execute(instr):
    x = instr[0:2]  #Opcode
    y = instr[2:5]
    z = instr[5:8]
    p = instr[2:4]
    q = instr[4]

    if len(instr) >= 16:
        byte2 = instr[8:16]
        if len(instr) == 24:
            byte3 = instr[16:24]

    if x == '00':
        # Relative jumps and assorted ops
        if z == '000':
            if y == '000':
                print('No Operation for this instruction.')
            if y == '001':
                update()
                registros['AF'] , registros['AF_p'] = registros['AF_p'] , registros['AF']
            # TODO: Y=2, y=3, y = 4..7

        # 16-bit load immediate/add
        if z == '001':
            if q == '0':
                ld(letters[y], byte2)
            if q == '1':
                if p == '00':
                    add('HL', 'BC')
                if p == '01':
                    add('HL', 'DE')
                if p == '10':
                    add('HL', 'HL')
                if p == '11':
                    add('HL', 'SP')

        # Indirect loading
        if z == '010':
            if q == '0':
                if p == '00':
                    memory['BC'] = registros['A']
                if p == '01':
                    memory['DE'] = registros['A']
                if p == '10':
                    memory[byte3+byte2] = registros['HL']
                if p == '11':
                    memory[byte3+byte2] = registros['A']
            if q == '1':
                if p == '00':
                    registros['A'] = memory['BC']
                if p == '01':
                    registros['A'] = memory['DE']
                if p == '10':
                    registros['HL'] = memory[byte3+byte2]
                if p == '11':
                    registros['A'] = memory[byte3+byte2]

        # 16-bit INC/DEC
        if z == '011':
            if q == '0':
                inc(instr)
            if q == '1':
                dec(instr)

        # 8-bit INC
        if z == '100':
            inc(y)
        # 8-bit DEC
        if z == '101':
            dec(y)
        # 8-bit load immediate
        if z == '110':
            ld(y, z)

        # Assorted operations on accumulator/flags
        if z == '111':
            if y == '000':
                rlca()
            if y == '001':
                rrca()
            if y == '010':
                rla()
            # TODO: y=3..7

    if x == '01':
        ld(y,z)

    if x == '10':
        ALU(y, registros[ letters[z] ])

    if x == '11':
        if z == '000':
            ALU(y, registros[ letters[z] ])

        if z == '001':
            if q == '0':
                if p == '00':
                    pop('BC')
                if p == '01':
                    pop('DE')
                if p == '10':
                    pop('HL')
                if p == '11':
                    pop('AF')
            if q == '1':
                if p == '00':
                    a=0 #solo para dejar compilar
                if p == '01':
                    exx()
                if p == '10':
                    a=0 #solo para dejar compilar
                if p == '11':
                    ld('SP', HL)

        if z == '010':
            a=0 #solo para dejar compilar

        if z == '011':
            if y == '100':
                ex('DE', 'HL')

        if z == '100':
            a=0 #solo para dejar compilar

        if z == '101':
            if q == '0':
                if p == '00':
                    push('BC')
                if p == '01':
                    push('DE')
                if p == '10':
                    push('HL')
                if p == '11':
                    push('AF')

        if z == '110':
            ALU(y, byte2)

        if z == '111':
            a=0 #solo para dejar compilar

    update()

instr1 = '01111000'  #Solo para pruebas
instr2 = '0011100001111000'
instr3 = '00111'

execute(instr3)
print(registros)


#El diccionario de funciones va despues de declarar las funciones
#Ejemplo de un diccionario de funciones
"""
                # TODO: ADD este implica manejar los flags, nada grave.
                a=0 #solo para dejar compilar

def suma(a,b):
    return a+b
def resta(arg):
    return arg-1

var1=int(input('ingrese un numero'))
var2=3
arg=6
dic={'1':suma(var1,var2),'2':resta(arg)}
print('diccionario de funciones', dic['1'])

"""
#variables para pasar a las funciones
arg1,arg2 = '',''

dicFunciones = {
    'ADC':'ADC',
    'ADD':add(arg1, arg2),
    'AND':'AND',
    'BIT':'BIT',
    'CALL':'CALL',
    'CCF':'CCF',
    'CP':'CP',
    'CPD':'CPD',
    'CPDR':'CDPR',
    'CPI':'CPI',
    'CPIR':'CIR',
    'CPL':'CPL',
    'DAA':'DAA',
    'DEC':dec(arg1),
    'DI':'DI',
    'DJNZ':'DJNZ',
    'EI':'EI',
    'EX':ex(arg1, arg2),
    'EXX': exx(),
    'HALT':'HALT',
    'IM':'IM',
    'IN':'IN',
    'INC':inc(arg1),
    'IND':'IND',
    'INDR':'INDR',
    'INI':'INI',
    'INIR':'INIR',
    'JP':'JP',
    'JR':'JR',
    'LD':ld(arg1, arg2),
    'LDD':'LDD',
    'LDDR':'LDDR',
    'LDI':'LDI',
    'LDIR':'LDIR',
    'NEG':'NEG',
    'NOP':'NOP',
    'OR':'OR',
    'OTDR':'OTDR',
    'OUT':'OUT',
    'OUTD':'OUTD',
    'OUTI':'OUTI',
    'POP': pop(arg1),
    'PUSH': push(arg1),
    'RES':'RES',
    'RET':'RET',
    'RETI':'RETI',
    'RETN':'RETN',
    'RL':'RL',
    'RLA':rla(),
    'RLC':'RLC',
    'RLCA':rlca(),
    'RLD':'RLD',
    'RR':'RR',
    'RRA':'RRA',
    'RRC':'RRC',
    'RRCA':rrca(),
    'RRD':'RRD',
    'RST':'RST',
    'SBC':'SBC',
    'SCF':'SCF',
    'SET':'SET',
    'SLA':'SLA',
    'SRA':'SRA',
    'SLR':'SLR',
    'SUB':'SUB',
    'XOR':'XOR'
}
