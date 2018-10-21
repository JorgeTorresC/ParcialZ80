# -*- coding: utf-8 -*-
# *************************
# 21 De Octubre del 2018
# Emulador Procesador Z80
# Jorge Ivan Torres
# Daniel Caita
# *************************

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
    if len(ins) > 0:
        if ins[0] in dic1:
            if len(ins) == 1:
                #Llamar diccionario de funciones, operar
            elif len(ins) == 2:
                if ins[1] in dic2:
                    #Llamar diccionario de funciones, operar
                else:
                    if ins[1][0] == '%' or ins[1][0] == '$':
                        #trasformar a binario, operar
                    else:
                        print ('Comando invalido')
            elif len(ins) == 4:
                if ins[2] == ',':
                    #Llamar diccionario de funciones, operar
                else:
                    print ('Separador no valido')
            elif len(ins) == 6:
                if ins[2] == ',' or ins[4] == ',':
                    if ins[1] == '(' or ins[1] == '[':
                        if ins[3] == ')' or ins[3] == ']' :
                            #Llamar diccionario de funciones, operar
                            #llamar funcion de cargado especial en memoria
                        else:
                            print ("Se espera un cierre ")
                    elif ins[3] == '(' or ins[3] == '[':
                        if ins[5] == ')' or ins[5] == ']':
                            #Llamar diccionario de funciones, operar
                            #llamar funcion de cargado especial en memoria
                        else:
                            print ("Se espera un cierre ")
                elif ins[3] == '+' or ins[3] == '-':
                    # opera entre a y b
                    # luego llama a la instricción como si fuera tipo ( opc var )
                else:
                    print ('Comando invalido')
            elif len(ins) == 8:
        else:
            print ('Instruccion no valida')

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
