from random import randint
import sys
import time
import os
import dice
import random

name = ""
district = 0
current_location = "CORNUCOPIA"
inventory = []
equipment = []
player_health = 100

monsters = [{'name' : 'Monkey Mutts', 'health' : 20, 'damage' : '1d5'},
            {'name' : 'Jabberjays', 'health' : 25, 'damage' : '1d8'},
            {'name' : 'Tracker Jackers', 'health' : 30, 'damage' : '1d10'}]

tributes = [{'name' : 'Facet', 'district': 1, 'health' : 50, 'damage' : '1d15'},
            {'name' : 'Marcus', 'district': 2, 'health' : 50, 'damage' : '1d15'},
            {'name' : 'Circ', 'district': 3, 'health' : 50, 'damage' : '1d15'},
            {'name' : 'Mizzen', 'district': 4, 'health' : 50, 'damage' : '1d15'},
            {'name' : 'Hy', 'district': 5, 'health' : 50, 'damage' : '1d15'},
            {'name' : 'Otto', 'district': 6, 'health' : 50, 'damage' : '1d15'},
            {'name' : 'Treech', 'district': 7, 'health' : 50, 'damage' : '1d20'},
            {'name' : 'Bobbin', 'district': 8, 'health' : 50, 'damage' : '1d20'},
            {'name' : 'Panlo', 'district': 9, 'health' : 50, 'damage' : '1d20'},
            {'name' : 'Tanner', 'district': 10, 'health' : 50, 'damage' : '1d20'},
            {'name' : 'Reapper Ash', 'district': 11, 'health' : 50, 'damage' : '1d20'},
            {'name' : 'Lucy Gray Baird', 'district': 12, 'health' : 50, 'damage' : '1d20'}]

