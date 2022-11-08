# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

#What's this?
#This script generates a strong and personalized password


#Requirements: 
    #Install the requirements (at the terminal) to run this program
        #pip install random

#Enjoyment!

import random

#This series of lists (lowercase, Capitalletters, numbers, specialcharacters) define the characters that will 
#later be used to generate your password
lowercase = "abcdefghijklmnñopqrstuvwxyz"
capitalletters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numbers = "0123456789"
specialcharacters = "ºª!|·#$%&¬/()=?¿¡.:-_,;*{,}ç^[+]"

    #These variables will be configured later
#This variable measures the length of the password
length = 0
#This variable configures the security level of your password
security_level = 0
global lists

#Function where we customize the password
def personalization():
    global lowercase
    global Capitalletters
    global numbers
    global specialcharacters
    global lists

    global length

    global security_level

    #We specify to the user what we are going to do
    print("Now you will be asked a series of questions about how you want your password (length and security level)")

    #At this time we ask what will be the length of the password
    length = int(input("PASSWORD length: "))

    #The password will have a maximum of 20 characters
    if length > 20:
        print("The maximum number of characters is 20")
        length = int(input("PASSWORD length: "))
    #The password will have a minimum of 8 characters
    elif length < 8:
        print("The minimum number of characters is 8")
        length = int(input("PASSWORD length: "))

    #Here we ask the user what level of security he wants for his password
    security_level = int(input("Choose a number from 1 to 3 depending on the security level of your password: "))

    #This conditional structure will validate the previous answer
    if security_level >= 4:
        print("Eliga entre estas opciones: \n    Level 1. Uppercase and Lowercase\n    Level 2. Previous + Numbers \n    Level 3. Previous + Characters")
        security_level = int(input("Choose a number from 1 to 3 depending on the security level of your password:"))
    elif security_level <= 0:
        print("Eliga entre estas opciones: \n    Level 1. Uppercase and Lowercase\n    Level 2. Previous + Numbers \n    Level 3. Previous + Characters")
        security_level = int(input("Choose a number from 1 to 3 depending on the security level of your password:"))

    #This conditional structure will create a list with the characters that we will use in the pass
    if security_level == 1:
        lists = Capitalletters+lowercase
    elif security_level == 2:
        lists = Capitalletters+lowercase+numbers
    elif security_level == 3:
        lists = Capitalletters+lowercase+numbers+specialcharacters

#This function is responsible for generating the password
def GeneratePassword():
    global lists
    global length

    password = ""

    #This for loops through the range you predefined above. For each cycle, it randomly chooses a character 
    #from the previously created list to generate our password
    for x in range(length):
        a = random.choice(str(lists))
        password += a
    
    print(password)

if __name__ == '__main__':
    personalization()
    GeneratePassword()
