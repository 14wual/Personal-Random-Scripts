# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

#What's this?
#This is a book recommendation algorithm, where the algorithm recommends titles based on your votes.
                                   

#Requirements: BEFORE ALL YOU MUST CREATE YOUR DATABASE!
  #Install the requirements (at the terminal) to run this program
    #pip install mysql.connector random time

    #You will need to create your database table with this command (after line 19):
      #mycursor.execute("CREATE TABLE <Table Name> (Author VARCHAR(255), Títle VARCHAR(255), Genre VARCHAR(255)")
    
    #To make new records in your database write this:
          #sql = "INSERT INTO tablalibros (Author, Genre, Títle) VALUES (%s, %s, %s)"
          #val = [("<Author Name>","<Genre Name>","<Title Name>")]
          #mycursor.execute(sql, val)

    #To view your logs use this command:
          #mycursor.execute("SELECT * FROM <Table Name>")
          #myresult = mycursor.fetchall()
          #for x in myresult:
            #  print(x)


import mysql.connector
import random
import time

#Connection to mysql database
mydb = mysql.connector.connect(
  host="localhost",
  user="<USSER>",
  passwd="<PASSWORD>",
  database= "<DDBB>"
)

mycursor = mydb.cursor()

#Enclose genders in "..." with a comma (,) to separate them from each other
genders = ("Gender1","Gender2","Gender3","Gender4","Gender5","...")
#The algorithm randomly selects a genre to show the user
gender = random.choice(genders)

#This "print" can comment or delete it because it only serves as a guide
#The thanks is that the user does not know what genre he is talking about, and that he is guided by the titles
print(gender)

#We will create a new list because we cannot modify the tuple
#It will be understood in line 92
new_gender = list()

#The api() function will be in charge of processing the entire algorithm
#The whole code will be explained below
def api(gender):

  #This is the request that we will make to our database table where we will ask it to save us in the 
  #"sql_title" tuple a list of authors and titles that belong to the respective genre that we have previously requested
  sql_title = "SELECT Títle, Author FROM <Name Table> WHERE gender ='%s'" % gender

  mycursor.execute(sql_title)
  myresult = mycursor.fetchall()

  #The "upvote" variable is used as a marker, so that when we exceed a predefined figure, we get the alert 
  #that our genre was found
  upvote = 0

  #This for will allow us to show all the results one by one
  for x in myresult:
    #Show the title
    print(x)

    #We will use this variable in the future to check if the author is still in the list
    author = x[1]
    #This "print" can comment or delete it because it only serves as a guide
    print(author)

    #We give the user time to read the title
    time.sleep(1)

    #At the time of voting, the user must choose whether or not they like the title
    vote = input("[+/-] | Vote positively or negatively according to how you liked the title: ")
    while vote != "+" and vote != "-":
      vote = input("[+/-] | Vote positively or negatively according to how you liked the title: ")

    if vote == "-":
      #If the user votes no
      for y in myresult:
        #We will check that the author is inside the tuple and if so, we will delete all the lists with his name 
        #so that it is not recommended again
        if author in myresult[1]:
          #The ".remove" method will be the one we implement for this action
          myresult.remove(y)
    elif vote == "+":
      #If the user votes yes
      #We will add one to our variable upvote
      upvote += 1
      #The number [3] can be changed to whatever you see fit, whether you have a larger or smaller database. 
      #It is recommended that the minimum number of each gender is this number
      if upvote == 3:
        #We congratulate the user for having found his gender
        print("Congratulations!\nYou have found your gender: %s" % gender)
        #We stop executing the script
        exit()
  #If we run out of titles it will mean that the user did not like me enough so we must start over
  cont()



def cont():
  #We will ask the user if he continues
  vote = input("[y/n] | You still there?: ")
  while vote != "y" and vote != "n" and vote != "N" and vote != "Y":
    vote = input("[y/n] |  You still there?: ")

  if vote == "y" or vote == "Y":
    #If your decision is yes
    global genders
    global gender

    #With the list that we created earlier, we are going to regenerate the genre list excluding the genre that we already used before
    for x in genders:
      new_gender.append(x)
    new_gender.remove(gender)
    
    #We randomly generate another gender
    gender = random.choice(new_gender)
    print(gender)
    
    #We start again
    api(gender)
  
  #If the user chooses this option it will mean that he wants to exit
  elif vote == "y" or vote == "Y":
    print("Thanks for your attention!")

if __name__ == '__main__':
    api(gender)
