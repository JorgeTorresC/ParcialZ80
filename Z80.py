# -*- coding: utf-8 -*-
# *************************
# 11 De Octubre del 2018
# Emulador Procesador Z80
# Jorge Ivan Torres
# Daniel Caita
# *************************

from Funcions import *
#Definición de Registros
#-----------------------------------

#Banderas <|S|Z|-|H|-|P|N|C|>
F = ['0','0','0','0','0','0','0']
F_p = ['0','0','0','0','0','0','0']
#F = '00000000'  #8bits

#Primer banco
A = '10101100'          #8bits
B = ''          #8bits
C = ''          #8bits
D = ''          #8bits
E = ''          #8bits
H = ''          #8bits
L = ''          #8bits
BC = B + C      #16bits
DE = D + E      #16bits
HL = H + L      #16bits
AF = A + ''     #16bits


#Segundo banco
A_p = ''        #8bits
B_p = ''        #8bits
C_p = ''        #8bits
D_p = ''        #8bits
E_p = ''        #8bits
H_p = ''        #8bits
L_p = ''        #8bits
BC_p = ''       #16bits
DE_p = ''       #16bits
HL_p = ''       #16bits
AF_p = ''       #16bits

#Registros de Proposito Especial
PC = ''         #16bits Program counter
SP = ''         #16bits Stack Pounter
IX = ''         #16bits Index Register X
IY = ''         #16bits Index Register Y
R = ''          #8bits Refresh
I = ''          #8bits Interrupciones

#-----------------------------------

#Definicion de memoria

memoria = {'0':'00000000'}

#Funciones
#-----------------------------------

#opcodes

#LD
def LD_01 (arg):
    global BC
    global B
    global C
    if len(arg) == 16:
        B = arg[0:8]
        C = arg[8:16]
        BC = B + C
    else:
        print('opcode 01 erroneo ')

#LD
def LD_02 ():
    global A
    memoria[BC] = A

#INC
def INC_03 ():
    global BC
    global B
    global C
    if C=='11111111':
        C = '00000000'
        aux = int(B,2) + int('1',2)
        B = Rell_Zeros(bin(aux))
    else:
        aux = int(C,2) + int('1',2)
        C = Rell_Zeros(bin(aux))
    BC = B + C

#INC
def INC_04 ():
    global B
    global F
    aux = int(B,2) + int('1',2)
    B = Rell_Zeros(bin(aux))
    F[6]='0'
    F[5]='1'#Overflow

#DEC
def DEC_05():
    global B
    global F
    aux = int(B,2) - int('1',2)
    B = Rell_Zeros(bin(aux))
    F[6]='1'
    F[5]='1'#Overflow

#LD
def LD_06 (arg):
    global B
    if len(arg)==8:
        B = arg
    else:
        print('opcode 06 erroneo ')

#RLCA posible corrimiento
def RLCA_07():
    global A
    aux = A[1:8] + A[0]
    A = aux
    A[1] = F[7]
    #Falta reset N y H

#EX
def EX_08():
    global A
    global F
    global AF
    global AF_p
    auxA = A
    auxF1 = ''
    auxF_p1 = ''
    for i in range (len(F)):
        auxF1 = auxF1 + str(F[i])
        auxF_p1 = auxF_p1 + str(F_p[i])
    auxFL = F
    auxAF = AF
    A = A_p
    F = F_p
    A_p = auxA
    F_p = auxFL
    AF = A + auxF1
    AF_p = A + auxF_p1

#ADD
def ADD_09():
    global HL
    global H
    global L
    global B
    global C
    aux = int(L,2) + int(C,2)
    if aux >= 255:
        aux2 = int(H,2) + int('1',2)
        aux3 = Rell_Zeros(bin(aux2))
        aux2 = int(aux3,2) + int(B,2)
        L = '00000000'
        H = Rell_Zeros(bin(aux2))
    else:
        L =  Rell_Zeros(bin(aux))
    HL = H + L

#LD
def LD_0A():
    global A
    A = memoria[BC]
     #Sin probar

