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
    ',':'token_coma'
}

#Diccionario de las palabras reservadas del lenguaje
dicPalabrasreservadas = {
    'ADC':'true',
    'ADD':'false',
    'AND':'nil',
    'BIT':'if',
    'CALL':'else',
    'CCF':'while',
    'CP':'log',
    'CPD':'for',
    'CPDR':'funcion',
    'CPI':'end',
    'CPIR':'retorno',
    'CPL':'importar',
    'DAA':'desde',
    'DEC':"todo",
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
Abc =['A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#Diccionario de numeros
Numero = ['0','1','2','3','4','5','6','7','8','9']


#Funcion para concatenar la respuesta
#Recibe una serie de strings y retorna el string resultante de la concatenacion
def do_answer(s1, s2, s3, s4, s5, s6, s7):
    answer = s1
    answer += s2
    answer += s3
    answer += s4
    answer += s5
    answer += s6
    answer += s7
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
    elif isfloat(w) == 1:
        return "Num_flotante"
    elif w.isalpha(): # True si "pepegrillo"
        return "Id"
    elif w.isalnum(): #True si "pepegrillo75"
        if w[0] in Numero:
            return "Error_Lexico"
        else:
            return "Id"
    else:
        return "Error_Lexico"

#Revisa la lista de posibles tokens
#mirando el tipo de token que puede llegar a ser el objeto en la lista,
#Imprime en pantalla el tipo de token que clasifica
def Lexema( l, fil ):
    aux = ''
    answer = ''
    col = 1
    flag = False
    for i in l:
        if i == "#":
            fil = fil + 1
            break
        w = tipo(i)
        if w == "token_operadores":
            answer = do_answer('<', dic_operadores[i], ',' ,str(fil), ',', str(col), '>')
            print (answer)
            col=col+len(i)
        elif w == "token_palabras":
            answer = do_answer('<', dicPalabrasreservadas[i], ',' ,str(fil), ',', str(col), '>')
            print(answer)
            col=col+len(i)
        elif w == "Num_entero":
            answer = do_answer('<token_integer,', i, ',' ,str(fil), ',', str(col), '>')
            print(answer)
            col=col+len(i)
        elif w == "String":
            aux = i.split('"')
            answer = do_answer('<token_string,', aux[1], ',' ,str(fil), ',', str(col), '>')
            print(answer)
            col = col + len(i)
        elif w == "Num_flotante":
            answer = do_answer('<token_float,', i, ',' ,str(fil), ',', str(col), '>')
            print(answer)
            col=col+len(i)
        elif w == "Id":
            answer = do_answer('<id,', i, ',' ,str(fil), ',', str(col), '>')
            print(answer)
            col=col+len(i)
        elif w == "Error_Lexico":
            answer = ">>> Error lexico(linea:"
            answer += str(fil)
            answer += ',posicion:'
            answer += str(col)
            answer += ')'
            print(answer)
            flag = True
        elif w == "espacio":
            col=col+1
    if flag == False:
        return 1
    else:
        return -1

#Leer caracter por caracter
#Separa los tokens por espacio o por aparicion de palabras reservadas u operadores
#Genera una lista de posibles tokens por cada linea

def lector (linea):
    linea.lower()
    string_Temporal = ''
    flag_string = False
    l=list()
    for i in linea:
        if flag_string == True:
            string_Temporal += i
        else:
            if i == " ":
                l.append(string_Temporal)
                string_Temporal = ''
                l.append(" ")
            elif i in dic_operadores:
                if string_Temporal != '' and string_Temporal not in dic_operadores:
                    if string_Temporal.isdigit() and i == '.':
                        string_Temporal += i
                        continue
                    else:
                        l.append(string_Temporal)
                        string_Temporal = ''
                elif string_Temporal != '' and string_Temporal in dic_operadores:
                    if (string_Temporal + i) in dic_operadores:
                        string_Temporal += i
                        l.append(string_Temporal)
                        string_Temporal = ''
                        continue
                    else:
                        l.append(string_Temporal)
                        string_Temporal = ''
                string_Temporal += i
                continue
            elif (string_Temporal in dic_operadores) and string_Temporal != "in":
                l.append(string_Temporal)
                string_Temporal = ''
                string_Temporal += i
            elif ( not( i.isdigit() ) ) and string_Temporal.isdigit() and string_Temporal != '':
                l.append(string_Temporal)
                string_Temporal = ''
                string_Temporal += i
            elif ( i.isdigit() )  and string_Temporal.isdigit() and string_Temporal != '':
                string_Temporal += i
            elif isfloat(string_Temporal)==1 and ( not( i.isdigit() ) and string_Temporal != ''):
                l.append(string_Temporal)
                string_Temporal = ''
                string_Temporal += i
            elif (string_Temporal + i) in dic_operadores:
                string_Temporal += i
                l.append(string_Temporal)
                string_Temporal = ''
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

instr = sys.stdin.readlines()
l=lector(instr)
if Lexema(l,num_columna) == -1:
    break
num_columna = num_columna + 1
