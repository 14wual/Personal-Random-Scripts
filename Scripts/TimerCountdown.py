# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

#What's this?
#This script is a Progressive Bar Timer


#Requirements: 
    #Install the requirements (at the terminal) to run this program
        #pip install random tqdm

#Enjoyment!

#Temporizador con Barra de Progres
from time import sleep
from tqdm.auto import tqdm

#Function with all variables
def vars():
    global time_hours
    global time_minutes
    global time_seconds

    #In these variables we indicate to the program the time we want our timer to take
    #We only accept integers so as not to have any errors in the future
    time_seconds = int(input("Seconds: "))
    time_minutes = int(input("Minutes: "))
    time_hours = int(input("Hours: "))

#Function with countdown customization
def regre():

    global time_hours
    global time_minutes
    global time_seconds

    global time
    time = 0

    #Here we show the user the time it will take to finish the timer
    print (f"Timer: {time}s\n{time_hours}Hours / {time_minutes}Minutes / {time_seconds}Seconds")
    print("\n")

    #These conditionals:
    if time_hours > 0:
        #Convert the number of hours to seconds since we will be working in seconds
        time_hours = time_hours * 3600
        #We add the time (hours) to the time list
        time += time_hours
    if time_minutes > 0:
        #Convert the amount of minutes to seconds since we will be working in seconds
        time_minutes = time_minutes * 60
        #We add the time (minutes) to the time list
        time += time_minutes
    if time_seconds > 0:
        #We add the time in segundos to the time list
        time += time_seconds    

    #We will leave 3 seconds to the user to prepare to do the exercise that needs a timer
    print("Timer will start on:")
    temp = 3
    #I It will loop 3 times because temp = 3, you can modify temp if you need more time to prepare
    for i in range(temp):
        #We subtract 1 from temp to be able to write the remaining number in terminal
        temp -=1
        #The end='/r' is interesting. This, what it does is erase the previous content printed in the terminal and write the new one
        print(temp,end='\r')
        sleep(1)
    
    print("\n")

#Countdown function    
def progr():

    global time

    #This for is in charge of doing all the magic
    #We use tqdm to create the progressive bar
    #We will go through the cycle as many times as there are numbers in the time range that we configured before
    for i in tqdm(range(time)):
        print("",end='\r')
        #We sleep to the program 1 second
        sleep(1)

if __name__ == '__main__':
    vars()
    regre()
    progr()
