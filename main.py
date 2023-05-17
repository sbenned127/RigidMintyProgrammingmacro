# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Darryl Bennett
# Creation Date: 5/8/23
# Below is a simple program with several.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
  # The three quotes weren't necessary you just didn't make your print in one whole line, meaning that you kept clicking enter to make it seem like it was one line so I made an adjustment and made sure to delete the spaces to make it 1 line.
	print('You are in a land full of dragons. In front of you you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.')
	print()

def chooseCave():
    cave = ''
  #Looks like an indent error here, I unindented this block --DB
    while cave != '1' and cave != '2':
      print('Which cave will you go into? (1 or 2)')
      cave = input()
  # It looks like you put in an "s" in "cave" so I just removed the s from "cave"
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    #sleep for 2 seconds
    time.sleep(2)
    print('It is dark and spooky...')
    #sleep for 2 seconds
    time.sleep(3)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    #sleep for 2 seconds
    time.sleep(2)
    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
      #It looks like you forgot to complete your print with parenthesis on each side. I put in the paranthesis to complete this print.
        print ('Gobbles you down in one bite!')
        print("that's crazy")


displayIntro()
# It looks like you didn't use the camel case for "chooseCave" so python read it as "choosecave" which said it wasn't defined so I fixed it and put a camel case in it. Also your parenthesis were in the outside of chooseCave instead of it supposed to be on the side as I fixed. 
caveNumber = chooseCave()
checkCave(caveNumber)
    # it looks like you didn't were trying to say "playing" but you put an "n" so I corrected it and put "playing"
print("Thanks for playing")
