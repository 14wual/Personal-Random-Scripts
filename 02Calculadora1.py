#Variables Globales
from xml.etree.ElementTree import Element


global operador
global elemento
global igual
global ultimo_resultado


def calculadora():

    #Variables Por defecto
    resultado = 0
    igual = False
    ronda = 0

    while igual == False:

        if ronda == 0:
            ultimo_resultado = int(input("Escribe: "))
            operador = input("Operador: ")
            elemento = int(input("Escribe: "))
            ronda += 1
        elif ronda != 0:
            operador = input("Operador: ")
            elemento = int(input("Escribe: "))
            
        if operador == '=':
            igual = True
        elif operador == '+':
            ultimo_resultado = ultimo_resultado + elemento
        elif operador == '-':
            ultimo_resultado = ultimo_resultado - elemento
        elif operador == '*' or 'x' or 'X':
            ultimo_resultado = ultimo_resultado * elemento
        elif operador == '/':
            resultado = ultimo_resultado / elemento
        else:
                print('Operador incorrecto, use [+],[-],[*] o [/]')

        
    else:
        resultado = ultimo_resultado
        print(resultado)

if __name__ == '__main__':
    calculadora()