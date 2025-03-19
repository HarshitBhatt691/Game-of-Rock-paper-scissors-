Rock Paper Scissors - Python Game

Description

This is a simple Rock Paper Scissors game implemented in Python. The player competes against the computer in a classic game of Rock, Paper, Scissors.

Features

User vs. Computer gameplay

Randomized computer choices

Input validation

Score tracking (optional)


Requirements

Python 3.x


How to Run

1. Clone or download the repository.


2. Open a terminal and navigate to the project folder.
 
3. Run the script using: `python rock_paper_scissors.py ` 
 

 
## How to Play
 
 
1. The game prompts the user to choose Rock, Paper, or Scissors.
 
2. The computer randomly selects an option.
 
3. The winner is decided based on the following rules: 
 
  - Rock beats Scissors
 
  - Scissors beats Paper
 
  - Paper beats Rock
 

 
 
4. The game continues until the user decides to quit.
 

 
## Example Output
 `Enter your choice (rock, paper, scissors): rock   Computer chose: scissors   You win!   ` 
## License
This project is open-source and free to use.

# python code
'''

R=1

P=-1

S=0

'''

import random

computer=random.choice([1,-1,0])

youstr=input("Enter your choice(R,P,S): ")

dict={'R':1,'P':-1,'S':0}

reversedict={1:"Rock",-1:"Paper",0:"Sisor"}

you=dict[youstr]

print(f"you chose: {reversedict[you]}\nComputer chose: {reversedict[computer]}")

if(computer==you):

print("ITS A DRAW")

else:

if(computer==1 and you==-1):

print("YOU WIN")

elif(computer==1 and you==0):

print("YOU LOSE")

elif(computer==-1 and you==1):

print("YOU LOSE")

elif(computer==-1 and you==0):

print("YOU WIN")
elif(computer==0 and you==1):

print("YOU WIN")

elif(computer==0 and you==-1):

print("YOU LOSE")

else:

print("SORRY!! Something went wrong ")
