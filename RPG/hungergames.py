#!usr/bin/env python3
from random import randint
import sys
import time
import os
import dice

name = ""
district = 0
current_location = "CORNUCOPIA"
inventory = []
equipment = []
player_health = 100

bestiary = [{'name' : 'goblin', 'health' : 10, 'damage' : '1d5'},
            {'name' : 'orc', 'health' : 15, 'damage' : '1d8'},
            {'name' : 'ogre', 'health' : 20, 'damage' : '1d12'}]
armory = {'sword': {'damage': '1d12'}}

food ={
  'apple': 10,
  'banana': 20,
  'mushroom': -20,
  'nightlockberries': -100,
  'rabbit': 30,
  'snake': 50,
  'deer': 100,
  'beef': 25
}

arena = {
        'CORNUCOPIA' : {
            'south' : 'DOPPLER',
            'east' : 'BRAZIL',
            'north': 'ARIZONA',
            'west': 'HOUDINI',
            'item' : ['sword', 'bow and arrow', 'knife', 'crossbow', 'axe', 'apple', 'banana', 'beef'],
            'desc' : 'You are in the center of the Arena with most resources, however, this is also the most dangerous place.'
            },
        'ARIZONA' : {
            'south' : 'CORNUCOPIA',
            'east' : 'BIGFOOT',
            'west': 'LOWFLYINGHAWK',
            'item' : ['apple', 'banana', 'mushroom'],
            'desc' : 'You are in the beautiful ARIZONA section. You may collect some food for survival, but be careful, some of them can be poisonous.'
            },
        'BIGFOOT' : {
            'south' : 'BRAZIL',
            'west': 'ARIZONA',
            'item': ['deer', 'apple', 'bow&arrow'],
            'desc' : 'You are in the BIGFOOT section. Mutated monsters could be around.',
            },
        'BRAZIL' : {
            'west' : 'CORNUCOPIA',
            'south' : 'DAWSON',
            'north' : 'BIGFOOT',
            'item' : ['rabbit', 'snake'],
            'desc' : 'You are in the wild BRAZIL section. More rewarding items comes with more danger',
            },
        'DAWSON' : {
            'north' : 'BRAZIL',
            'west' : 'DOPPLER',
            'item' : ['banana', 'mushroom', 'knife'],
            'desc' : 'You are in the DAWSON section, some weapons are laying around',
            },
        'DOPPLER' : {
            'east' : 'DAWSON',
            'north': 'CORNUCOPIA',
            'west': 'FIONA',
            'item' : ['crossbow', 'axe'],
            'desc' : 'You are in the DOPPLER section. It\'s quite winddy here',
            },
        'FIONA' : {
            'east' : 'DOPPLER',
            'north': 'HOUDINI',
            'item' : ['mushroom', 'nightlockberries'],
            'desc' : 'You are in the FIONA section. '
            },
        'HOUDINI' : {
            'south' : 'FIONA',
            'east' : 'CORNUCOPIA',
            'north': 'LOWFLYINGHAWK',
            'item' : ['nightlockberries'],
            'desc' : 'You are in the HOUDINI section'
            },
        'LOWFLYINGHAWK' : {
            'south' : 'HOUDINI',
            'east' : 'ARIZONA',
            'item' : ['apple', 'banana'],
            'desc' : 'You are in the LOWFLYINGHAWK section'
            },
        }

