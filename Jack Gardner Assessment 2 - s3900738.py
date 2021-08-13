#COSC1519 Introduction to Programming
#Student name: Jack Gardner
#Student number: 3900738
#Practical group:
# Thursday 8:30am

#!/bin/python3

#string input which asks the user their name and gives a scenario

name = str(input("""
Welcome Sir, thank you for ariving on such short notice. 
We have called upon all the knights in the kingdom to the come to the aid of the Princess. 
A terrible dragon has taken her castle hostage. Only you can save her! 
What is your name kind sir?
"""))

#This is an integer input question which asks the player their title/nickname as a knight. it saves this data for when refurring to them

while True:
  nickname1 = int(input("""
  Ah yes I have heard of Sir %s before. 
  However I cannot remember the title the King bestowed upon you.
  Was it?
  1 - %s The Brave
  2 - %s The Tall
  3 - %s The Strong
  4 - %s The Noble
  """ % (name, name, name, name, name)))
  
#This takes the players answer of a simple to input integer and determines their title/nickname or asks them to try again if they did it incorrectly

  if nickname1 == 1:
    nickname2 = 'The Brave'
    break
  elif nickname1 == 2:
    nickname2 = 'The Tall'
    break
  elif nickname1 == 3:
    nickname2 = 'The Strong'
    break
  elif nickname1 == 4:
    nickname2 = 'The Noble'
    break
  else:
    print("""
    Please try again.
    """)
print("")

#This outputs the players name and title/nickname to let them know that it is correct and to make them feel as though they are being interacted with

if nickname2 == 'The Brave':
  print("Ah yes Sir %s %s I remember now!" % (name, nickname2))
elif nickname2 == 'The Tall':
  print("Ah yes Sir %s %s I remember now!" % (name, nickname2))
elif nickname2 == 'The Strong':
  print("Ah yes Sir %s %s I remember now!" % (name, nickname2))
elif nickname2 == 'The Noble':
  print("Ah yes Sir %s %s I remember now!" % (name, nickname2))

#An easter egg question which gets any input for meters and convers to floating point, it then states the players height back to them for fun

if nickname2 == 'The Tall':
    height = input("""
    You sure are tall, around 1.9 Meters. How tall are you in meters?
    """)
    height = float(height)
    print("""
    Wow %s is indeed tall!
    """ %(height))

#This shows the details for the senario and gives a storyline and some useful hints, it also mentions the players name

print("""
Anyways where was I? Ah yes the Princess.
Quickly you must go through that gate, you will then pass through a court yard.
After you enter the castle you must take the left hallway, rememeber that.
You may encounter some outlaws taking advantage of the situation and looting the castle, be mindful of them.
And good luck Sir %s %s!
""" % (name, nickname2))

#This updates the player on their status and gives them options on what to do next.

print("You have entered the castle.")

while True:
  turn = int(input("""
  There are three hallways. 
  1 - The left
  2 - The middle
  3 - The right 
  Which one do you take?
  """))

#This determines if the input was correct, if yes they progress, if not they will have to restart

  if turn == 1:
    turn2 = 'the left hallway'
    break
  elif turn == 2:
    turn2 = 'the middle hallway'
    break
  elif turn == 3:
    turn2 = 'the right hallway'
    break
  else:
    print("""
    Please try again.
    """)

#This provides a message to the player updating them on their position and if they did the correct or incorrect thing

if turn2 == 'the left hallway':
  print("""
  Well done! 
  You went down the correct hallway.
  Keep going forwards.
  """)
elif turn2 == 'the middle hallway':
  print("""
  You took the wrong hallway. By the time you realised it was too late. The dragon took the Princess.
  Try the game again.
  """)
  quit()
elif turn2 == 'the right hallway':
  print("""
  You took the wrong hallway. By the time you realised it was too late. The dragon took the Princess.
  Try the game again.
  """)
  quit()

#Text descriping the senario and giving you options on what to do

