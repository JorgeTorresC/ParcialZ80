# -*- coding: utf-8 -*-
# *************************
# 21 De Octubre del 2018
# Emulador Procesador Z80
# Jorge Ivan Torres
# Daniel Caita
# *************************

from Funcions import *

# Pondremos una sóla instrucción de ensamblador por línea.
# Todos los valores numéricos se considerarán, por defecto, escritos en decimal.
# Para introducir valores números en hexadecimal los precederemos del carácter “$”,
# y para escribir valores numéricos en binario lo haremos mediante el carácter “%”.
# Los comentarios, que en  Z80 se introducen con el símbolo “;”,
# de forma que todo lo que el ensamblador encuentre a la derecha de un ; será ignorado.
# Podemos utilizar cualquier cadena de texto, excepto los nombres de las
# palabras reservadas de ensamblador.
# Ya que la entrada esta dada por comandos individuales se omiten etiquetas Como
# ORG, END, EQL que define variables

# (Diccionario instrucciones, diccionario registros, instruccion en Lista)
def enlazador(dic1, dic2, ins):
    respuesta = list[]
    if len(ins) > 0:
        if ins[0] in dic1:
            if len(ins) == 1:
                respuesta.append(1) # Flag en True
                respuesta.append(ins) # Opcode
                return respuesta

            #Instruccion argumento
            elif len(ins) == 2:
                if ins[1] in dic2:
                    respuesta.append(1) #flag
                    respuesta.append(ins[0]) #opcode
                    respuesta.append(ins[1]) #registro
                    return respuesta
                else:
                    if ins[1][0] == '%': #Binario
                        l = len(ins[1])
                        aux = ins[1][1:l]
                        respuesta.append(1) # Flag
                        respuesta.append(ins[0]) # Opcode
                        respuesta.append(aux) # numero binario
                        return respuesta
                    elif ins[1][0] == '$':#hexadecimal
                        aux = hexa_transform(ins[1][0]) #de HEX a BIN
                        respuesta.append(1) #Flag
                        respuesta.append(ins[0]) # Opcode
                        respuesta.append(aux) # Numero Bin
                        return respuesta
                    elif ins[1].isdigit(): #Entro un numero
                        l = len(ins[1])
                        aux=bin_trasnform(ins[1][1:l]) #pasar a binario
                        respuesta.append(1) # Flag
                        respuesta.append(ins[0]) # Opcode
                        respuesta.append(aux) # numero binario
                        return respuesta
                    else:
                        respuesta.append(0) #Flag en falso
                        respuesta.append('Comando invalido') #Mensaje de error
                        #print ('Comando invalido')
                        return respuesta
            #Fin 2

            #Intrucciones cortas Len 4
            elif len(ins) == 4:
                if ins[2] == ',':
                    if ins[1] in dic2 and ins[3] in dic2: #Si ambos estan en reg
                        respuesta.append(1) # Flag
                        respuesta.append(ins[0]) # Opcode
                        respuesta.append(ins[1]) # reg 1
                        respuesta.append(ins[3]) # reg 2
                        return respuesta

                    elif ins[1] not in dic2 and ins[3] in dic2: #Si solo esta el reg 2
                        if ins[1][0] == '%':#Binario
                            l = len(ins[1])
                            aux = ins[1][1:l]
                            respuesta.append(1) # Flag
                            respuesta.append(ins[0]) #Opcode
                            respuesta.append(aux) #Binario
                            respuesta.append(ins[3]) # Reg 2
                            return respuesta
                        elif ins[1][0] == '$': #hexadecimal
                            aux = hexa_transform(ins[1])
                            respuesta.append(1) #flag
                            respuesta.append(ins[0]) #opcode
                            respuesta.append(aux) #binario
                            respuesta.append(ins[3]) #reg 2
                            return respuesta
                        elif ins[1].isdigit():
                            aux = bin_trasnform(ins[1])
                            respuesta.append(1) # flag
                            respuesta.append(ins[0]) # opcode
                            respuesta.append(aux) # binario
                            respuesta.append(ins[3]) #registro
                            return respuesta
                        else:
                            respuesta.append(0) #Flag
                            respuesta.append('Primer parametro invalido')#Error
                            #print ('Comando invalido')
                            return respuesta
                    elif ins[3] not in dic2 and ins[1] in dic2: #Si solo esta el reg 1
                        if ins[3][0] == '%': #Binario
                            l = len(ins[3])
                            aux = ins[3][1:l]
                            respuesta.append(1) #Flag
                            respuesta.append(ins[0]) #Opcode
                            respuesta.append(ins[1]) #Reg 1
                            respuesta.append(aux) # Binario
                            return respuesta
                        elif ins[3][0] == '$': #hexadecimal
                            aux = hexa_transform(ins[3])
                            respuesta.append(1) # Flag
                            respuesta.append(ins[0]) # Opcode
                            respuesta.append(ins[1]) #Reg 1
                            respuesta.append(aux) #Binario
                            return respuesta
                        elif ins[3].isdigit(): #Digito
                            aux = bin_trasnform(ins[3])
                            respuesta.append(1) # Flag
                            respuesta.append(ins[0]) # Opcode
                            respuesta.append(ins[1]) #Reg 1
                            respuesta.append(aux) #Binario
                            return respuesta
                        else:
                            respuesta.append(0) #Flag
                            respuesta.append('Segundo parametro invalido')#Error
                            #print ('Comando invalido')
                            return respuesta
                    else: #Si ninguno esta en REG
                        if ins[1][0] == '%':
                            if ins[3][0] == '%':# Bin - Bin
                                l1 = len(ins[1])
                                l2 = len(ins[3])
                                aux1 = ins[1][1:l1]
                                aux2 = ins[3][1:l2]
                                respuesta.append(1) #Flag
                                respuesta.append(ins[0]) #Opcode
                                respuesta.append(aux1) #Binario
                                respuesta.append(aux2) #Binario
                                return respuesta
                            elif ins[3][0] == '$':#Bin - Hex
                                l1 = len(ins[1])
                                aux = hexa_transform(ins[3])
                                respuesta.append(1) #Flag
                                respuesta.append(ins[0]) #Opcode
                                respuesta.append(ins[1][1:l1]) #Binario 1
                                respuesta.append(aux) #Binario 2
                                return respuesta
                            elif ins[3].isdigit(): #Bin - Digito
                                aux = bin_trasnform(ins[3])
                                respuesta.append(1) #Flag
                                respuesta.append(ins[0]) #Opcode
                                respuesta.append(ins[1][1:l1]) #Binario 1
                                respuesta.append(aux) #Bnario 2
                                return respuesta
                            else: #Bin - Desconocido
                                respuesta.append(0) #Flag
                                respuesta.append('El segundo valor no se reconoce') #Error
                                return respuesta
                        elif ins[1][0] == '$':
                            if ins[3][0] == '%': #Hex - Bin
                                aux1 = hexa_transform(ins[1])
                                l2 = len(ins[3])
                                aux2 = ins[3][1:l2]
                                respuesta.append(1) #Flag
                                respuesta.append(ins[0]) #Opcode
                                respuesta.append(aux1) #Binario 1
                                respuesta.append(aux2) #Binario 2
                                return respuesta
                            elif ins[3][0] == '$':# Hex - Hex
                                aux1 = hexa_transform(ins[1])
                                aux2 = hexa_transform(ins[3])
                                respuesta.append(1) #Flag
                                respuesta.append(ins[0]) #Opcode
                                respuesta.append(aux1) #Binario 1
                                respuesta.append(aux2) #Binario 2
                                return respuesta
                            elif ins[3].isdigit(): #Hex - Digito
                                aux1 = hexa_transform(ins[1])
                                aux2 = bin_trasnform(ins[3])
                                respuesta.append(1) #Flag
                                respuesta.append(ins[0]) #Opcode
                                respuesta.append(aux1) #Binario 1
                                respuesta.append(aux2) #Binario 2
                                return respuesta
                            else: #Hex - Desconocido
                                respuesta.append(0) #Flag
                                respuesta.append('El segundo valor no se reconoce')
                                return respuesta
                        elif ins[1].isdigit():
                            if ins[3][0] == '%': #Digito - Bin
                                aux1 = bin_trasnform(ins[1])
                                l2 = len(ins[3])
                                aux2 = ins[3][1:l2]
                                respuesta.append(1) #Flag
                                respuesta.append(ins[0]) #Opcode
                                respuesta.append(aux1) #Binario 1
                                respuesta.append(aux2) #Binario 2
                                return respuesta
                            elif ins[3][0] == '$':# Digito - Hex
                                aux1 = bin_trasnform(ins[1])
                                aux2 = hexa_transform(ins[3])
                                respuesta.append(1) #Flag
                                respuesta.append(ins[0]) #Opcode
                                respuesta.append(aux1) #Binario 1
                                respuesta.append(aux2) #Binario 2
                                return respuesta
                            elif ins[3].isdigit(): #Digito - Digito
                                aux1 = bin_trasnform(ins[1])
                                aux2 = bin_trasnform(ins[3])
                                respuesta.append(1) #Flag
                                respuesta.append(ins[0]) #Opcode
                                respuesta.append(aux1) #Binario 1
                                respuesta.append(aux2) #Binario 2
                                return respuesta
                            else: #Hex - Desconocido
                                respuesta.append(0) #Flag
                                respuesta.append('El segundo valor no se reconoce')
                                return respuesta
                        else:
                            respuesta.append(0) #Flag
                            respuesta.append('El primer valor no se reconoce')
                            #print ('Comando invalido')
                            return respuesta
                else:
                    respuesta.append(0)
                    respuesta.append("Se espera ',' ")
                    #print ('Separador no valido')
            #Fin 4

            #Para instruciones de 6
            elif len(ins) == 6:
                if ins[2] == ',' or ins[4] == ',':

                    #Primer caso de 6
                    if ins[1] == '(' or ins[1] == '[':
                        if ins[3] == ')' or ins[3] == ']' :
                            if ins[2] in dic2 and ins[5] in dic2: #Si ambos estan en reg
                                respuesta.append(1) # Flag
                                respuesta.append(ins[0]) # Opcode
                                respuesta.append(ins[2]) # reg 1
                                respuesta.append(ins[5]) # reg 2
                                return respuesta
                            elif ins[2] not in dic2 and ins[5] in dic2: #Si solo esta el reg 2
                                if ins[2][0] == '%':#Binario
                                    l = len(ins[2])
                                    aux = ins[2][1:l]
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(aux) #Binario
                                    respuesta.append(ins[5]) # Reg 2
                                    return respuesta
                                elif ins[2][0] == '$': #hexadecimal
                                    aux = hexa_transform(ins[2])
                                    respuesta.append(1) #flag
                                    respuesta.append(ins[0]) #opcode
                                    respuesta.append(aux) #binario
                                    respuesta.append(ins[5]) #reg 2
                                    return respuesta
                                elif ins[2].isdigit():
                                    aux = bin_trasnform(ins[2])
                                    respuesta.append(1) # flag
                                    respuesta.append(ins[0]) # opcode
                                    respuesta.append(aux) # binario
                                    respuesta.append(ins[5]) #registro
                                    return respuesta
                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('Primer parametro invalido')#Error
                                    #print ('Comando invalido')
                                    return respuesta
                            elif ins[5] not in dic2 and ins[2] in dic2: #Si solo esta el reg 1
                                if ins[5][0] == '%': #Binario
                                    l = len(ins[5])
                                    aux = ins[5][1:l]
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(ins[2]) #Reg 1
                                    respuesta.append(aux) # Binario
                                    return respuesta
                                elif ins[5][0] == '$': #hexadecimal
                                    aux = hexa_transform(ins[5])
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) # Opcode
                                    respuesta.append(ins[2]) #Reg 1
                                    respuesta.append(aux) #Binario
                                    return respuesta
                                elif ins[5].isdigit(): #Digito
                                    aux = bin_trasnform(ins[5])
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) # Opcode
                                    respuesta.append(ins[2]) #Reg 1
                                    respuesta.append(aux) #Binario
                                    return respuesta
                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('Segundo parametro invalido')#Error
                                    #print ('Comando invalido')
                                    return respuesta
                            else: #Si ninguno esta en REG
                                if ins[2][0] == '%':
                                    if ins[5][0] == '%':# Bin - Bin
                                        l1 = len(ins[2])
                                        l2 = len(ins[5])
                                        aux1 = ins[2][1:l1]
                                        aux2 = ins[5][1:l2]
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(aux1) #Binario
                                        respuesta.append(aux2) #Binario
                                        return respuesta
                                    elif ins[5][0] == '$':#Bin - Hex
                                        l1 = len(ins[2])
                                        aux = hexa_transform(ins[5])
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(ins[2][1:l1]) #Binario 1
                                        respuesta.append(aux) #Binario 2
                                        return respuesta
                                    elif ins[5].isdigit(): #Bin - Digito
                                        aux = bin_trasnform(ins[5])
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(ins[2][1:l1]) #Binario 1
                                        respuesta.append(aux) #Bnario 2
                                        return respuesta
                                    else: #Bin - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce') #Error
                                        return respuesta
                                elif ins[2][0] == '$':
                                    if ins[5][0] == '%': #Hex - Bin
                                        aux1 = hexa_transform(ins[2])
                                        l2 = len(ins[5])
                                        aux2 = ins[5][1:l2]
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(aux1) #Binario 1
                                        respuesta.append(aux2) #Binario 2
                                        return respuesta
                                    elif ins[5][0] == '$':# Hex - Hex
                                        aux1 = hexa_transform(ins[2])
                                        aux2 = hexa_transform(ins[5])
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(aux1) #Binario 1
                                        respuesta.append(aux2) #Binario 2
                                        return respuesta
                                    elif ins[5].isdigit(): #Hex - Digito
                                        aux1 = hexa_transform(ins[2])
                                        aux2 = bin_trasnform(ins[5])
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(aux1) #Binario 1
                                        respuesta.append(aux2) #Binario 2
                                        return respuesta
                                    else: #Hex - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce')
                                        return respuesta
                                elif ins[2].isdigit():
                                    if ins[5][0] == '%': #Digito - Bin
                                        aux1 = bin_trasnform(ins[2])
                                        l2 = len(ins[5])
                                        aux2 = ins[5][1:l2]
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(aux1) #Binario 1
                                        respuesta.append(aux2) #Binario 2
                                        return respuesta
                                    elif ins[5][0] == '$':# Digito - Hex
                                        aux1 = bin_trasnform(ins[2])
                                        aux2 = hexa_transform(ins[5])
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(aux1) #Binario 1
                                        respuesta.append(aux2) #Binario 2
                                        return respuesta
                                    elif ins[5].isdigit(): #Digito - Digito
                                        aux1 = bin_trasnform(ins[2])
                                        aux2 = bin_trasnform(ins[5])
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(aux1) #Binario 1
                                        respuesta.append(aux2) #Binario 2
                                        return respuesta
                                    else: #Hex - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce')
                                        return respuesta
                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('El primer valor no se reconoce')
                                    #print ('Comando invalido')
                                    return respuesta
                        else:
                            respuesta.append(0)
                            respuesta.append("Se espera un cierre ")
                            #print ("Se espera un cierre ")

                    #Segundo caso de 6
                    elif ins[3] == '(' or ins[3] == '[':
                        if ins[5] == ')' or ins[5] == ']':
                            if ins[1] in dic2 and ins[4] in dic2: #Si ambos estan en reg
                                respuesta.append(1) # Flag
                                respuesta.append(ins[0]) # Opcode
                                respuesta.append(ins[1]) # reg 1
                                respuesta.append(ins[4]) # reg 2
                                return respuesta
                            elif ins[1] not in dic2 and ins[4] in dic2: #Si solo esta el reg 2
                                if ins[1][0] == '%':#Binario
                                    l = len(ins[1])
                                    aux = ins[1][1:l]
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(aux) #Binario
                                    respuesta.append(ins[4]) # Reg 2
                                    return respuesta
                                elif ins[1][0] == '$': #hexadecimal
                                    aux = hexa_transform(ins[1])
                                    respuesta.append(1) #flag
                                    respuesta.append(ins[0]) #opcode
                                    respuesta.append(aux) #binario
                                    respuesta.append(ins[4]) #reg 2
                                    return respuesta
                                elif ins[1].isdigit():
                                    aux = bin_trasnform(ins[1])
                                    respuesta.append(1) # flag
                                    respuesta.append(ins[0]) # opcode
                                    respuesta.append(aux) # binario
                                    respuesta.append(ins[4]) #registro
                                    return respuesta
                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('Primer parametro invalido')#Error
                                    #print ('Comando invalido')
                                    return respuesta
                            elif ins[4] not in dic2 and ins[1] in dic2: #Si solo esta el reg 1
                                if ins[4][0] == '%': #Binario
                                    l = len(ins[4])
                                    aux = ins[4][1:l]
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(ins[1]) #Reg 1
                                    respuesta.append(aux) # Binario
                                    return respuesta
                                elif ins[4][0] == '$': #hexadecimal
                                    aux = hexa_transform(ins[4])
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) # Opcode
                                    respuesta.append(ins[1]) #Reg 1
                                    respuesta.append(aux) #Binario
                                    return respuesta
                                elif ins[4].isdigit(): #Digito
                                    aux = bin_trasnform(ins[4])
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) # Opcode
                                    respuesta.append(ins[1]) #Reg 1
                                    respuesta.append(aux) #Binario
                                    return respuesta
                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('Segundo parametro invalido')#Error
                                    #print ('Comando invalido')
                                    return respuesta
                            else: #Si ninguno esta en REG
                                if ins[1][0] == '%':
                                    if ins[4][0] == '%':# Bin - Bin
                                        l1 = len(ins[1])
                                        l2 = len(ins[4])
                                        aux1 = ins[1][1:l1]
                                        aux2 = ins[4][1:l2]
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(aux1) #Binario
                                        respuesta.append(aux2) #Binario
                                        return respuesta
                                    elif ins[4][0] == '$':#Bin - Hex
                                        l1 = len(ins[1])
                                        aux = hexa_transform(ins[4])
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(ins[1][1:l1]) #Binario 1
                                        respuesta.append(aux) #Binario 2
                                        return respuesta
                                    elif ins[4].isdigit(): #Bin - Digito
                                        aux = bin_trasnform(ins[4])
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(ins[1][1:l1]) #Binario 1
                                        respuesta.append(aux) #Bnario 2
                                        return respuesta
                                    else: #Bin - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce') #Error
                                        return respuesta
                                elif ins[1][0] == '$':
                                    if ins[4][0] == '%': #Hex - Bin
                                        aux1 = hexa_transform(ins[1])
                                        l2 = len(ins[4])
                                        aux2 = ins[4][1:l2]
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(aux1) #Binario 1
                                        respuesta.append(aux2) #Binario 2
                                        return respuesta
                                    elif ins[4][0] == '$':# Hex - Hex
                                        aux1 = hexa_transform(ins[1])
                                        aux2 = hexa_transform(ins[4])
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(aux1) #Binario 1
                                        respuesta.append(aux2) #Binario 2
                                        return respuesta
                                    elif ins[4].isdigit(): #Hex - Digito
                                        aux1 = hexa_transform(ins[1])
                                        aux2 = bin_trasnform(ins[4])
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(aux1) #Binario 1
                                        respuesta.append(aux2) #Binario 2
                                        return respuesta
                                    else: #Hex - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce')
                                        return respuesta
                                elif ins[1].isdigit():
                                    if ins[4][0] == '%': #Digito - Bin
                                        aux1 = bin_trasnform(ins[1])
                                        l2 = len(ins[4])
                                        aux2 = ins[4][1:l2]
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(aux1) #Binario 1
                                        respuesta.append(aux2) #Binario 2
                                        return respuesta
                                    elif ins[4][0] == '$':# Digito - Hex
                                        aux1 = bin_trasnform(ins[1])
                                        aux2 = hexa_transform(ins[4])
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(aux1) #Binario 1
                                        respuesta.append(aux2) #Binario 2
                                        return respuesta
                                    elif ins[4].isdigit(): #Digito - Digito
                                        aux1 = bin_trasnform(ins[1])
                                        aux2 = bin_trasnform(ins[4])
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(aux1) #Binario 1
                                        respuesta.append(aux2) #Binario 2
                                        return respuesta
                                    else: #Hex - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce')
                                        return respuesta
                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('El primer valor no se reconoce')
                                    #print ('Comando invalido')
                                    return respuesta
                        else:
                            respuesta.append(0)
                            respuesta.append("Se espera un cierre ")
                            #print ("Se espera un cierre ")
                            return respuesta
                    #Tercer caso A
                    elif ins[3] == '+':
                        if ins[2] in dic2 and ins[4] in dic2: #Si ambos estan en reg
                            aux1 = dic2[ins[2]]
                            aux2 = dic2[ins[4]]
                            res=add_registros(aux1, aux2)
                            respuesta.append(1) # Flag
                            respuesta.append(ins[0]) # Opcode
                            respuesta.append(res) # resultado suma
                            return respuesta
                        elif ins[2] not in dic2 and ins[4] in dic2: #Si solo esta el reg 2
                            if ins[2][0] == '%':#Binario
                                l = len(ins[2])
                                aux1 = ins[2][1:l]
                                aux2 = dic2[ins[4]]
                                res=add_registros(aux1, aux2)
                                respuesta.append(1) # Flag
                                respuesta.append(ins[0]) #Opcode
                                respuesta.append(res) # Binario suma
                                return respuesta
                            elif ins[2][0] == '$': #hexadecimal
                                aux1 = hexa_transform(ins[2])
                                aux2 = dic2[ins[4]]
                                res=add_registros(aux1, aux2)
                                respuesta.append(1) #flag
                                respuesta.append(ins[0]) #opcode
                                respuesta.append(res) #binario suma
                                return respuesta
                            elif ins[2].isdigit():
                                aux1 = bin_trasnform(ins[2])
                                aux2 = dic2[ins[4]]
                                res=add_registros(aux1, aux2)
                                respuesta.append(1) # flag
                                respuesta.append(ins[0]) # opcode
                                respuesta.append(res) # binario suma
                                return respuesta
                            else:
                                respuesta.append(0) #Flag
                                respuesta.append('Primer parametro invalido')#Error
                                #print ('Comando invalido')
                                return respuesta
                        elif ins[4] not in dic2 and ins[2] in dic2: #Si solo esta el reg 1
                            if ins[4][0] == '%': #Binario
                                aux1 = dic2[ins[2]]
                                l = len(ins[4])
                                aux = ins[4][1:l]
                                res=add_registros(aux1, aux2)
                                respuesta.append(1) #Flag
                                respuesta.append(ins[0]) #Opcode
                                respuesta.append(res) #Resultado suma
                                return respuesta
                            elif ins[4][0] == '$': #hexadecimal
                                aux1 = dic2[ins[2]]
                                aux2 = hexa_transform(ins[4])
                                res=add_registros(aux1, aux2)
                                respuesta.append(1) # Flag
                                respuesta.append(ins[0]) # Opcode
                                respuesta.append(res) #Resultado suma
                                return respuesta
                            elif ins[4].isdigit(): #Digito
                                aux1 = dic2[ins[2]]
                                aux2 = bin_trasnform(ins[4])
                                res=add_registros(aux1, aux2)
                                respuesta.append(1) # Flag
                                respuesta.append(ins[0]) # Opcode
                                respuesta.append(res) #Resultado suma
                                return respuesta
                            else:
                                respuesta.append(0) #Flag
                                respuesta.append('Segundo parametro invalido')#Error
                                #print ('Comando invalido')
                                return respuesta
                        else: #Si ninguno esta en REG
                            if ins[2][0] == '%':
                                if ins[4][0] == '%':# Bin - Bin
                                    l1 = len(ins[2])
                                    l2 = len(ins[4])
                                    aux1 = ins[2][1:l1]
                                    aux2 = ins[2][1:l2]
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                elif ins[4][0] == '$':#Bin - Hex
                                    l1 = len(ins[2])
                                    aux1 = ins[2][1:l1]
                                    aux2 = hexa_transform(ins[4])
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                elif ins[4].isdigit(): #Bin - Digito
                                    aux1 = ins[2][1:l1]
                                    aux2 = bin_trasnform(ins[4])
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                else: #Bin - Desconocido
                                    respuesta.append(0) #Flag
                                    respuesta.append('El segundo valor no se reconoce') #Error
                                    return respuesta
                            elif ins[2][0] == '$':
                                if ins[4][0] == '%': #Hex - Bin
                                    aux1 = hexa_transform(ins[2])
                                    l2 = len(ins[4])
                                    aux2 = ins[4][1:l2]
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                elif ins[4][0] == '$':# Hex - Hex
                                    aux1 = hexa_transform(ins[2])
                                    aux2 = hexa_transform(ins[4])
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                elif ins[4].isdigit(): #Hex - Digito
                                    aux1 = hexa_transform(ins[2])
                                    aux2 = bin_trasnform(ins[4])
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                else: #Hex - Desconocido
                                    respuesta.append(0) #Flag
                                    respuesta.append('El segundo valor no se reconoce')
                                    return respuesta
                            elif ins[2].isdigit():
                                if ins[4][0] == '%': #Digito - Bin
                                    aux1 = bin_trasnform(ins[2])
                                    l2 = len(ins[4])
                                    aux2 = ins[4][1:l2]
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                elif ins[4][0] == '$':# Digito - Hex
                                    aux1 = bin_trasnform(ins[2])
                                    aux2 = hexa_transform(ins[4])
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                elif ins[4].isdigit(): #Digito - Digito
                                    aux1 = bin_trasnform(ins[2])
                                    aux2 = bin_trasnform(ins[4])
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario 1
                                    return respuesta
                                else: #Hex - Desconocido
                                    respuesta.append(0) #Flag
                                    respuesta.append('El segundo valor no se reconoce')
                                    return respuesta
                            else:
                                respuesta.append(0) #Flag
                                respuesta.append('El primer valor no se reconoce')
                                #print ('Comando invalido')
                                return respuesta
                    #Tercer caso B
                    elif  ins[3] == '-':
                        if ins[2] in dic2 and ins[4] in dic2: #Si ambos estan en reg
                            aux1 = dic2[ins[2]]
                            aux2 = dic2[ins[4]]
                            res=res_registros(aux1, aux2)
                            respuesta.append(1) # Flag
                            respuesta.append(ins[0]) # Opcode
                            respuesta.append(res) # resultado suma
                            return respuesta
                        elif ins[2] not in dic2 and ins[4] in dic2: #Si solo esta el reg 2
                            if ins[2][0] == '%':#Binario
                                l = len(ins[2])
                                aux1 = ins[2][1:l]
                                aux2 = dic2[ins[4]]
                                res=res_registros(aux1, aux2)
                                respuesta.append(1) # Flag
                                respuesta.append(ins[0]) #Opcode
                                respuesta.append(res) # Binario suma
                                return respuesta
                            elif ins[2][0] == '$': #hexadecimal
                                aux1 = hexa_transform(ins[2])
                                aux2 = dic2[ins[4]]
                                res=res_registros(aux1, aux2)
                                respuesta.append(1) #flag
                                respuesta.append(ins[0]) #opcode
                                respuesta.append(res) #binario suma
                                return respuesta
                            elif ins[2].isdigit():
                                aux1 = bin_trasnform(ins[2])
                                aux2 = dic2[ins[4]]
                                res=res_registros(aux1, aux2)
                                respuesta.append(1) # flag
                                respuesta.append(ins[0]) # opcode
                                respuesta.append(res) # binario suma
                                return respuesta
                            else:
                                respuesta.append(0) #Flag
                                respuesta.append('Primer parametro invalido')#Error
                                #print ('Comando invalido')
                                return respuesta
                        elif ins[4] not in dic2 and ins[2] in dic2: #Si solo esta el reg 1
                            if ins[4][0] == '%': #Binario
                                aux1 = dic2[ins[2]]
                                l = len(ins[4])
                                aux = ins[4][1:l]
                                res=res_registros(aux1, aux2)
                                respuesta.append(1) #Flag
                                respuesta.append(ins[0]) #Opcode
                                respuesta.append(res) #Resultado suma
                                return respuesta
                            elif ins[4][0] == '$': #hexadecimal
                                aux1 = dic2[ins[2]]
                                aux2 = hexa_transform(ins[4])
                                res=res_registros(aux1, aux2)
                                respuesta.append(1) # Flag
                                respuesta.append(ins[0]) # Opcode
                                respuesta.append(res) #Resultado suma
                                return respuesta
                            elif ins[4].isdigit(): #Digito
                                aux1 = dic2[ins[2]]
                                aux2 = bin_trasnform(ins[4])
                                res=res_registros(aux1, aux2)
                                respuesta.append(1) # Flag
                                respuesta.append(ins[0]) # Opcode
                                respuesta.append(res) #Resultado suma
                                return respuesta
                            else:
                                respuesta.append(0) #Flag
                                respuesta.append('Segundo parametro invalido')#Error
                                #print ('Comando invalido')
                                return respuesta
                        else: #Si ninguno esta en REG
                            if ins[2][0] == '%':
                                if ins[4][0] == '%':# Bin - Bin
                                    l1 = len(ins[2])
                                    l2 = len(ins[4])
                                    aux1 = ins[2][1:l1]
                                    aux2 = ins[2][1:l2]
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                elif ins[4][0] == '$':#Bin - Hex
                                    l1 = len(ins[2])
                                    aux1 = ins[2][1:l1]
                                    aux2 = hexa_transform(ins[4])
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                elif ins[4].isdigit(): #Bin - Digito
                                    aux1 = ins[2][1:l1]
                                    aux2 = bin_trasnform(ins[4])
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                else: #Bin - Desconocido
                                    respuesta.append(0) #Flag
                                    respuesta.append('El segundo valor no se reconoce') #Error
                                    return respuesta
                            elif ins[2][0] == '$':
                                if ins[4][0] == '%': #Hex - Bin
                                    aux1 = hexa_transform(ins[2])
                                    l2 = len(ins[4])
                                    aux2 = ins[4][1:l2]
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                elif ins[4][0] == '$':# Hex - Hex
                                    aux1 = hexa_transform(ins[2])
                                    aux2 = hexa_transform(ins[4])
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                elif ins[4].isdigit(): #Hex - Digito
                                    aux1 = hexa_transform(ins[2])
                                    aux2 = bin_trasnform(ins[4])
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                else: #Hex - Desconocido
                                    respuesta.append(0) #Flag
                                    respuesta.append('El segundo valor no se reconoce')
                                    return respuesta
                            elif ins[2].isdigit():
                                if ins[4][0] == '%': #Digito - Bin
                                    aux1 = bin_trasnform(ins[2])
                                    l2 = len(ins[4])
                                    aux2 = ins[4][1:l2]
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                elif ins[4][0] == '$':# Digito - Hex
                                    aux1 = bin_trasnform(ins[2])
                                    aux2 = hexa_transform(ins[4])
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario suma
                                    return respuesta
                                elif ins[4].isdigit(): #Digito - Digito
                                    aux1 = bin_trasnform(ins[2])
                                    aux2 = bin_trasnform(ins[4])
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Binario 1
                                    return respuesta
                                else: #Hex - Desconocido
                                    respuesta.append(0) #Flag
                                    respuesta.append('El segundo valor no se reconoce')
                                    return respuesta
                            else:
                                respuesta.append(0) #Flag
                                respuesta.append('El primer valor no se reconoce')
                                #print ('Comando invalido')
                                return respuesta
                else:
                    respuesta.append(0)
                    respuesta.append('Comando invalido')
                    #print ('Comando invalido')
            #Fin Len 6

            #Para instrucciones más largas 8
            elif len(ins) == 8:
                if ins[1] == '(' or ins[1] == '[':
                    if ins[5] == ')' or ins[5] == ']':
                        if ins[3] == '+':
                            if ins[2] in dic2 and ins[4] in dic2: #Si ambos estan en reg
                                aux1 = dic2[ins[2]]
                                aux2 = dic2[ins[4]]
                                res=add_registros(aux1, aux2)
                                respuesta.append(1) # Flag
                                respuesta.append(ins[0]) # Opcode
                                respuesta.append(res) # resultado suma
                                if ins[7] in dic2:
                                    aux3 = dic2[ins[7]]
                                    respuesta.append(aux3) #
                                    return respuesta
                                elif ins[7][0] =='%':
                                    l = len(ins[7])
                                    aux3 = ins[7][1:l]
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[7][0] =='$':
                                    aux3 = hexa_transform(ins[2])
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[7].isdigit():
                                    aux3 = bin_trasnform(ins[7])
                                    respuesta.append(aux3)
                                    return respuesta
                                else:
                                    respuesta=[]
                                    respuesta.append(0)
                                    respuesta.append('Segundo parametro erroneo')
                                    return respuesta
                            elif ins[2] not in dic2 and ins[4] in dic2: #Si solo esta el reg 2
                                if ins[2][0] == '%':#Binario
                                    l = len(ins[2])
                                    aux1 = ins[2][1:l]
                                    aux2 = dic2[ins[4]]
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) # Binario suma
                                elif ins[2][0] == '$': #hexadecimal
                                    aux1 = hexa_transform(ins[2])
                                    aux2 = dic2[ins[4]]
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) #flag
                                    respuesta.append(ins[0]) #opcode
                                    respuesta.append(res) #binario suma
                                elif ins[2].isdigit():
                                    aux1 = bin_trasnform(ins[2])
                                    aux2 = dic2[ins[4]]
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) # flag
                                    respuesta.append(ins[0]) # opcode
                                    respuesta.append(res) # binario suma
                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('Primer parametro invalido')#Error
                                    #print ('Comando invalido')
                                if ins[7] in dic2:
                                    aux3 = dic2[ins[7]]
                                    respuesta.append(aux3) #
                                    return respuesta
                                elif ins[7][0] =='%':
                                    l = len(ins[7])
                                    aux3 = ins[7][1:l]
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[7][0] =='$':
                                    aux3 = hexa_transform(ins[7])
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[7].isdigit():
                                    aux3 = bin_trasnform(ins[7])
                                    respuesta.append(aux3)
                                    return respuesta
                                else:
                                    respuesta=[]
                                    respuesta.append(0)
                                    respuesta.append('Segundo parametro erroneo')
                                    return respuesta
                            elif ins[4] not in dic2 and ins[2] in dic2: #Si solo esta el reg 1
                                if ins[4][0] == '%': #Binario
                                    aux1 = dic2[ins[2]]
                                    l = len(ins[4])
                                    aux = ins[4][1:l]
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Resultado suma
                                elif ins[4][0] == '$': #hexadecimal
                                    aux1 = dic2[ins[2]]
                                    aux2 = hexa_transform(ins[4])
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) # Opcode
                                    respuesta.append(res) #Resultado suma
                                elif ins[4].isdigit(): #Digito
                                    aux1 = dic2[ins[2]]
                                    aux2 = bin_trasnform(ins[4])
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) # Opcode
                                    respuesta.append(res) #Resultado suma
                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('Segundo parametro invalido')#Error
                                    #print ('Comando invalido')
                                    return respuesta
                                if ins[7] in dic2:
                                    aux3 = dic2[ins[7]]
                                    respuesta.append(aux3) #
                                    return respuesta
                                elif ins[7][0] =='%':
                                    l = len(ins[7])
                                    aux3 = ins[7][1:l]
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[7][0] =='$':
                                    aux3 = hexa_transform(ins[7])
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[7].isdigit():
                                    aux3 = bin_trasnform(ins[7])
                                    respuesta.append(aux3)
                                    return respuesta
                                else:
                                    respuesta=[]
                                    respuesta.append(0)
                                    respuesta.append('Segundo parametro erroneo')
                                    return respuesta
                            else: #Si ninguno esta en REG
                                if ins[2][0] == '%':
                                    if ins[4][0] == '%':# Bin - Bin
                                        l1 = len(ins[2])
                                        l2 = len(ins[4])
                                        aux1 = ins[2][1:l1]
                                        aux2 = ins[2][1:l2]
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4][0] == '$':#Bin - Hex
                                        l1 = len(ins[2])
                                        aux1 = ins[2][1:l1]
                                        aux2 = hexa_transform(ins[4])
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4].isdigit(): #Bin - Digito
                                        aux1 = ins[2][1:l1]
                                        aux2 = bin_trasnform(ins[4])
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    else: #Bin - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce') #Error
                                        return respuesta
                                    if ins[7] in dic2:
                                        aux3 = dic2[ins[7]]
                                        respuesta.append(aux3) #
                                        return respuesta
                                    elif ins[7][0] =='%':
                                        l = len(ins[7])
                                        aux3 = ins[7][1:l]
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[7][0] =='$':
                                        aux3 = hexa_transform(ins[2])
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[7].isdigit():
                                        aux3 = bin_trasnform(ins[7])
                                        respuesta.append(aux3)
                                        return respuesta
                                    else:
                                        respuesta=[]
                                        respuesta.append(0)
                                        respuesta.append('Segundo parametro erroneo')
                                        return respuesta
                                elif ins[2][0] == '$':
                                    if ins[4][0] == '%': #Hex - Bin
                                        aux1 = hexa_transform(ins[2])
                                        l2 = len(ins[4])
                                        aux2 = ins[4][1:l2]
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4][0] == '$':# Hex - Hex
                                        aux1 = hexa_transform(ins[2])
                                        aux2 = hexa_transform(ins[4])
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4].isdigit(): #Hex - Digito
                                        aux1 = hexa_transform(ins[2])
                                        aux2 = bin_trasnform(ins[4])
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    else: #Hex - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce')
                                        return respuesta
                                    if ins[7] in dic2:
                                        aux3 = dic2[ins[7]]
                                        respuesta.append(aux3) #
                                        return respuesta
                                    elif ins[7][0] =='%':
                                        l = len(ins[7])
                                        aux3 = ins[7][1:l]
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[7][0] =='$':
                                        aux3 = hexa_transform(ins[7])
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[7].isdigit():
                                        aux3 = bin_trasnform(ins[7])
                                        respuesta.append(aux3)
                                        return respuesta
                                    else:
                                        respuesta=[]
                                        respuesta.append(0)
                                        respuesta.append('Segundo parametro erroneo')
                                        return respuesta
                                elif ins[2].isdigit():
                                    if ins[4][0] == '%': #Digito - Bin
                                        aux1 = bin_trasnform(ins[2])
                                        l2 = len(ins[4])
                                        aux2 = ins[4][1:l2]
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4][0] == '$':# Digito - Hex
                                        aux1 = bin_trasnform(ins[2])
                                        aux2 = hexa_transform(ins[4])
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4].isdigit(): #Digito - Digito
                                        aux1 = bin_trasnform(ins[2])
                                        aux2 = bin_trasnform(ins[4])
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario 1
                                    else: #Hex - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce')
                                        return respuesta
                                    if ins[7] in dic2:
                                        aux3 = dic2[ins[7]]
                                        respuesta.append(aux3) #
                                        return respuesta
                                    elif ins[7][0] =='%':
                                        l = len(ins[7])
                                        aux3 = ins[7][1:l]
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[7][0] =='$':
                                        aux3 = hexa_transform(ins[2])
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[7].isdigit():
                                        aux3 = bin_trasnform(ins[7])
                                        respuesta.append(aux3)
                                        return respuesta
                                    else:
                                        respuesta=[]
                                        respuesta.append(0)
                                        respuesta.append('Segundo parametro erroneo')
                                        return respuesta

                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('El primer valor no se reconoce')
                                    #print ('Comando invalido')
                                    return respuesta

                        elif ins[3] == '-':
                            if ins[2] in dic2 and ins[4] in dic2: #Si ambos estan en reg
                                aux1 = dic2[ins[2]]
                                aux2 = dic2[ins[4]]
                                res = res_registros(aux1, aux2)
                                respuesta.append(1) # Flag
                                respuesta.append(ins[0]) # Opcode
                                respuesta.append(res) # resultado suma
                                if ins[7] in dic2:
                                    aux3 = dic2[ins[7]]
                                    respuesta.append(aux3) #
                                    return respuesta
                                elif ins[7][0] =='%':
                                    l = len(ins[7])
                                    aux3 = ins[7][1:l]
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[7][0] =='$':
                                    aux3 = hexa_transform(ins[2])
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[7].isdigit():
                                    aux3 = bin_trasnform(ins[7])
                                    respuesta.append(aux3)
                                    return respuesta
                                else:
                                    respuesta=[]
                                    respuesta.append(0)
                                    respuesta.append('Segundo parametro erroneo')
                                    return respuesta
                            elif ins[2] not in dic2 and ins[4] in dic2: #Si solo esta el reg 2
                                if ins[2][0] == '%':#Binario
                                    l = len(ins[2])
                                    aux1 = ins[2][1:l]
                                    aux2 = dic2[ins[4]]
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) # Binario suma
                                elif ins[2][0] == '$': #hexadecimal
                                    aux1 = hexa_transform(ins[2])
                                    aux2 = dic2[ins[4]]
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) #flag
                                    respuesta.append(ins[0]) #opcode
                                    respuesta.append(res) #binario suma
                                elif ins[2].isdigit():
                                    aux1 = bin_trasnform(ins[2])
                                    aux2 = dic2[ins[4]]
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) # flag
                                    respuesta.append(ins[0]) # opcode
                                    respuesta.append(res) # binario suma
                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('Primer parametro invalido')#Error
                                    #print ('Comando invalido')
                                if ins[7] in dic2:
                                    aux3 = dic2[ins[7]]
                                    respuesta.append(aux3) #
                                    return respuesta
                                elif ins[7][0] =='%':
                                    l = len(ins[7])
                                    aux3 = ins[7][1:l]
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[7][0] =='$':
                                    aux3 = hexa_transform(ins[2])
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[7].isdigit():
                                    aux3 = bin_trasnform(ins[7])
                                    respuesta.append(aux3)
                                    return respuesta
                                else:
                                    respuesta=[]
                                    respuesta.append(0)
                                    respuesta.append('Segundo parametro erroneo')
                                    return respuesta
                            elif ins[4] not in dic2 and ins[2] in dic2: #Si solo esta el reg 1
                                if ins[4][0] == '%': #Binario
                                    aux1 = dic2[ins[2]]
                                    l = len(ins[4])
                                    aux = ins[4][1:l]
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Resultado suma
                                elif ins[4][0] == '$': #hexadecimal
                                    aux1 = dic2[ins[2]]
                                    aux2 = hexa_transform(ins[4])
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) # Opcode
                                    respuesta.append(res) #Resultado suma
                                elif ins[4].isdigit(): #Digito
                                    aux1 = dic2[ins[2]]
                                    aux2 = bin_trasnform(ins[4])
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) # Opcode
                                    respuesta.append(res) #Resultado suma
                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('Segundo parametro invalido')#Error
                                    #print ('Comando invalido')
                                    return respuesta
                                if ins[7] in dic2:
                                    aux3 = dic2[ins[7]]
                                    respuesta.append(aux3) #
                                    return respuesta
                                elif ins[7][0] =='%':
                                    l = len(ins[7])
                                    aux3 = ins[7][1:l]
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[7][0] =='$':
                                    aux3 = hexa_transform(ins[2])
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[7].isdigit():
                                    aux3 = bin_trasnform(ins[7])
                                    respuesta.append(aux3)
                                    return respuesta
                                else:
                                    respuesta=[]
                                    respuesta.append(0)
                                    respuesta.append('Segundo parametro erroneo')
                                    return respuesta
                            else: #Si ninguno esta en REG
                                if ins[2][0] == '%':
                                    if ins[4][0] == '%':# Bin - Bin
                                        l1 = len(ins[2])
                                        l2 = len(ins[4])
                                        aux1 = ins[2][1:l1]
                                        aux2 = ins[2][1:l2]
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4][0] == '$':#Bin - Hex
                                        l1 = len(ins[2])
                                        aux1 = ins[2][1:l1]
                                        aux2 = hexa_transform(ins[4])
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4].isdigit(): #Bin - Digito
                                        aux1 = ins[2][1:l1]
                                        aux2 = bin_trasnform(ins[4])
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    else: #Bin - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce') #Error
                                        return respuesta
                                    if ins[7] in dic2:
                                        aux3 = dic2[ins[7]]
                                        respuesta.append(aux3) #
                                        return respuesta
                                    elif ins[7][0] =='%':
                                        l = len(ins[7])
                                        aux3 = ins[7][1:l]
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[7][0] =='$':
                                        aux3 = hexa_transform(ins[2])
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[7].isdigit():
                                        aux3 = bin_trasnform(ins[7])
                                        respuesta.append(aux3)
                                        return respuesta
                                    else:
                                        respuesta=[]
                                        respuesta.append(0)
                                        respuesta.append('Segundo parametro erroneo')
                                        return respuesta
                                elif ins[2][0] == '$':
                                    if ins[4][0] == '%': #Hex - Bin
                                        aux1 = hexa_transform(ins[2])
                                        l2 = len(ins[4])
                                        aux2 = ins[4][1:l2]
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4][0] == '$':# Hex - Hex
                                        aux1 = hexa_transform(ins[2])
                                        aux2 = hexa_transform(ins[4])
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4].isdigit(): #Hex - Digito
                                        aux1 = hexa_transform(ins[2])
                                        aux2 = bin_trasnform(ins[4])
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    else: #Hex - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce')
                                        return respuesta
                                    if ins[7] in dic2:
                                        aux3 = dic2[ins[7]]
                                        respuesta.append(aux3) #
                                        return respuesta
                                    elif ins[7][0] =='%':
                                        l = len(ins[7])
                                        aux3 = ins[7][1:l]
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[7][0] =='$':
                                        aux3 = hexa_transform(ins[2])
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[7].isdigit():
                                        aux3 = bin_trasnform(ins[7])
                                        respuesta.append(aux3)
                                        return respuesta
                                    else:
                                        respuesta=[]
                                        respuesta.append(0)
                                        respuesta.append('Segundo parametro erroneo')
                                        return respuesta
                                elif ins[2].isdigit():
                                    if ins[4][0] == '%': #Digito - Bin
                                        aux1 = bin_trasnform(ins[2])
                                        l2 = len(ins[4])
                                        aux2 = ins[4][1:l2]
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4][0] == '$':# Digito - Hex
                                        aux1 = bin_trasnform(ins[2])
                                        aux2 = hexa_transform(ins[4])
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4].isdigit(): #Digito - Digito
                                        aux1 = bin_trasnform(ins[2])
                                        aux2 = bin_trasnform(ins[4])
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario 1
                                    else: #Hex - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce')
                                        return respuesta
                                    if ins[7] in dic2:
                                        aux3 = dic2[ins[7]]
                                        respuesta.append(aux3) #
                                        return respuesta
                                    elif ins[7][0] =='%':
                                        l = len(ins[7])
                                        aux3 = ins[7][1:l]
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[7][0] =='$':
                                        aux3 = hexa_transform(ins[2])
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[7].isdigit():
                                        aux3 = bin_trasnform(ins[7])
                                        respuesta.append(aux3)
                                        return respuesta
                                    else:
                                        respuesta=[]
                                        respuesta.append(0)
                                        respuesta.append('Segundo parametro erroneo')
                                        return respuesta

                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('El primer valor no se reconoce')
                                    #print ('Comando invalido')
                                    return respuesta
                        else:
                            respuesta.append(0)
                            respuesta.append('Operador invalido')
                            #print ('Comando invalido')
                    else:
                        respuesta.append(0)
                        respuesta.append('Se espera cierre')
                        #print ('Se espera un cierre ')
                elif ins[3] == '(' or ins[3] == '[':
                    if ins[7] == ')' or ins[7] == ']':
                        if ins[5] == '+':
                            if ins[6] in dic2 and ins[4] in dic2: #Si ambos estan en reg
                                aux1 = dic2[ins[6]]
                                aux2 = dic2[ins[4]]
                                res=add_registros(aux1, aux2)
                                respuesta.append(1) # Flag
                                respuesta.append(ins[0]) # Opcode
                                respuesta.append(res) # resultado suma
                                if ins[1] in dic2:
                                    aux3 = dic2[ins[1]]
                                    respuesta.append(aux3) #
                                    return respuesta
                                elif ins[1][0] =='%':
                                    l = len(ins[1])
                                    aux3 = ins[1][1:l]
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[1][0] =='$':
                                    aux3 = hexa_transform(ins[1])
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[1].isdigit():
                                    aux3 = bin_trasnform(ins[1])
                                    respuesta.append(aux3)
                                    return respuesta
                                else:
                                    respuesta=[]
                                    respuesta.append(0)
                                    respuesta.append('Segundo parametro erroneo')
                                    return respuesta
                            elif ins[6] not in dic2 and ins[4] in dic2: #Si solo esta el reg 2
                                if ins[6][0] == '%':#Binario
                                    l = len(ins[6])
                                    aux1 = ins[6][1:l]
                                    aux2 = dic2[ins[4]]
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) # Binario suma
                                elif ins[6][0] == '$': #hexadecimal
                                    aux1 = hexa_transform(ins[6])
                                    aux2 = dic2[ins[4]]
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) #flag
                                    respuesta.append(ins[0]) #opcode
                                    respuesta.append(res) #binario suma
                                elif ins[6].isdigit():
                                    aux1 = bin_trasnform(ins[6])
                                    aux2 = dic2[ins[4]]
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) # flag
                                    respuesta.append(ins[0]) # opcode
                                    respuesta.append(res) # binario suma
                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('Primer parametro invalido')#Error
                                    #print ('Comando invalido')
                                if ins[1] in dic2:
                                    aux3 = dic2[ins[1]]
                                    respuesta.append(aux3) #
                                    return respuesta
                                elif ins[1][0] =='%':
                                    l = len(ins[1])
                                    aux3 = ins[1][1:l]
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[1][0] =='$':
                                    aux3 = hexa_transform(ins[1])
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[1].isdigit():
                                    aux3 = bin_trasnform(ins[1])
                                    respuesta.append(aux3)
                                    return respuesta
                                else:
                                    respuesta=[]
                                    respuesta.append(0)
                                    respuesta.append('Segundo parametro erroneo')
                                    return respuesta
                            elif ins[4] not in dic2 and ins[6] in dic2: #Si solo esta el reg 1
                                if ins[4][0] == '%': #Binario
                                    aux1 = dic2[ins[6]]
                                    l = len(ins[4])
                                    aux = ins[4][1:l]
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Resultado suma
                                elif ins[4][0] == '$': #hexadecimal
                                    aux1 = dic2[ins[6]]
                                    aux2 = hexa_transform(ins[4])
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) # Opcode
                                    respuesta.append(res) #Resultado suma
                                elif ins[4].isdigit(): #Digito
                                    aux1 = dic2[ins[6]]
                                    aux2 = bin_trasnform(ins[4])
                                    res=add_registros(aux1, aux2)
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) # Opcode
                                    respuesta.append(res) #Resultado suma
                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('Segundo parametro invalido')#Error
                                    #print ('Comando invalido')
                                    return respuesta
                                if ins[1] in dic2:
                                    aux3 = dic2[ins[1]]
                                    respuesta.append(aux3) #
                                    return respuesta
                                elif ins[1][0] =='%':
                                    l = len(ins[1])
                                    aux3 = ins[1][1:l]
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[1][0] =='$':
                                    aux3 = hexa_transform(ins[1])
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[1].isdigit():
                                    aux3 = bin_trasnform(ins[1])
                                    respuesta.append(aux3)
                                    return respuesta
                                else:
                                    respuesta=[]
                                    respuesta.append(0)
                                    respuesta.append('Segundo parametro erroneo')
                                    return respuesta
                            else: #Si ninguno esta en REG
                                if ins[6][0] == '%':
                                    if ins[4][0] == '%':# Bin - Bin
                                        l1 = len(ins[6])
                                        l2 = len(ins[4])
                                        aux1 = ins[6][1:l1]
                                        aux2 = ins[6][1:l2]
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4][0] == '$':#Bin - Hex
                                        l1 = len(ins[6])
                                        aux1 = ins[6][1:l1]
                                        aux2 = hexa_transform(ins[4])
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4].isdigit(): #Bin - Digito
                                        aux1 = ins[6][1:l1]
                                        aux2 = bin_trasnform(ins[4])
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    else: #Bin - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce') #Error
                                        return respuesta
                                    if ins[1] in dic2:
                                        aux3 = dic2[ins[1]]
                                        respuesta.append(aux3) #
                                        return respuesta
                                    elif ins[1][0] =='%':
                                        l = len(ins[1])
                                        aux3 = ins[1][1:l]
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[1][0] =='$':
                                        aux3 = hexa_transform(ins[1])
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[1].isdigit():
                                        aux3 = bin_trasnform(ins[1])
                                        respuesta.append(aux3)
                                        return respuesta
                                    else:
                                        respuesta=[]
                                        respuesta.append(0)
                                        respuesta.append('Segundo parametro erroneo')
                                        return respuesta
                                elif ins[6][0] == '$':
                                    if ins[4][0] == '%': #Hex - Bin
                                        aux1 = hexa_transform(ins[6])
                                        l2 = len(ins[4])
                                        aux2 = ins[4][1:l2]
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4][0] == '$':# Hex - Hex
                                        aux1 = hexa_transform(ins[6])
                                        aux2 = hexa_transform(ins[4])
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4].isdigit(): #Hex - Digito
                                        aux1 = hexa_transform(ins[6])
                                        aux2 = bin_trasnform(ins[4])
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    else: #Hex - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce')
                                        return respuesta
                                    if ins[1] in dic2:
                                        aux3 = dic2[ins[1]]
                                        respuesta.append(aux3) #
                                        return respuesta
                                    elif ins[1][0] =='%':
                                        l = len(ins[1])
                                        aux3 = ins[1][1:l]
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[1][0] =='$':
                                        aux3 = hexa_transform(ins[1])
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[1].isdigit():
                                        aux3 = bin_trasnform(ins[1])
                                        respuesta.append(aux3)
                                        return respuesta
                                    else:
                                        respuesta=[]
                                        respuesta.append(0)
                                        respuesta.append('Segundo parametro erroneo')
                                        return respuesta
                                elif ins[6].isdigit():
                                    if ins[4][0] == '%': #Digito - Bin
                                        aux1 = bin_trasnform(ins[6])
                                        l2 = len(ins[4])
                                        aux2 = ins[4][1:l2]
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4][0] == '$':# Digito - Hex
                                        aux1 = bin_trasnform(ins[6])
                                        aux2 = hexa_transform(ins[4])
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4].isdigit(): #Digito - Digito
                                        aux1 = bin_trasnform(ins[6])
                                        aux2 = bin_trasnform(ins[4])
                                        res=add_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario 1
                                    else: #Hex - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce')
                                        return respuesta
                                    if ins[1] in dic2:
                                        aux3 = dic2[ins[1]]
                                        respuesta.append(aux3) #
                                        return respuesta
                                    elif ins[1][0] =='%':
                                        l = len(ins[1])
                                        aux3 = ins[1][1:l]
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[1][0] =='$':
                                        aux3 = hexa_transform(ins[1])
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[1].isdigit():
                                        aux3 = bin_trasnform(ins[1])
                                        respuesta.append(aux3)
                                        return respuesta
                                    else:
                                        respuesta=[]
                                        respuesta.append(0)
                                        respuesta.append('Segundo parametro erroneo')
                                        return respuesta

                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('El primer valor no se reconoce')
                                    #print ('Comando invalido')
                                    return respuesta

                        elif ins[5] == '-':
                            if ins[6] in dic2 and ins[4] in dic2: #Si ambos estan en reg
                                aux1 = dic2[ins[6]]
                                aux2 = dic2[ins[4]]
                                res=res_registros(aux1, aux2)
                                respuesta.append(1) # Flag
                                respuesta.append(ins[0]) # Opcode
                                respuesta.append(res) # resultado suma
                                if ins[1] in dic2:
                                    aux3 = dic2[ins[1]]
                                    respuesta.append(aux3) #
                                    return respuesta
                                elif ins[1][0] =='%':
                                    l = len(ins[1])
                                    aux3 = ins[1][1:l]
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[1][0] =='$':
                                    aux3 = hexa_transform(ins[1])
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[1].isdigit():
                                    aux3 = bin_trasnform(ins[1])
                                    respuesta.append(aux3)
                                    return respuesta
                                else:
                                    respuesta=[]
                                    respuesta.append(0)
                                    respuesta.append('Segundo parametro erroneo')
                                    return respuesta
                            elif ins[6] not in dic2 and ins[4] in dic2: #Si solo esta el reg 2
                                if ins[6][0] == '%':#Binario
                                    l = len(ins[6])
                                    aux1 = ins[6][1:l]
                                    aux2 = dic2[ins[4]]
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) # Binario suma
                                elif ins[6][0] == '$': #hexadecimal
                                    aux1 = hexa_transform(ins[6])
                                    aux2 = dic2[ins[4]]
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) #flag
                                    respuesta.append(ins[0]) #opcode
                                    respuesta.append(res) #binario suma
                                elif ins[6].isdigit():
                                    aux1 = bin_trasnform(ins[6])
                                    aux2 = dic2[ins[4]]
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) # flag
                                    respuesta.append(ins[0]) # opcode
                                    respuesta.append(res) # binario suma
                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('Primer parametro invalido')#Error
                                    #print ('Comando invalido')
                                if ins[1] in dic2:
                                    aux3 = dic2[ins[1]]
                                    respuesta.append(aux3) #
                                    return respuesta
                                elif ins[1][0] =='%':
                                    l = len(ins[1])
                                    aux3 = ins[1][1:l]
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[1][0] =='$':
                                    aux3 = hexa_transform(ins[1])
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[1].isdigit():
                                    aux3 = bin_trasnform(ins[1])
                                    respuesta.append(aux3)
                                    return respuesta
                                else:
                                    respuesta=[]
                                    respuesta.append(0)
                                    respuesta.append('Segundo parametro erroneo')
                                    return respuesta
                            elif ins[4] not in dic2 and ins[6] in dic2: #Si solo esta el reg 1
                                if ins[4][0] == '%': #Binario
                                    aux1 = dic2[ins[6]]
                                    l = len(ins[4])
                                    aux = ins[4][1:l]
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) #Flag
                                    respuesta.append(ins[0]) #Opcode
                                    respuesta.append(res) #Resultado suma
                                elif ins[4][0] == '$': #hexadecimal
                                    aux1 = dic2[ins[6]]
                                    aux2 = hexa_transform(ins[4])
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) # Opcode
                                    respuesta.append(res) #Resultado suma
                                elif ins[4].isdigit(): #Digito
                                    aux1 = dic2[ins[6]]
                                    aux2 = bin_trasnform(ins[4])
                                    res=res_registros(aux1, aux2)
                                    respuesta.append(1) # Flag
                                    respuesta.append(ins[0]) # Opcode
                                    respuesta.append(res) #Resultado suma
                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('Segundo parametro invalido')#Error
                                    #print ('Comando invalido')
                                    return respuesta
                                if ins[1] in dic2:
                                    aux3 = dic2[ins[1]]
                                    respuesta.append(aux3) #
                                    return respuesta
                                elif ins[1][0] =='%':
                                    l = len(ins[1])
                                    aux3 = ins[1][1:l]
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[1][0] =='$':
                                    aux3 = hexa_transform(ins[1])
                                    respuesta.append(aux3)
                                    return respuesta
                                elif ins[1].isdigit():
                                    aux3 = bin_trasnform(ins[1])
                                    respuesta.append(aux3)
                                    return respuesta
                                else:
                                    respuesta=[]
                                    respuesta.append(0)
                                    respuesta.append('Segundo parametro erroneo')
                                    return respuesta
                            else: #Si ninguno esta en REG
                                if ins[6][0] == '%':
                                    if ins[4][0] == '%':# Bin - Bin
                                        l1 = len(ins[6])
                                        l2 = len(ins[4])
                                        aux1 = ins[6][1:l1]
                                        aux2 = ins[6][1:l2]
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4][0] == '$':#Bin - Hex
                                        l1 = len(ins[6])
                                        aux1 = ins[6][1:l1]
                                        aux2 = hexa_transform(ins[4])
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4].isdigit(): #Bin - Digito
                                        aux1 = ins[6][1:l1]
                                        aux2 = bin_trasnform(ins[4])
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    else: #Bin - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce') #Error
                                        return respuesta
                                    if ins[1] in dic2:
                                        aux3 = dic2[ins[1]]
                                        respuesta.append(aux3) #
                                        return respuesta
                                    elif ins[1][0] =='%':
                                        l = len(ins[1])
                                        aux3 = ins[1][1:l]
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[1][0] =='$':
                                        aux3 = hexa_transform(ins[1])
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[1].isdigit():
                                        aux3 = bin_trasnform(ins[1])
                                        respuesta.append(aux3)
                                        return respuesta
                                    else:
                                        respuesta=[]
                                        respuesta.append(0)
                                        respuesta.append('Segundo parametro erroneo')
                                        return respuesta
                                elif ins[6][0] == '$':
                                    if ins[4][0] == '%': #Hex - Bin
                                        aux1 = hexa_transform(ins[6])
                                        l2 = len(ins[4])
                                        aux2 = ins[4][1:l2]
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4][0] == '$':# Hex - Hex
                                        aux1 = hexa_transform(ins[6])
                                        aux2 = hexa_transform(ins[4])
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4].isdigit(): #Hex - Digito
                                        aux1 = hexa_transform(ins[6])
                                        aux2 = bin_trasnform(ins[4])
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    else: #Hex - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce')
                                        return respuesta
                                    if ins[1] in dic2:
                                        aux3 = dic2[ins[1]]
                                        respuesta.append(aux3) #
                                        return respuesta
                                    elif ins[1][0] =='%':
                                        l = len(ins[1])
                                        aux3 = ins[1][1:l]
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[1][0] =='$':
                                        aux3 = hexa_transform(ins[1])
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[1].isdigit():
                                        aux3 = bin_trasnform(ins[1])
                                        respuesta.append(aux3)
                                        return respuesta
                                    else:
                                        respuesta=[]
                                        respuesta.append(0)
                                        respuesta.append('Segundo parametro erroneo')
                                        return respuesta
                                elif ins[6].isdigit():
                                    if ins[4][0] == '%': #Digito - Bin
                                        aux1 = bin_trasnform(ins[6])
                                        l2 = len(ins[4])
                                        aux2 = ins[4][1:l2]
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4][0] == '$':# Digito - Hex
                                        aux1 = bin_trasnform(ins[6])
                                        aux2 = hexa_transform(ins[4])
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario suma
                                    elif ins[4].isdigit(): #Digito - Digito
                                        aux1 = bin_trasnform(ins[6])
                                        aux2 = bin_trasnform(ins[4])
                                        res=res_registros(aux1, aux2)
                                        respuesta.append(1) #Flag
                                        respuesta.append(ins[0]) #Opcode
                                        respuesta.append(res) #Binario 1
                                    else: #Hex - Desconocido
                                        respuesta.append(0) #Flag
                                        respuesta.append('El segundo valor no se reconoce')
                                        return respuesta
                                    if ins[1] in dic2:
                                        aux3 = dic2[ins[1]]
                                        respuesta.append(aux3) #
                                        return respuesta
                                    elif ins[1][0] =='%':
                                        l = len(ins[1])
                                        aux3 = ins[1][1:l]
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[1][0] =='$':
                                        aux3 = hexa_transform(ins[1])
                                        respuesta.append(aux3)
                                        return respuesta
                                    elif ins[1].isdigit():
                                        aux3 = bin_trasnform(ins[1])
                                        respuesta.append(aux3)
                                        return respuesta
                                    else:
                                        respuesta=[]
                                        respuesta.append(0)
                                        respuesta.append('Segundo parametro erroneo')
                                        return respuesta

                                else:
                                    respuesta.append(0) #Flag
                                    respuesta.append('El primer valor no se reconoce')
                                    #print ('Comando invalido')
                                    return respuesta

                        else:
                            respuesta.append(0)
                            respuesta.append('operador invalido')
                            return respuesta
                            #print ('Comando invalido')
                    else:
                        respuesta.append(0)
                        respuesta.append('Se espera un cierre')
                        #print ('Se espera un cierre ')
                else:
                    respuesta.append(0)
                    respuesta.append('Comando invalido verifique la instruccion')
                    #print ('Comando invalido verifique la instruccion')
            #Fin len 8
            else:
                respuesta.append(0)
                respuesta.append('Verifique la instruccion ')
                #print ('Verifique la instruccion ')
        else:
            respuesta.append(0)
            respuesta.append('Instruccion no valida')
            #print ('Instruccion no valida')
    else:
        respuesta.append(0)
        respuesta.append('ingrese un comando')

#-----------------------------
# Ejemplo de base
#-----------------------------

"""
def suma(a,b):
    return a+b
def resta(arg):
    return arg-1

var1=int(input('ingrese un numero'))
var2=3
arg=6
dic={'1':suma(var1,var2),'2':resta(arg),'3':'hola'}
print('diccionario de funciones', dic['1'])

def fun_dic_para(dicci):
    if '3' in dicci:
        print('dicci', dicci['3'])
    print("funcion con dic de parametro", dicci['2'])

fun_dic_para(dic)
"""