def speech_text(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

def welcome_text():
  print("Welcome to Hunger Games!")
  speech_text("let's create your character\n")
  speech_text("What's your name? ")
  global name, district
  name = input("> ")
  speech_text("Which district are you from? ")
  district = int(input("> "))
  speech_text(f"Welcome {name} from district {district} \n")
  speech_text(f"Congratulations, you are selected as the tribute for district {district}. May the odds be ever in your favor! \n")

def showInstructions():
    print('''
THE HUNGER GAMES
--------
Actions:
    GO [north, south, east, west]
    GET [item]
    USE [item]
    INV/INVENTORY
Type 'help' at any time! Type 'q' to quit!''')

def playerinfo():
  print('=================================')
  print('YOU ARE IN THE ' + current_location + '.')
  print('Equipment :', str(equipment))
  print('Inventory :', str(inventory))
  print('=================================')


def showStatus(): # display the player's status
  if 'item' in arena[current_location]:
    print('Items available here are: ' + ', '.join(arena[current_location]['item']) + '.')

def combat():
  monster_ID= randint(0,2)

  global player_health, inventory, armory, bestiary
  round = 1
  monster_health = bestiary[monster_ID]['health']

  print(f"A ferocious {bestiary[monster_ID]['name']} approaches! COMBAT HAS BEGUN!\n")
  while True:
    print(f"ROUND {round}")
    print("Player Health: [" + str(player_health) + "]")
    print("Monster Health: [" + str(monster_health) + "]")

    print("Type: RUN, ATTACK, or USE [item]") # gotta write code for cast
    move = input().lower().split() # converts move into a lower-case list to deal with each item in list separately
    monster_damage = sum(dice.roll(bestiary[monster_ID]['damage']))
    print("\n=========================")

    if move[0] == 'use': #
      if move[1] in inventory: # checks if weapon is in your inventory
        player_damage = dice.roll(armory[move[1]]['damage'])
        print(f"You hit a {bestiary[monster_ID]['name']} for {player_damage} damage!")
      if move[1] not in inventory:
        print(f"There is no {move[1]} in your inventory!")

      try:
        monster_health -= int(player_damage)
      except:
        pass
      if monster_health <= 0:
        print(f"The {bestiary[monster_ID]['name']} lies dead. You are victorious!\n")
        break

      print(f"A {bestiary[monster_ID]['name']} hits you for {monster_damage} damage!")
      print ("=========================\n")
      round += 1
      player_health -= int(monster_damage)

      if player_health <= 0:
        print("You have been vanquished! You are dead.")
        sys.exit()

def game():
  global player_health, inventory, current_location, equipment
  weapon_list =['sword', 'bow&arrow', 'knife', 'crossbow', 'axe']
  while True:   # MAIN INFINITE LOOP
    playerinfo()
    showStatus()
    # ask the player what they want to do
    move = ''
    while move == '':
      move = input('>') # so long as the move does not
        # have a value. Ask the user for input
    move = move.lower().split() # make everything lower case because directions and items require it, then split into a list
    os.system('clear') # clear the screen
    if move[0] == 'go':
      if move[1] in arena[current_location]:
        current_location = arena[current_location][move[1]]
        if 'desc' in arena[current_location]:
          print(arena[current_location]['desc'])
      else:
        print("YOU CAN'T GO THAT WAY!")
    if move[0] == 'use':
        if move[1].lower() == 'potion' and 'potion' in inventory:
          print("You drink from the potion. Your health has been restored!")
          player_health = 20
    if move[0] == 'get':
      if move[1] in weapon_list:
        if len(equipment) < 3:
          if move[1] in arena[current_location]['item']:
            equipment += [move[1]]
            print(move[1].capitalize() + ' received!') # msg saying you received the item
            arena[current_location]['item'].remove(move[1]) # deletes that item from the dictionary
          else:
            print('YOU CANNOT GET ' + (move[1].upper()) + '!')
        else:
          print("Your reached your equipment limit, you cannot get any more weapons")
      else:
        if len(inventory) < 5:
          if move[1] in arena[current_location]['item']:
            inventory += [move[1]] # add item to inv
            print(move[1].capitalize() + ' received!') # msg saying you received the item
            arena[current_location]['item'].remove(move[1]) # deletes that item from the dictionary
          else:
            print('YOU CANNOT GET ' + (move[1].upper()) + '!')
        else:
          print("Your bag is full, you cannot get any more items")

    elif move[0] == 'help':
      showInstructions()

    elif move[0] in ['q', 'quit]']:
      print("Are you sure you want to quit? Yes/No")
      quit_query = input('>')
      if quit_query.lower() in ['y', 'yes']:
        print("Thanks for playing!")
        sys.exit()
      else:
        pass

def main():
  #welcome_text()
  showInstructions()
  game()

if __name__ == '__main__':
    main()