while True:
  outlaws = int(input("""
  You have been running down the left hallway.
  Eventually you come across some outlaws looting silver wear.
  They draw their swords.
  What do you do?
  1 - Draw your sword and fight
  2 - Turn and run back to the entrance
  3 - Say "Hey what's that over there!" and run past them
  """))

#if statements to determine if the players input was correct, if yes it would congradulate them and they would progress, if not the game would end

  if outlaws == 1:
    print("You decided to fight the outlaws. You managed to win, but it took too long and the Dragon got to the Princess before you did.")
    quit()
  elif outlaws == 2:
    print("You decided to run. The Dragon took the Princess, the outlaws took the silver and the King stripped you of your Knighthood.")
    quit()
  elif outlaws == 3:
    print("You sucsessfully distracted the outlaws and got past them!")
    break
  else: 
    print("""
    Please try again.
    """)

#This is a statement for the next challenge for the player

print("""
You find the dragon in the main hall searching for the Princess.
You approach it.
Tt has 3 points of health.
To defeat a dragon you must understand it.
The Dragon says 'Idao gha haba ae javes'
You know 'Idao gha haba ae' translates to 'I hope they don't know my weakness is a'
You must figure out what Javes means.
Luckily you have a book to translate.
J is S, A is P, V is E, E is A and S is r.
""")

#The i is for the dragons health which deterierates after damage. There is also a question that if answered correctly progresses the player to the next stage, if not they get a retry

i = 3

while True:
  dragon_speech = input("What did the Dragon say word for word?")
  
  dragon_speech = str(dragon_speech)
  
  if dragon_speech == "I hope they don't know my weakness is a spear":
    print("""
    Well done you successfully translated the speech.
    You now know his weakness.
    """)
    break
  else:
    print("""
    That was an incorrect translation. Please try that again.
    """)

#This is a integer question to collect the players response

while True:
  dragon_spear = int(input("""
  You understand what the dragons weakness is.
  You must capitalise off this.
  What do you do?
  1 - Use your sword instead
  2 - Run and hope the dragon doesn't chase you
  3 - Grab a spear from a nearby armour stand
  """))

#This is checking the players input and if it is correct they continue onwards with a congradulations, if not they must restart, or it lets them answer again if they answered incorrectly.

  if dragon_spear == 1:
    print("""
    You tried yo use your sword. You needed to get too close to fight. The dragon just hit you with ease.
    Try the game again.
    """)
    quit()
  elif dragon_spear == 2:
    print("""
    You tried to out run the dragon, but he just flew to you with ease.
    Try the game again.
    """)
    quit()
  elif dragon_spear == 3:
    print("""
    Well done, you made the correct decision. 
    The dragon is scared now!
    """)
    break
  else:
    print("""
    Please try again.
    """)
  
#This is a floating point question to collect the players response 

while True:
  dragon_action = float(input(("""
  The Dragon sees your spear and cowers into a corner.
  You have the spear aimed at his body.
  You must his a critical spot for him to take damage from the attack.
  You must aim your spear a certain ammount of degrees for one of these targets:
  34.8 degrees for the head
  26.7 degrees for the neck
  13.9 degrees for the chest
  Input the degree number you want to try, it's ok if you miss, there are more spears to pick up:
  """)))

#This is checking the players input, if it is correct a health point will be taken away from the dragon

  if dragon_action == 34.8:
    print("""
    Well done. You went for the head, it has taken damage!
    The Dragon now has 2 points of health.
    """)
    i = i - 1
    break
  elif dragon_action == 26.7:
    print("""
    You went for the neck, but it was too narrow and you just missed.
    Grab another spear and try again.
    """)
  elif dragon_action == 13.9:
    print("""
    You went for the chest, but it hit his scales and did not do any significant damage.
    Grab another spear and try again.
    """)
  else:
    print("""
    Please try again.
    """) 

#This is giving the player an update on their situation