#DEC
def DEC_0B():
    global B
    global C
    global BC
    if C == '00000000':
        C = '11111111'
        aux = int(B,2) - int('1',2)
        B = Rell_Zeros(bin(aux))
    else:
        aux = int(C,2) - int('1',2)
        C = Rell_Zeros(bin(aux))
    BC = B + C

#INC
def INC_0C ():
    global C
    aux = int(C,2) + int('1',2)
    C = Rell_Zeros(bin(aux))

#DEC
def DEC_0D():
    global C
    aux = int(C,2) - int('1',2)
    C = Rell_Zeros(bin(aux))

#LD
def LD_0E (arg):
    global C
    if len(arg)==8:
        C = arg
    else:
        print('opcode 0E erroneo ')

#RRCA Posible corrimiento
def RRCA_0F():
    global A
    global F
    aux = A[7] + A[0:7]
    A = aux
    A[1] = F[7]

#DJNZ
#---------------------NO lo entendí

def LD_11(arg):
    global DE
    global D
    global E
    if len(arg) == 16:
        D = arg[0:8]
        E = arg[8:16]
        DE = D + E
    else:
        print('opcode 11 erroneo ')

#LD
def LD_12 ():
    global A
    memoria[DC] = A

#INC
def INC_13():
    global DE
    global D
    global E
    if E == '11111111':
        E = '00000000'
        aux = int(D,2) + int('1',2)
        D = Rell_Zeros(bin(aux))
    else:
        aux = int(E,2) + int('1',2)
        E = Rell_Zeros(bin(aux))
    DE = D + E

#INC
def INC_14():
    global D
    global F
    aux = int(D,2) + int('1',2)
    D = Rell_Zeros(bin(aux))
    F[6]='0'
    F[5]='1'

#DEC
def DEC_15():
    global D
    global F
    aux = int(D,2) - int('1',2)
    D = Rell_Zeros(bin(aux))
    F[6]='1'
    F[5]='1'#Overflow

#LD
def LD_16(arg):
    global D
    if len(arg)==8:
        D = arg
    else:
        print('opcode 16 erroneo ')

#RLA Posible corrimiento
def RLA_17():
    global A
    global F
    aux2=F[7]
    aux = A[1:8] + aux2
    A = aux
    A[1] = F[7]

#JR
def JR_18(arg):
    global PC
    aux = arg[0]
    aux2 = int(PC,2) + int(aux,2)
    PC = Rell_Zeros(bin(aux2))

#ADD
def ADD_19():
    global HL
    global H
    global L
    global D
    global E
    aux = int(L,2) + int(E,2)
    if aux >= 255:
        aux2 = int(H,2) + int('1',2)
        aux3 = Rell_Zeros(bin(aux2))
        aux2 = int(aux3,2) + int(D,2)
        L = '00000000'
        H = Rell_Zeros(bin(aux2))
    else:
        L =  Rell_Zeros(bin(aux))
    HL = H + L

#LD
def LD_1A():
    global A
    A = memoria[DE]

#DEC
def DEC_1B():
    global D
    global E
    global DE
    if E == '00000000':
        E = '11111111'
        aux = int(D,2) - int('1',2)
        D = Rell_Zeros(bin(aux))
    else:
        aux = int(E,2) - int('1',2)
        E = Rell_Zeros(bin(aux))
    DE = D + E

#INC
def INC_1C():
    global E
    aux = int(E,2) + int('1',2)
    E = Rell_Zeros(bin(aux))

#DEC
def DEC_1D():
    global E
    aux = int(E,2) - int('1',2)
    E = Rell_Zeros(bin(aux))

#LD
def LD_1E():
    global E
    if len(arg)==8:
        E = arg
    else:
        print('opcode 1E erroneo ')

#RRA -REvisar posible corrimiento...
def RRA_1F():
    global A
    global F
    auxf=F[7]
    aux = A[7] + A[0:7]
    A = aux
    A[1] = F[7]

#JR
#def JR_20(arg): No lo entendí

#LD
def LD_21(arg):
    global HL
    global H
    global L
    if len(arg) == 16:
        H = arg[0:8]
        L = arg[8:16]
        HL = H + L
    else:
        print('opcode 21 erroneo ')

