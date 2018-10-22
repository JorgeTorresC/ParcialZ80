import EnlzCarg
import sys
from ALZ80 import *

registros = {
    #Registros de Proposito General
    'A'    : '10000000' ,         #8bits -> Acumulador
    'B'    : '00000001',          #8bits
    'C'    : '00001000',          #8bits
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
    'IX'   : '00000000',          #16bits Index Register X
    'IY'   : '',          #16bits Index Register Y
    'R'    : '',          #8bits Refresh
    'I'    : ''           #8bits Interrupciones
}


dicFunciones = {
    'ADC':'ADC',
    'ADD':'add(arg1, arg2)',
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
    'DEC':'dec(arg1)',
    'DI':'DI',
    'DJNZ':'DJNZ',
    'EI':'EI',
    'EX':'ex(arg1, arg2)',
    'EXX': 'exx()',
    'HALT':'HALT',
    'IM':'IM',
    'IN':'IN',
    'INC':'inc(arg1)',
    'IND':'IND',
    'INDR':'INDR',
    'INI':'INI',
    'INIR':'INIR',
    'JP':'JP',
    'JR':'JR',
    'LD':'LD',
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


f = sys.stdin.readlines()
for line in f:
    itx = list()
    linea = line
    l=lector(linea)
    #print(l)
    if Lexema(l,itx) == -1:
        break
    #print(itx, len(itx))
    print(EnlzCarg.enlazador(dicFunciones, registros, itx))
