# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

#What's this?
# ! Welcome to the classic game of Rock Paper Scissors !


#Requirements: 
    #Install the requirements (at the terminal) to run this program
        #pip install random time

#Enjoyment!

import random, time

#variables
global round
round = 0
global marker_player
marker_player = 0
global marker_computer
marker_computer = 0

#Game rules
def introduction():
    print("Welcome to the game of ROCK PAPER SCISSORS")
    print("\n The Rules are as follows.")
    print("\n1. Scissors beats paper, but paper is beaten by stone")
    print("\n2. Rock beats scissors, but scissors is beaten by paper")
    print("\n3. Paper wins scissors, but paper wins scissors")

def compr():
    global marker_player
    global marker_computer 
    global round

    #Each time the rules() function is called, the global variable "round" will be added 1 to keep track of the number of rounds
    round += 1

    #This list is used in random for computer decision making. Where the pc player chooses "Rock, Paper, Scissors"
    lists = ['Scissors','Paper','Stone']
    computer = random.choice(lists)

    #We wait a second to give excitement to the game
    time.sleep(1)

    #These structures are in charge of checking who was the winner
    #If the player chooses scissors
    if player == 'scissors' or 'Scissors':
        if computer == 'Paper':
            print("Player WIN")
            #If the player wins, add 1 to the player's score
            marker_player += 1
        elif computer == 'Stone':
            print("Player LOSE")
            #If the player lose, 1 is added to the computer score
            marker_computer += 1
        elif computer == 'Scissors':
            #If the player and the computer make the same decision, nothing will be done, since it is a tie.
            print("Player TIE")

    elif player == 'stone' or 'Stone':
        if computer == 'scissors' or 'Scissors':
            print("Player WIN")
            #If the player wins, add 1 to the player's score
            marker_player += 1
        elif computer == 'Paper':
            print("Player LOSE")
            #If the player lose, 1 is added to the computer score
            marker_computer += 1
        elif computer == 'Stone':
            #If the player and the computer make the same decision, nothing will be done, since it is a tie.
            print("Player TIE")
            
    elif player == 'paper' or 'Paper':
        if computer == 'Stone':
            print("Player WIN")
            #If the player wins, add 1 to the player's score
            marker_player += 1
        elif computer == 'Scissors':
            #If the player lose, 1 is added to the computer score
            print("Player LOSE")
            marker_computer += 1
        elif computer == 'Paper':
            #If the player and the computer make the same decision, nothing will be done, since it is a tie.
            print("Player TIE")

    #At the end of the round we return to the main to make decisions again and show the result of this last round
    main() 


def main():
    global marker_computer
    global marker_player
    global player
    player = 0

    #We will show round Number X
    print("\n\nRound Number %d" % round)
    #We will show the marker
    print(f"\nMarker {marker_player} (Player) - {marker_computer} (Computer)")

    print("Rock, Paper or Scissors?")

    #We ask the player what his decision is
    player = input("\n([Q] to exit) | Choose: ")

    while player != "q" or "Q":
        #if not press Q,  We call the function "compr"
        compr()
    else:
        #if he presses Q, We call the function "finish"
        finish()
        

def finish():

    #By the end

    print("\nThanks for playing")
    #We will show the statistics of the game
    print("\n \nYOUR RESULT")

    #We will show the number of rounds we have played
    print("\n\nHas played %d ronds" % round)
    #We will show the final result
    print(f"\nMarker {marker_player} (Player) - {marker_computer} (Computer)")

if __name__ == '__main__':
    introduction()
    main()