#LD
def LD_22(arg):
    global HL
    memoria[arg] = HL

#INC
def INC_23():
    global HL
    global H
    global L
    if L == '11111111':
        L = '00000000'
        aux = int(H,2) + int('1',2)
        H = Rell_Zeros(bin(aux))
    else:
        aux = int(L,2) + int('1',2)
        L = Rell_Zeros(bin(aux))
    HL = H + L

#INC
def INC_24():
    global H
    global F
    aux = int(H,2) + int('1',2)
    H = Rell_Zeros(bin(aux))
    F[6]='0'
    F[5]='1'

#DEC
def DEC_25():
    global H
    global F
    aux = int(H,2) - int('1',2)
    H = Rell_Zeros(bin(aux))
    F[6]='1'
    F[5]='1'#Overflow

#LD
def LD_26():
    global H
    if len(arg)==8:
        H = arg
    else:
        print('opcode 26 erroneo ')

#DAA
# def DAA_27(): ---- No la

#JR
#def JR_28():

#ADD
def ADD_29():
    global HL
    global H
    global L
    auxa = H
    auxb = L
    aux = int(L,2) + int(auxb,2)
    if aux >= 255:
        aux2 = int(H,2) + int('1',2)
        aux3 = Rell_Zeros(bin(aux2))
        aux2 = int(aux3,2) + int(auxa,2)
        L = '00000000'
        H = Rell_Zeros(bin(aux2))
    else:
        L =  Rell_Zeros(bin(aux))
    HL = H + L

#LD
def LD_2A(arg):
    global H
    global L
    global HL
    aux = memoria[arg]
    H = aux[0:8]
    L = aux[8:16]
    HL = H + L

#DEC
def DEC_2B():
    global H
    global L
    global HL
    if L == '00000000':
        L = '11111111'
        aux = int(H,2) - int('1',2)
        H = Rell_Zeros(bin(aux))
    else:
        aux = int(L,2) - int('1',2)
        L = Rell_Zeros(bin(aux))
    HL = H + L

#INC
def INC_2C():
    global L
    aux = int(L,2) + int('1',2)
    L = Rell_Zeros(bin(aux))

#DEC
def DEC_2D():
    global L
    aux = int(L,2) - int('1',2)
    L = Rell_Zeros(bin(aux))

#LD
def LD_2E(arg):
    global L
    if len(arg)==8:
        L = arg
    else:
        print('opcode 2E erroneo ')

#CPL
def CPL_2F():
    global A
    aux = ''
    for i in  A :
        if i == '1':
            aux += '0'
        else:
            aux += '1'
    A = aux

#JR
#-----------------No lo entiendo

#LD
def LD_31(arg):
    global SP
    if len(arg) == 16:
        SP = arg
    else:
        print('opcode 31 erroneo ')

#LD
def LD_32(arg):
    global A
    memoria[arg] = A

#INC
def INC_33():
    global SP
    aux = int(SP,2) + int('1',2)
    SP = Rell_Zeros(bin(aux))

#INC
def INC_34():
    global HL
    global H
    global L
    global F
    if L == '11111111':
        L = '00000000'
        aux = int(H,2) + int('1',2)
        H = Rell_Zeros(bin(aux))
    else:
        aux = int(L,2) + int('1',2)
        L = Rell_Zeros(bin(aux))
    HL = H + L
    F[5]='1'

#DEC
def DEC_35():
    global H
    global L
    global HL
    if L == '00000000':
        L = '11111111'
        aux = int(H,2) - int('1',2)
        H = Rell_Zeros(bin(aux))
    else:
        aux = int(L,2) - int('1',2)
        L = Rell_Zeros(bin(aux))
    HL = H + L
    F[6]='1'

#LD
def LD_36(arg):
    global HL
    global H
    global L
    if len(arg) == 8:
        H = '00000000'
        L = arg
        HL = H + L
    else:
        print('opcode 36 erroneo ')

#SCF
def SCF_37():
    global F
    F[6] = '0'
    F[3] = '0'
    return F[7]

#JR
# condicion CC = True .... Sin entender

