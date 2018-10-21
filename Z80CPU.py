from Funcions import *

#Registros de Proposito General
registros = {
    'A'  : '',          #8bits
    'B'  : '',          #8bits
    'C'  : '',          #8bits
    'D'  : '',          #8bits
    'E'  : '',          #8bits
    'H'  : '',          #8bits
    'L'  : '',          #8bits
    'BC' : B + C ,     #16bits
    'DE' : D + E ,     #16bits
    'HL' : H + L ,     #16bits
    'AF' : A + '',     #16bits
    'A_p'  : '',        #8bits
    'B_p'  : '',        #8bits
    'C_p'  : '',        #8bits
    'D_p'  : '',        #8bits
    'E_p'  : '',        #8bits
    'H_p'  : '',        #8bits
    'L_p'  : '',        #8bits
    'BC_p' : '',       #16bits
    'DE_p' : '',       #16bits
    'HL_p' : '',       #16bits
    'AF_p' : ''        #16bits
}

#Registros de Proposito Especial
reg_especial = {
    'PC' : ''         #16bits Program counter
    'SP' : ''         #16bits Stack Pounter
    'IX' : ''         #16bits Index Register X
    'IY' : ''         #16bits Index Register Y
    'R'  : ''          #8bits Refresh
    'I'  : ''          #8bits Interrupciones
}

memoria = {'0':'00000000'}

dic1Byte = {
    '111' : 'A',
    '000' : 'B',
    '001' : 'C',
    '010' : 'D',
    '011' : 'E',
    '100' : 'H',
    '101' : 'L'
}

instr = '01111000'  #Solo para pruebas
#Instruccion de transferencia para 1 Byte

def ld(opA, opB):
    registros[opA] = registros[opB]

def execute(instr):
    if len(instr) == 8:
        x = instr[0:2]  #Opcode
        y = instr[2:5]
        z = instr[5:8]
    if x == '01':
        ld(dic1Byte[y], dic1Byte[z])
