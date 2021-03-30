#!/usr/bin/env python3
heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "he's a wizard",
    "archenemy": "Voldemort",},
"agent fitz":
    {"real name": "Leopold Fitz",
    "powers": "intelligence",
    "archenemy": "Hydra",}
        }
herolist = ["wolverine","harry potter", "agent fitz"]
hero = input("Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz)").lower
if hero in herolist:
    hero = input("Input hero not in our list, please type again")
herocap = hero.capitalize)
stats = input("Which statistic do you want to know about? (real name, powers, archenemy)")

output = heroes[hero][stats]
print(f"{herocap}'s {stats} is {output}")
