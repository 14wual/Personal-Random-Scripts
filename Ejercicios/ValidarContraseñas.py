#Validador de contraseñas
import random

global carácteres
global lista_carácteres 

carácteres = "ºª!|·#$%&¬/()=?¿¡.:-_,;*{,}ç^[+]"
lista_carácteres = ("º","ª","!","|","·",",","$","%","&","¬","/","(",")","=","?","¿","¡",".",":","-","_",";","*","{","}","ç","^","[","+","]<")

def api():
    global carácteres

    usser_pass = input("Introduzca su contraseña: ")

    if usser_pass.isalpha() == True:
        if usser_pass.islower() == True:
            print("Su contraseña no es segura.\nNo valla por la vida con minúsculas.\nLe sugerimos esta nueva contraseña:")
            passgenerator()
        elif usser_pass.isupper() == True:
            print("Su contraseña no es segura.\nNo valla por la vida con mayúsculas.\nLe sugerimos esta nueva contraseña:")
            passgenerator()
        else:
            print("Aunque goce de Mayúsculas y minúsuclas, su contraseña no es segura.\nLe sugerimos esta nueva contraseña:")
            passgenerator()
    elif usser_pass.isdigit() == True:
        print("Su contraseña no es segura.\nNo valla por la vida con números.\nLe sugerimos esta nueva contraseña:")
        passgenerator()
    else:
        nums = 0
        for n in usser_pass:
            nums += 1
        if nums <= 10:
            print("Su contraseña es demasiado corta.\nLe sugerimos esta nueva contraseña:")
            passgenerator()
        else:
            iscar = False
            #True and usser_pass in carácteres
            for n in usser_pass: 
                if n in lista_carácteres :
                    iscar = True
            if iscar == True:
                print("Usted tiene una contraseña segura")


def passgenerator():
    
    minusculas = "abcdefghijklmnñopqrstuvwxyz"
    mayúsculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    numeros = "0123456789"
    global carácteres
    
    lista = mayúsculas+minusculas+numeros+carácteres
    longitud = 12
    
    longitud

    contraseña = ""

    for s in range(longitud):
        a = random.choice(str(lista))
        contraseña += a
    
    print(contraseña)

if __name__ == '__main__':
    api()