print("""
The dragon tries to fly away after the attack.
  You notice a crossbow and a bow lying on the ground.
  Along with some flint tipped arrows and some iron tipped arrows.
  You must pick up a combination and fire them at the Dragon.
  """)

#This is giving the player some options

while True:
    
    dragon_action2 = int(input("""
    Do you pick up the Crossbow or the Bow?
    1 - Crossbow
    2 - Bow
    """))
  
#This is giving the player futher options to complete the question

    dragon_action3 = int(input("""
    Do you pick up the flint tipped arrows or the iron tipped arrows))
    1 - Flint tipped arrows
    2 - Iron tipped arrows
    """))

#This is an if statement with an 'and' condition as it is for two questions

    if dragon_action2 == 1 and dragon_action3 == 2:
        print("""
        Well done.
        That was the right decision.
        Even tho the crossbow took longer to load it did more damage as the bow would not have been powerful enough.
        The iron arrows are also better at piercing a dragon's scales.
        The Dragon now has 1 health point.
        """)
        i = i - 1
        break
    else:
        print("""
        Please try again.
        """)

#This is updating the player on the story

print("""
You chase the Dragon and see him flying.
He is circling the tallest tower of the castle.
He has found the Princess.
He is flying too high for your Crossbow to reach.
You begin to lose hope, but then you remember!
In your book for translations to Dragon-Tongue there is also a chapter on spells for dragons.
""")

#This is a string input question that has options for a spell which must be typed out

spell = str(input("""
There are three spells for Dragons that you understand:
They are as follows:
-'Sacar le relt' meaning 'May your wings stop working'
-'Kraken nai mo' meaning 'May your scales break'
-'Haven emm poi' meaning 'May you become blind'
State the spell in its language:
"""))

#This is a loop with if statements, if the players answer is correct it will tell them they did the right thing, tell them the dragon has to health and it will then make i = 0, this will display a messge that the dragon is slain
#If the wrong answer is given they will be informed that got it wrong and they they will have to restart the game

while True:
  if spell == 'Sacar le relt':
    print("""
    You made its wings stop working.
    He could not fly and fell.
    The dragon now has 0 health points.
    """)
    i = i - 1
    break
  elif spell == 'Kraken nai mo':
    print("""
    The Dragons scales broke, but he was unharmed and took the Princess.
    Try the game again.
    """)
    quit()
  elif spell == 'Haven emm poi':
    print("""
    The Dragon became blind, but in panik he broke the tall tower and the Princess fell.
    Try the game again.
    """)
    quit()
  else:
    print("""
    Please try again.
    """)

#This is a calculation, by now the i = 0, and if i = 0 then it will display a message to the player congradulating them on slaying the dragon

if i == 0:
  print("""
  Well done! The Dragon is slain!
  """)
  
#This is an update to the player on the story

print("""
You climb the tallest tower and at the top you find the Princess!
You look at her and kneel, as it is customary for a Knight to kneel for Royalty.
You don't know what comes over you but you propose!
""")
 
#you find the princess and propose, it uses a list and simple loop
marry = ["Please marry me", "Please marry me", "Please marry me"]
for x in marry:
  print(x)
  
#nested loop with the princesses response of yes in many forms

print("""
She says:
""")

words1 = ["Um", "Of course", "Absolutely"]
words2 = ["Yes", "I will", "Now"]

for x in words1:
  for y in words2:
    print(x, y)

#updating the player on the story

print("""
You leave the castle with the Dragon slain and the Princess in your arms.
You greet the Gate Keeper who you meet earlier.
He says:
""")

#function that displays the gatekeepers congratulations
def name_function(knight_name):
  print("Well done " + knight_name)

name_function("%s %s" % (name, nickname2))
name_function("%s %s" % (name, nickname2))
name_function("%s %s" % (name, nickname2))

#printing a string many times showing the crows appreciating

print("""
The crowd that has gathered begins to cheer:
""")

cheers = '*cheering sounds* '

print(cheers*8)

print("""
Well done! The Game is over!
""")