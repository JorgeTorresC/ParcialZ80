from Funcions import *

#Banderas <|S|Z|-|H|-|P|N|C|>
F = '00000000'
F_p = '00000000'  #8bits

registros = {
    #Registros de Proposito General
    'A'  : '11',        #8bits
    'B'  : '00',        #8bits
    'C'  : '',          #8bits
    'D'  : '',          #8bits
    'E'  : '',          #8bits
    'H'  : '',          #8bits
    'L'  : '',          #8bits
    'BC' : '',          #16bits
    'DE' : '',          #16bits
    'HL' : '',          #16bits
    'AF' : '',          #16bits
    'A_p'  : '',        #8bits
    'B_p'  : '',        #8bits
    'C_p'  : '',        #8bits
    'D_p'  : '',        #8bits
    'E_p'  : '',        #8bits
    'H_p'  : '',        #8bits
    'L_p'  : '',        #8bits
    'BC_p' : '',        #16bits
    'DE_p' : '',        #16bits
    'HL_p' : '',        #16bits
    'AF_p' : '',         #16bits
    #Registros de Proposito Especial
    'PC' : '',          #16bits Program counter
    'SP' : '',          #16bits Stack Pounter
    'IX' : '',          #16bits Index Register X
    'IY' : '',          #16bits Index Register Y
    'R'  : '',          #8bits Refresh
    'I'  : ''           #8bits Interrupciones
}


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

instr1 = '01111000'  #Solo para pruebas
instr2 = '0011100001111000'
instr3 = '00111'

#Instruccion de transferencia para 1 Byte
def ld(opA, opB):
    if len(opB) == 3:
        registros[letters[opA]] = registros[letters[opB]]
    elif len(opB) == 8 or len(opB) == 16:
        registros[opA] = opB

def inc(opA):
    varInc = registros[opA]
    if len(opA) == 8:
        aux = int(varInc,2) + int('1',2)
        varInc = Rell_Zeros(bin(aux))
        registros[apA] = varInc
    elif len(opA) == 16:
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


    # TODO: Incrementar Funcion
def dec(opA):
    varDec = registros[opA]
    if len(opA) == 8:
        aux = int(varDec,2) - int('1',2)
        varDec = Rell_Zeros(bin(aux))
        registros[apA] = varDec
    elif len(opA) == 16:
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

    # TODO: Decrementar Funcion



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
                # TODO: ADD este implica manejar los flags, nada grave.
                a=0 #solo para dejar compilar
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
            a=0 #solo para dejar compilar
        # 8-bit DEC
        if z == '101':
            a=0 #solo para dejar compilar
        # 8-bit load immediate
        if z == '110':
            ld(y, z)

        # Assorted operations on accumulator/flags
        if z == '111':
            a=0 #solo para dejar compilar
    update()

execute(instr3)
print(registros)


#El diccionario de funciones va despues de declarar las funciones
#Ejemplo de un diccionario de funciones
"""

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

dicFunciones = {
    'ADC':'ADC',
    'ADD':'ADD',
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
    'DEC':"DEC",
    'DI':'DI',
    'DJNZ':'DJNZ',
    'EI':'EI',
    'EX':'EX',
    'EXX':'EXX',
    'HALT':'HALT',
    'IM':'IM',
    'IN':'IN',
    'INC':'INC',
    'IND':'IND',
    'INDR':'INDR',
    'INI':'INI',
    'INIR':'INIR',
    'JP':'JP',
    'JR':'JR',
    'LD':ld(ld1, ld2),
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
    'POP':'POP',
    'PUSH':'PUSH',
    'RES':'RES',
    'RET':'RET',
    'RETI':'RETI',
    'RETN':'RETN',
    'RL':'RL',
    'RLA':'RLA',
    'RLC':'RLC',
    'RLCA':'RLCA',
    'RLD':'RLD',
    'RR':'RR',
    'RRA':'RRA',
    'RRC':'RRC',
    'RRCA':'RRCA',
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