armory = {
  'sword': {'damage': '1d15'},
  'bow&arrow': {'damage': '1d30'},
  'knife': {'damage': '1d12'},
  'crossbow': {'damage': '1d25'},
  'axe': {'damage': '1d30'},
}

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
            'item' : ['sword', 'bow&arrow', 'knife', 'crossbow', 'axe', 'apple', 'banana', 'beef'],
            'desc' : 'You are in the center of the Arena with most resources, however, this is also the most dangerous place.',
            'randenc' : '30'
            },
        'ARIZONA' : {
            'south' : 'CORNUCOPIA',
            'east' : 'BIGFOOT',
            'west': 'LOWFLYINGHAWK',
            'item' : ['apple', 'banana', 'mushroom'],
            'desc' : 'You are in the beautiful ARIZONA section. You may collect some food for survival, but be careful, some of them can be poisonous.',
            'randenc' : '0'
            },
        'BIGFOOT' : {
            'south' : 'BRAZIL',
            'west': 'ARIZONA',
            'item': ['deer', 'apple', 'bow&arrow'],
            'desc' : 'You are in the BIGFOOT section. Mutated monsters could be around.',
            'randenc' : '20'
            },
        'BRAZIL' : {
            'west' : 'CORNUCOPIA',
            'south' : 'DAWSON',
            'north' : 'BIGFOOT',
            'item' : ['rabbit', 'snake'],
            'desc' : 'You are in the wild BRAZIL section. More rewarding items comes with more danger',
            'randenc' : '10'
            },
        'DAWSON' : {
            'north' : 'BRAZIL',
            'west' : 'DOPPLER',
            'item' : ['banana', 'mushroom', 'knife'],
            'desc' : 'You are in the DAWSON section, some weapons are laying around',
            'randenc' : '20'
            },
        'DOPPLER' : {
            'east' : 'DAWSON',
            'north': 'CORNUCOPIA',
            'west': 'FIONA',
            'item' : ['crossbow', 'axe'],
            'desc' : 'You are in the DOPPLER section. It\'s quite winddy here',
            'randenc' : '20'
            },
        'FIONA' : {
            'east' : 'DOPPLER',
            'north': 'HOUDINI',
            'item' : ['mushroom', 'nightlockberries'],
            'desc' : 'You are in the FIONA section. ',
            'randenc' : '0'
            },
        'HOUDINI' : {
            'south' : 'FIONA',
            'east' : 'CORNUCOPIA',
            'north': 'LOWFLYINGHAWK',
            'item' : ['nightlockberries'],
            'desc' : 'You are in the HOUDINI section',
            'randenc' : '0'
            },
        'LOWFLYINGHAWK' : {
            'south' : 'HOUDINI',
            'east' : 'ARIZONA',
            'item' : ['apple', 'banana'],
            'desc' : 'You are in the LOWFLYINGHAWK section',
            'randenc' : '10'
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

def random_encounter():
  randenc = int(arena[current_location]['randenc']) +5
  if randenc >= 30:
    fight_tribute()
    fight_tribute()
  elif randenc >=20:
    fight_tribute()
  elif randenc >=10:
    fight_monster()

def fight_monster():
  global player_health, inventory, armory, monsters
  
  monster_ID= randint(0,2)

  round = 1
  monster_health = monsters[monster_ID]['health']

  print(f"A ferocious {monsters[monster_ID]['name']} approaches! COMBAT HAS BEGUN!\n")
  while True:
    print(f"ROUND {round}")
    print("Player Health: [" + str(player_health) + "]")
    print("Monster Health: [" + str(monster_health) + "]")

    print("Type: RUN, ATTACK, or USE [item]") # gotta write code for cast
    move = input().lower().split() # converts move into a lower-case list to deal with each item in list separately
    monster_damage = sum(dice.roll(monsters[monster_ID]['damage']))
    print("\n=========================")

    if move[0] == 'use': #
      if move[1] in equipment: # checks if weapon is in your inventory
        player_damage = dice.roll(armory[move[1]]['damage'])
        print(f"You hit a {monsters[monster_ID]['name']} for {player_damage} damage!")
      if move[1] not in equipment:
        print(f"There is no {move[1]} in your equipment!")

    if move[0] == 'attack':
      player_damage = dice.roll('5d10')
      print(f"You hit a {monsters[monster_ID]['name']} for {player_damage} damage!")

    if move[0] == 'run':
      print('You made a flawless escape!')
      break

      try:
        monster_health -= int(player_damage)
      except:
        pass
      if monster_health <= 0:
        print(f"The {monsters[monster_ID]['name']} lies dead. You are victorious!\n")
        break

      print(f"A {monsters[monster_ID]['name']} hits you for {monster_damage} damage!")
      print ("=========================\n")
      round += 1
      player_health -= int(monster_damage)

      if player_health <= 0:
        print("You have been vanquished! You are dead.")
        sys.exit()

def accident():
  luckynumber= randint(0,2)
  number_list = random.sample(range(0, len(tributes)), luckynumber)
  for number in number_list:
    speech_text((f"{tributes[number]['name']} from district {tributes[number]['district']} has fallen!\n"))
    del tributes[number]

def fight_tribute():
  global player_health, inventory, armory, tributes
  
  tribute_ID= randint(0,len(tributes))

  round = 1
  tribute_health = tributes[tribute_ID]['health']

  print(f"{tributes[tribute_ID]['name']} from district {tributes[tribute_ID]['district']} approaches! FIGHT HAS BEGUN!\n")
  while True:
    print(f"ROUND {round}")
    print("Player Health: [" + str(player_health) + "]")
    print("Tribute Health: [" + str(tribute_health) + "]")

    print("Type: RUN, ATTACK, or USE [item]") # gotta write code for cast
    move = input().lower().split() # converts move into a lower-case list to deal with each item in list separately
    tribute_damage = sum(dice.roll(tributes[tribute_ID]['damage']))
    print("\n=========================")

    if move[0] == 'use': #
      if move[1] in equipment: # checks if weapon is in your equipment
        player_damage = dice.roll(armory[move[1]]['damage'])
        print(f"You hit {tributes[tribute_ID]['name']} for {player_damage} damage!")
      if move[1] not in equipment:
        print(f"There is no {move[1]} in your equipment!")

    if move[0] == 'attack':
      player_damage = dice.roll('5d10')
      print(f"You attacked {tributes[tribute_ID]['name']} for {player_damage} damage!")

    if move[0] == 'run':
      print('You made a flawless escape!')
      break
      
    try:
      tribute_health -= int(player_damage)
    except:
      pass
    if tribute_health <= 0:
      print(f"{tributes[tribute_ID]['name']} lies dead. You are victorious!\n")
      del tributes[tribute_ID]
      break

    print(f"A {tributes[tribute_ID]['name']} hits you for {tribute_damage} damage!")
    print ("=========================\n")
    round += 1
    player_health -= int(tribute_damage)

    if player_health <= 0:
      speech_text("You have been vanquished! You are dead.\n")
      sys.exit()

def checkvictory():
  if len(tributes) == 0:
    speech_text(f"Congratulations {name} from district {district}, you are the winner of this year's Hunger Games!\n")
    sys.exit()

def game():
  global player_health, inventory, current_location, equipment
  weapon_list =['sword', 'bow&arrow', 'knife', 'crossbow', 'axe']
  while True:   # MAIN INFINITE LOOP
    playerinfo()
    showStatus()
    checkvictory()
    
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
        accident()
        random_encounter()
      else:
        print("YOU CAN'T GO THAT WAY!")
    if move[0] == 'use':
      item = move[1].lower()
      if item in food.keys() and item in inventory:
        print(f"You used {item}. Your health is changed to {player_health+ food[item]}")
        player_health += food[item]
        inventory.remove(item)
        if player_health <= 0:
          print("You have been vanquished! You are dead.")
          sys.exit()
        
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
  welcome_text()
  showInstructions()
  game()

if __name__ == '__main__':
    main()

