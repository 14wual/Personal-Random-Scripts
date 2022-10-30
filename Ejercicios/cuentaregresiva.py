#Temporizador con Barra de Progreso
from time import sleep
from tqdm.auto import tqdm

def vars():
    global tiempo_horas
    global tiempo_minutos
    global tiempo_segundos

    tiempo_segundos = int(input("Segundos: "))
    tiempo_minutos = int(input("Minutos: "))
    tiempo_horas = int(input("Horas: "))

def regre():

    global tiempo_horas
    global tiempo_minutos
    global tiempo_segundos

    global tiempo
    tiempo = 0

    print (f"Temporizador: {tiempo}s\n{tiempo_horas}Horas / {tiempo_minutos}Minutos / {tiempo_segundos}Segundos")
    print("\n")

    if tiempo_horas > 0:
        tiempo_horas = tiempo_horas * 3600
        tiempo += tiempo_horas
    if tiempo_minutos > 0:
        tiempo_minutos = tiempo_minutos * 60
        tiempo += tiempo_minutos
    if tiempo_segundos > 0:
        tiempo += tiempo_segundos    

    print("Temporizador empezará en:")
    temp = 3
    for i in range(temp):
        temp -=1
        print(temp,end='\r')
        sleep(1)
    
    print("\n")
    
def progr():

    global tiempo

    for i in tqdm(range(tiempo)):
        print("",end='\r')
        sleep(1)

if __name__ == '__main__':
    vars()
    regre()
    progr()
