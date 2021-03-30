#!usr/bin/env python
challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

eyes = challenge[2][1]
goggles = challenge[2][0]
nothing = challenge[3]
challenge_print = f"My {eyes}! The {goggles} do {nothing}!"

eyes2 = trial[2]["goggles"]
goggles2 = trial[2]["eyes"]
nothing2 = trial[3]
trial_print = f"My {eyes2}! The {goggles2} do {nothing2}!"

eyes3 = nightmare[0]["user"]["name"]["first"]
goggles3 = nightmare[0]["kumquat"]
nothing3 = nightmare[0]["d"]
nightmare_print = f"My {eyes3}! The {goggles3} do {nothing3}!"

print(challenge_print)
print(trial_print)
print(nightmare_print)

