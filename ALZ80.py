"""
UNIVERSIDAD NACIONAL DE COLOMBIA
Analizador Z80
SAb,20 de Oct
Jorge Ivan Torres Candia
Daniel Caita
"""
import sys

#Diccionario de operadores especiales
dic_operadores = {
    '(':'token_par_izq',
    ')':'token_par_der',
    '[':'token_cor_izq',
    ']':'token_cor_der',
    '+':'token_mas',
    '=':'token_igual',
    '-':'token_menos',
    '%':'token_base2',
    ';':'token_punto_y_coma',
    ',':'token_coma',
    "'":'token_apostrofe',
    '$':'token_pesos'
}

#Diccionario de las palabras reservadas del lenguaje
dicPalabrasreservadas = {
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

#Diccionario de Letras del alfabeto mayusculas
Abc =['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#Diccionario de numeros
Numero = ['0','1','2','3','4','5','6','7','8','9']


#Funcion para concatenar la respuesta
#Recibe una serie de strings y retorna el string resultante de la concatenacion
def do_answer(s1, s2, s3, s4, s5):
    answer = s1
    answer += s2
    answer += s3
    answer += s4
    answer += s5
    return answer


#clasifica los tokens posibles, si no pertenece a ninguna categoria se considera error lexico
def tipo(w):
    aux = ''
    if w in dic_operadores:
        return "token_operadores"
    elif w in dicPalabrasreservadas:
        return "token_palabras"
    elif w == " ":
        return "espacio"
    elif w == "":
        return "vacio"
    elif w.isdigit():
        return "Num_entero"
    elif w.find('"') != -1:
        return "String"
    elif w.isalpha(): # True si "pepegrillo"
        return "Id"
    elif w.isalnum(): #True si "pepegrillo75"
        if w[0] in Numero:
            return "Error_Lexico"
        else:
            return "Id"
    elif w[0] == '$':
        return "Num_Hexadecimal"
    else:
        return "Error_Lexico"

#Revisa la lista de posibles tokens
#mirando el tipo de token que puede llegar a ser el objeto en la lista,
#Imprime en pantalla el tipo de token que clasifica
def Lexema( l ):
    global itx #Instruccion a ejecutar
    aux = ''
    answer = ''
    col = 1
    flag = False
    for i in l:
        #Ignora los comentarios
        if i == ";":
            break

        w = tipo(i)
        if w == "token_operadores":
            itx.append(dic_operadores[i])
        elif w == "token_palabras":
            itx.append(dicPalabrasreservadas[i])
        elif w == "Num_entero":
            itx.append(i)
        elif w == "Id":
            itx.append(i)
        elif w == "Num_Hexadecimal":
            itx.append(i)
        elif w == "Error_Lexico":
            answer = ">>> Error lexico"
            flag = True
    if flag == False:
        return 1
    else:
        return -1

#Leer caracter por caracter
#Separa los tokens por espacio o por aparicion de palabras reservadas u operadores
#Genera una lista de posibles tokens por cada linea
def lector (linea):
    string_Temporal = ''
    flag_string = False
    l=list()
    for i in linea:
        #print (i)
        if i == "\n" or i == "\t":
            if string_Temporal != '':
                l.append(string_Temporal)
            string_Temporal = ''

        if flag_string == True:
            string_Temporal += i
        else:
            if i == " ":
                if string_Temporal != '':
                    l.append(string_Temporal)
                    string_Temporal = ''
                #l.append(" ")
            elif i in dic_operadores:
                if i == '$':
                    string_Temporal += i
                    continue
                else:
                    l.append(string_Temporal)
                    string_Temporal = ''
                    l.append(i)
            elif string_Temporal.find('$') != -1 and i.isdigit():
                string_Temporal += i
            elif string_Temporal in dic_operadores:
                l.append(string_Temporal)
                string_Temporal = ''
                string_Temporal += i
            elif ( not( i.isdigit() ) ) and string_Temporal.isdigit() and string_Temporal != '':
                l.append(string_Temporal)
                string_Temporal = ''
                string_Temporal += i
            elif ( i.isdigit() )  and string_Temporal.isdigit() and string_Temporal != '':
                string_Temporal += i
            elif i not in Abc and i not in Numero:
                l.append(string_Temporal)
                string_Temporal = ''
                string_Temporal += i

            else:
                string_Temporal +=i
    if string_Temporal != '' and string_Temporal !='\n':
        l.append(string_Temporal)
        string_Temporal = ''
    return l

#Main del programa
"""
instr = sys.stdin.readlines()
aux=instr
l=lector(aux)
print(len(aux))
print(l)
Lexema(l)
"""