#ADD
def ADD_39():
    global HL
    global H
    global L
    global SP
    aux = int(L,2) + int(SP[8:16],2)
    if aux >= 255:
        aux2 = int(H,2) + int('1',2)
        aux3 = Rell_Zeros(bin(aux2))
        aux2 = int(aux3,2) + int(SP[0:8],2)
        L = '00000000'
        H = Rell_Zeros(bin(aux2))
    else:
        L =  Rell_Zeros(bin(aux))
    HL = H + L

#LD
def LD_3A(arg):
    global A
    A = memoria[arg]

#DEC
def DEC_3B():
    global SP
    auxp = SP[8:16]
    auxs = SP[0:8]
    if auxp == '00000000':
        auxp = '11111111'
        aux = int(auxs,2) - int('1',2)
        auxs = Rell_Zeros(bin(aux))
    else:
        aux = int(auxp,2) - int('1',2)
        auxp = Rell_Zeros(bin(aux))
    SP = auxs + auxp

#INC
def INC_3C():
    global A
    aux = int(A,2) + int('1',2)
    A = Rell_Zeros(bin(aux))

#DEC
def DEC_3D():
    global A
    aux = int(A,2) - int('1',2)
    A = Rell_Zeros(bin(aux))

#LD
def LD_3E(arg):
    global A
    if len(arg)==8:
        A = arg
    else:
        print('opcode 3E erroneo ')

#CCF
def CCF_3F():
    global F
    F[6] = '0'
    if F[7] == '0':
        F[7] == '1'
    else:
        F[7] == '0'

#LD 40 ES MUY TONTA--------------------
#LD
def LD_41():
    global B
    global C
    B = C

#LD
def LD_42():
    global B
    global D
    B = D

#LD
def LD_43():
    global B
    global E
    B = E

#LD
def LD_44():
    global B
    global H
    B = H

#LD
def LD_45():
    global B
    global L
    B = L

#LD
def LD_46():
    global B
    global H
    if len(arg) == 8:
        B = H
    else:
        print('opcode 46 erroneo ')

#LD
def LD_47():
    global B
    global A
    B = A

#LD
def LD_48():
    global B
    global C
    C = B

#Opcode 49 muy tonto

#LD
def LD_4A():
    global D
    global C
    C = D

#LD
def LD_4B():
    global E
    global C
    C = E

#LD
def LD_4C():
    global H
    global C
    C = H

#LD
def LD_4D():
    global L
    global C
    C = L

#LD
def LD_4E():
    global B
    global H
    if len(arg) == 8:
        B = H
    else:
        print('opcode 46 erroneo ')

#LD
def LD_4F():
    global L
    global A
    C = A

#LD
def LD_50():
    global B
    global D
    D = B

#LD
def LD_51():
    global C
    global D
    D = C

#-----Muy tonto Opcode 52
#LD
def LD_53():
    global E
    global D
    D = E

#LD
def LD_54():
    global H
    global D
    D = H

#LD
def LD_55():
    global L
    global D
    D = L

#LD
def LD_56():
    global D
    global H
    if len(arg) == 8:
        D = H
    else:
        print('opcode 56 erroneo ')

#LD
def LD_57():
    global A
    global D
    D = A

#LD
def LD_58():
    global B
    global E
    E = B

#LD
def LD_59():
    global C
    global E
    E = C

#LD
def LD_5A():
    global D
    global E
    E = D

#Opcode 5B es muy tonto---------------
#LD
def LD_5C():
    global H
    global E
    E = H

#LD
def LD_5D():
    global L
    global E
    E = L

#LD
def LD_5E():
    global E
    global H
    if len(arg) == 8:
        E = H
    else:
        print('opcode 56 erroneo ')

#LD
def LD_5F():
    global A
    global E
    E = A

#LD
def LD_60():
    global B
    global H
    H = B

#LD
def LD_61():
    global C
    global H
    H = C

#LD
def LD_62():
    global D
    global H
    H = D

#LD
def LD_63():
    global E
    global H
    H = E

#opcode 65 no es necesario...
#LD
def LD_65():
    global L
    global H
    H = L

