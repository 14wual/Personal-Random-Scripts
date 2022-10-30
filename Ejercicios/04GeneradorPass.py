#Generador de contraseñas

import random


minusculas = "abcdefghijklmnñopqrstuvwxyz"
mayúsculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "0123456789"
carácteres = "ºª!|·#$%&¬/()=?¿¡.:-_,;*{,}ç^[+]"

longitud = 0
nivel_seguridad = 0
nivel_elegido = 0
global lista

def personalización():
    global minusculas
    global mayúsculas
    global numeros
    global carácteres
    global lista

    global longitud

    global nivel_seguridad
    global nivel_elegido


    print("Ahora se le hará una serie de preguntas de cómo quiere su contraseña")

    
    longitud = int(input("Longitud de la CONTRASEÑA: "))

    if longitud > 20:
        print("El máximo de caráceres es de 20")
        longitud = int(input("Longitud de la CONTRASEÑA: "))
    elif longitud <= 0:
        print("El máximo de caráceres es de 20")
        longitud = int(input("Longitud de la CONTRASEÑA: "))

    nivel_seguridad = int(input("Eliga un número del 1 al 3 dependiendo del nivel de seguridad de su contraseña: "))

    if nivel_seguridad >= 4:
        print("Eliga entre estas opciones: \n    Nivel 1. Mayúsculas y Minúsculas\n    Nivel 2. Anterior + Números \n    Nivel 3. Anterior + Carácteres")
        nivel_seguridad = int(input("Eliga un número del 1 al 3 dependiendo del nivel de seguridad de su contraseña: "))
    elif nivel_seguridad <= 0:
        print("Eliga entre estas opciones: \n    Nivel 1. Mayúsculas y Minúsculas\n    Nivel 2. Anterior + Números \n    Nivel 3. Anterior + Carácteres")
        nivel_seguridad = int(input("Eliga un número del 1 al 3 dependiendo del nivel de seguridad de su contraseña: "))

    if nivel_seguridad == 1:
        lista = mayúsculas+minusculas
    elif nivel_seguridad == 2:
        lista = mayúsculas+minusculas+numeros
    elif nivel_seguridad == 3:
        lista = mayúsculas+minusculas+numeros+carácteres

def generar_password():
    global lista
    global longitud

    contraseña = ""

    for s in range(longitud):
        a = random.choice(str(lista))
        contraseña += a
    
    print(contraseña)

if __name__ == '__main__':
    personalización()
    generar_password()
