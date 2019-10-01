# Austin Hibbitt
# Rock Paper Scissors Game
#_________________________
# break into pieces
# Welcome page, name entry
# Score screen with computer, player (name), tles
# Options or game r, p, s, q
# Game will loop until q is entered
# Each loop it will get a random choice from the computer
#a choice from the player, compare the two, and update score
# When game ends (q is entered) final score is displayed 

# Welcome page 
# Prompt for name
# a welcome message 

#_________________________

# imports
import random
# variables
playerScore = 0
computerScore = 0
ties = 0
# make a list 
cChoices =["r", "p", "s"]
print("Welcome to Rock Paper Scissors")
name = input("Enter your name")
# Main Loop 
while True:
	print("Score:")
	print("Computer: " + str(computerScore))
	print(name + str(playerScore))
	print("Ties: " + str(ties))
	choice = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors or 'q' to quit: ")
	computerChoice = random.choice(cChoices)







    