#LD
def LD_66():
    global H
    global HL
    if len(arg) == 16:
        H = HL[8:16]
    else:
        print('opcode 66 erroneo ')

#LD
def LD_67():
    global A
    global H
    H = A

#LD
def LD_68():
    global B
    global L
    L = B

#LD
def LD_69():
    global C
    global L
    L = C

#LD
def LD_6A():
    global D
    global L
    L = D

#LD
def LD_6B():
    global E
    global L
    L = E

#LD
def LD_6C():
    global H
    global L
    L = H

#OPcode 6D innecesario
#LD
def LD_6E():
    global L
    global HL
    if len(arg) == 16:
        L = HL[8:16]
    else:
        print('opcode 6E erroneo ')

#LD
def LD_6F():
    global A
    global L
    L = A

#LD
def LD_70():
    global HL
    global H
    global L
    global B
    H = '00000000'
    L = B
    HL = H + L

#LD
def LD_71():
    global HL
    global H
    global L
    global C
    H = '00000000'
    L = C
    HL = H + L

#LD
def LD_72():
    global HL
    global H
    global L
    global D
    H = '00000000'
    L = D
    HL = H + L

#LD
def LD_73():
    global HL
    global H
    global L
    global E
    H = '00000000'
    L = E
    HL = H + L

#LD
def LD_74():
    global HL
    global L
    H = '00000000'
    HL = H + L

#LD
def LD_75():
    global HL
    global H
    global L
    H = '00000000'
    L = L
    HL = H + L

#-----------Halt 76
#LD
def LD_77():
    global HL
    global H
    global L
    global A
    H = '00000000'
    L = A
    HL = H + L

#LD
def LD_78():
    global A
    global B
    A = B

#LD
def LD_79():
    global A
    global C
    A = C

#LD
def LD_7A():
    global A
    global D
    A = D

#LD
def LD_7B():
    global A
    global E
    A = E

#LD
def LD_7C():
    global A
    global H
    A = H

#LD
def LD_7D():
    global A
    global L
    A = L

#LD
def LD_7E():
    global A
    global HL
    if len(arg) == 16:
        A = HL[8:16]
    else:
        print('opcode 6E erroneo ')

#Opcode 7F es cargar A en A

#ADD
def ADD_80():
    global A
    global B
    aux = int(A,2) + int(B,2)
    A = Rell_Zeros(bin(aux))

#ADD
def ADD_81():
    global A
    global C
    aux = int(A,2) + int(C,2)
    A = Rell_Zeros(bin(aux))

#ADD
def ADD_82():
    global A
    global D
    aux = int(A,2) + int(D,2)
    A = Rell_Zeros(bin(aux))

#ADD
def ADD_83():
    global A
    global E
    aux = int(A,2) + int(E,2)
    A = Rell_Zeros(bin(aux))

#ADD
def ADD_84():
    global A
    global H
    aux = int(A,2) + int(H,2)
    A = Rell_Zeros(bin(aux))

#ADD
def ADD_85():
    global A
    global L
    aux = int(A,2) + int(L,2)
    A = Rell_Zeros(bin(aux))

#ADD
def ADD_86():
    global A
    global HL
    aux = int(A,2) + int(HL[8:16],2)
    A = Rell_Zeros(bin(aux))

#ADD
def ADD_87():
    global A
    aux1 = A
    aux = int(A,2) + int(aux1,2)
    A = Rell_Zeros(bin(aux))

#ADC
#Faltan todos los de ADC

#SUB
def SUB_09():
    global A
    global B
    aux = int(A,2) - int(B,2)
    A = Rell_Zeros(bin(aux))

#SUB
def SUB_91():
    global A
    global C
    aux = int(A,2) - int(C,2)
    A = Rell_Zeros(bin(aux))

#SUB
def SUB_92():
    global A
    global D
    aux = int(A,2) - int(D,2)
    A = Rell_Zeros(bin(aux))

#SUB
def SUB_93():
    global A
    global E
    aux = int(A,2) - int(E,2)
    A = Rell_Zeros(bin(aux))

#SUB
def SUB_94():
    global A
    global H
    aux = int(A,2) - int(H,2)
    A = Rell_Zeros(bin(aux))

