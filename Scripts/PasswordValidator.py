# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

#What's this?
#This algorithm checks if your password is secure, if it is not, it generates a


#Requirements: 
    #Install the requirements (at the terminal) to run this program
        #pip install random 

#Enjoyment!

import random

global specialcharacters
global char_list 

specialcharacters = "ºª!|·#$%&¬/()=?¿¡.:-_,;*{,}ç^[+]"
char_list = ("º","ª","!","|","·",",","$","%","&","¬","/","(",")","=","?","¿","¡",".",":","-","_",";","*","{","}","ç","^","[","+","]<")

def api():
    global specialcharacters

    #The user will enter the password to check its security
    usser_pass = input("Enter your password: ")

    #The algorithm checks that all characters in the password are text
    if usser_pass.isalpha() == True:
        #If true, check that they are all lowercase.
        if usser_pass.islower() == True:
            print("Your password is not secure.\nDo not go through life with lowercase letters.\nWe suggest this new password: ")
            #Since a password of only lowercase letters is not secure, it warns the user and calls the passgenerator function to randomly generate a password
            passgenerator()
        #If true, cocmtest that they are all uppercase
        elif usser_pass.isupper() == True:
            print("Your password is not secure.\nDo not fence through life with capital letters.\nWe suggest this new password: ")
            #Since an all-caps password is not secure, it warns the user and calls the passgenerator function to randomly generate a password.
            passgenerator()
        else:
            print("Even if you are case sensitive, your password is not secure.\nWe suggest this new password: ")
            #Since a password of only uppercase and lowercase letters is not secure, it warns the user and calls the passgenerator function to randomly generate a password
            passgenerator()
    #The algorithm checks that all characters in the password are numbers
    elif usser_pass.isdigit() == True:
        print("Your password is not secure.\nDon't go through life with numbers.\nWe suggest this new password:")
        ##Since a password of only letters and numbers is not secure, warn the user and call the passgenerator function to randomly generate a password
        passgenerator()
    #If the algorithm has passed to the else, it means that the password has a future
    else:
        length = 0
        #This for will check the length of the password
        for n in usser_pass:
            length += 1

        if length <= 8:
            print("Your password is too short.\nWe suggest this new password: ")
            ##If the length is less than or equal to 8, a password is recommended because it is too short a password.
            passgenerator()
        else:
            iscar = False
            #True and usser_pass in carácteres
            for n in usser_pass: 
                #Otherwise, if it is longer than 8, the algorithm will check character by character that one 
                #of them matches the list of characters on line 24.
                if n in char_list :
                    iscar = True
            if iscar == True:
                #If the iscar variable is == true, it will mean that our password is secure
                print("You have a strong password")

#This function counted in another repository script.
def passgenerator():
    
    lowercase = "abcdefghijklmnñopqrstuvwxyz"
    capitalletters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    numbers = "0123456789"
    global specialcharacters
    
    #The password will have uppercase and lowercase letters, numbers and special characters
    lists = capitalletters+lowercase+numbers+specialcharacters
    #Its length will be 12
    length = 12

    password = ""


    for s in range(length):
        a = random.choice(str(lists))
        password += a
    
    print(password)

if __name__ == '__main__':
    api()