#SUB
def SUB_95():
    global A
    global L
    aux = int(A,2) - int(L,2)
    A = Rell_Zeros(bin(aux))

#SUB
def SUB_96():
    global A
    global HL
    aux = int(A,2) - int(HL[8:16],2)
    A = Rell_Zeros(bin(aux))

#SUB
def SUB_97():
    global A
    A = '00000000'

#SBC
#Faltan todos los de SBC

#AND
def AND_A0():
    global A
    global B
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and B[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#AND
def AND_A1():
    global A
    global C
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and C[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#AND
def AND_A2():
    global A
    global D
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and D[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#AND
def AND_A3():
    global A
    global E
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and E[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#AND
def AND_A4():
    global A
    global H
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and H[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#AND
def AND_A5():
    global A
    global L
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and L[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#AND
def AND_A6():
    global A
    global HL
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and HL[i+8] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#Opcode A7 es and entre A con A

#XOR
def XOR_A8():
    global A
    global B
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and B[i] == '0':
            aux += '1'
        elif A[i] == '0' and B[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#XOR
def XOR_A9():
    global A
    global C
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and C[i] == '0':
            aux += '1'
        elif A[i] == '0' and C[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#XOR
def XOR_AA():
    global A
    global D
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and D[i] == '0':
            aux += '1'
        elif A[i] == '0' and D[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#XOR
def XOR_AB():
    global A
    global E
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and E[i] == '0':
            aux += '1'
        elif A[i] == '0' and E[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#XOR
def XOR_AC():
    global A
    global H
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and H[i] == '0':
            aux += '1'
        elif A[i] == '0' and H[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#XOR
def XOR_AD():
    global A
    global L
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and L[i] == '0':
            aux += '1'
        elif A[i] == '0' and L[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#XOR
def XOR_AE():
    global A
    global HL
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and HL[i+8] == '0':
            aux += '1'
        elif A[i] == '0' and HL[i+8] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#XOR
def XOR_AF():
    global A
    A = '00000000'

#OR
def OR_B0():
    global A
    global B
    aux = ''
    for i in range(len(A))
        if A[i] == '1' or B[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux


#OR
def OR_B1():
    global A
    global C
    aux = ''
    for i in range(len(A))
        if A[i] == '1' or C[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#OR
def OR_B2():
    global A
    global D
    aux = ''
    for i in range(len(A))
        if A[i] == '1' or D[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#OR
def OR_B3():
    global A
    global E
    aux = ''
    for i in range(len(A))
        if A[i] == '1' or E[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#OR
def OR_B4():
    global A
    global H
    aux = ''
    for i in range(len(A))
        if A[i] == '1' or H[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#OR
def OR_B5():
    global A
    global L
    aux = ''
    for i in range(len(A))
        if A[i] == '1' or L[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#OR
def OR_B6():
    global A
    global HL
    aux = ''
    for i in range(len(A))
        if A[i] == '1' or HL[i+8] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

#Opcode B7 es OR entre A y A

#Opcodes CP basicamente solo uso de las flags

#RET condición CC True

#POP
def POP_C1():
    global C
    global B
    global SP
    C = memoria[SP]
    aux = int(SP,2) + int('1',2)
    SP = Rell_Zeros(bin(aux))
    B = memoria[SP]
    aux = int(SP,2) + int('1',2)
    SP = Rell_Zeros(bin(aux))

#C2 funciona con condicion CC true

#JP
def JP_C3(arg):
    global CP
    CP = arg

#C4 es con CC true

#PUSH
def PUSH_C5():
    global C
    global B
    global SP
    aux = int(SP,2) - int('1',2)
    SP = Rell_Zeros(bin(aux))
    memoria[SP] = B
    aux = int(SP,2) - int('1',2)
    SP = Rell_Zeros(bin(aux))
    memoria[SP] = C

#ADD
def ADD_C6(arg):
    global A
    aux = int(A,2) + int(arg,2)
    A = Rell_Zeros(bin(aux))

#C7 el valor actual de PC+1 es metido en la Pila
#Luego se ubica en 00H

#C8 Condition cc is True
#C9 Stack
#CA cc is True
#CB tabla aparte



def POP_D1():
    global E
    global D
    global SP
    E = memoria[SP]
    aux = int(SP,2) + int('1',2)
    SP = Rell_Zeros(bin(aux))
    D = memoria[SP]
    aux = int(SP,2) + int('1',2)
    SP = Rell_Zeros(bin(aux))

#PUSH
def PUSH_D5():
    global E
    global D
    global SP
    aux = int(SP,2) - int('1',2)
    SP = Rell_Zeros(bin(aux))
    memoria[SP] = D
    aux = int(SP,2) - int('1',2)
    SP = Rell_Zeros(bin(aux))
    memoria[SP] = E

def EXX_D9():
    global B
    global C
    global D
    global E
    global H
    global L
    global BC
    global DE
    global HL
    global B_p
    global C_p
    global D_p
    global E_p
    global H_p
    global L_p
    global BC_p
    global DE_p
    global HL_p
    auxb=B
    auxc=C
    auxd=D
    auxe=E
    auxh=H
    auxl=L
    B = B_p
    C = C_p
    D = D_p
    E = E_p
    H = H_p
    L = L_p
    B_P = auxb
    C_P = auxc
    D_P = auxd
    E_P = auxe
    H_P = auxh
    L_P = auxl
    BC = B + C
    DE = D + E
    HL = H + L
    BC_p = B_p + C_p
    DE_p = D_p + E_p
    HL_p = H_p + L_p

def SUB_D6(arg):
    global A
    aux = int(A,2) - int(arg,2)
    A = Rell_Zeros(bin(aux))

def POP_E1():
    global L
    global H
    global SP
    L = memoria[SP]
    aux = int(SP,2) + int('1',2)
    SP = Rell_Zeros(bin(aux))
    H = memoria[SP]
    aux = int(SP,2) + int('1',2)
    SP = Rell_Zeros(bin(aux))

#PUSH
def PUSH_E5():
    global L
    global H
    global SP
    aux = int(SP,2) - int('1',2)
    SP = Rell_Zeros(bin(aux))
    memoria[SP] = H
    aux = int(SP,2) - int('1',2)
    SP = Rell_Zeros(bin(aux))
    memoria[SP] = L

def AND_E6(arg):
    global A
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and arg[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

def XOR_EE(arg):
    global A
    aux = ''
    for i in range(len(A))
        if A[i] == '1' and arg[i] == '0':
            aux += '1'
        elif A[i] == '0' and arg[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

def EX_EB():
    global D
    global E
    global H
    global L
    global DE
    global HL
    aux1 = D
    aux2 = E
    D = H
    E = L
    H = aux1
    L = aux2
    DE = D + E
    HL = H + L

def POP_F1():
    global F
    global A
    global SP
    auxF = memoria[SP]
    for i in range(len(F)):
        F[i] = auxF[i]
    aux = int(SP,2) + int('1',2)
    SP = Rell_Zeros(bin(aux))
    A = memoria[SP]
    aux = int(SP,2) + int('1',2)
    SP = Rell_Zeros(bin(aux))

#PUSH
def PUSH_F5():
    global F
    global A
    global SP
    aux = int(SP,2) - int('1',2)
    SP = Rell_Zeros(bin(aux))
    memoria[SP] = A
    aux = int(SP,2) - int('1',2)
    SP = Rell_Zeros(bin(aux))
    auxf = ''
    for i in range(len(F)):
        auxf += F[i]
    memoria[SP] = auxf

def OR_F6(arg):
    global A
    aux = ''
    for i in range(len(A))
        if A[i] == '1' or arg[i] == '1':
            aux += '1'
        else:
            aux += '0'
    A = aux

def LD_F9():
    global HL
    global SP
    SP = HL
#-------------------------------
"""
LD_01('1000000010101111')
print("B",B)
LD_02()
#INC_03()
INC_04()
print("B",B)
DEC_05()
print("B",B)
LD_06('10101110')
print("B",B)
ADD_09()
print("HL",HL)"""
print("A",A, type(A))
CPL_2F()
print("A",A)
