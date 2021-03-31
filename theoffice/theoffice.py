#!/usr/bin/env python3
characters = {
"ESTJ" : "Dwight - You are hardworking traditionalists, eager to take charge in organizing projects and people. Orderly, rule-abiding, and conscientious, ESTJs like to get things done, and tend to go about projects in a systematic, methodical way.",
"ESTP" : "Andy - You are energetic thrillseekers who are at their best when putting out fires, whether literal or metaphorical. They bring a sense of dynamic energy to their interactions with others and the world around them.",
"ESFJ" : "Erin - You are conscientious helpers, sensitive to the needs of others and energetically dedicated to their responsibilities. They are highly attuned to their emotional environment and attentive to both the feelings of others and the perception others have of them.",
"ESFP" : "Michael - You are vivacious entertainers who charm and engage those around them. They are spontaneous, energetic, and fun-loving, and take pleasure in the things around them: food, clothes, nature, animals, and especially people.",
"ENTJ" : "Robert - You are strategic leaders, motivated to organize change. They are quick to see inefficiency and conceptualize new solutions, and enjoy developing long-range plans to accomplish their vision. They excel at logical reasoning and are usually articulate and quick-witted.",
"ENTP" : "Ryan - You are inspired innovators, motivated to find new solutions to intellectually challenging problems. They are curious and clever, and seek to comprehend the people, systems, and principles that surround them.",
"ENFJ" : "Kelly - You are idealist organizers, driven to implement their vision of what is best for humanity. They often act as catalysts for human growth because of their ability to see potential in other people and their charisma in persuading others to their ideas.",
"ENFP" : "Kevin - You are people-centered creators with a focus on possibilities and a contagious enthusiasm for new ideas, people and activities. Energetic, warm, and passionate, ENFPs love to help other people explore their creative potential.",
"ISTJ" : "Daryl - You are responsible organizers, driven to create and enforce order within systems and institutions. They are neat and orderly, inside and out, and tend to have a procedure for everything they do.",
"ISTP" : "Stanley - You are observant artisans with an understanding of mechanics and an interest in troubleshooting. They approach their environments with a flexible logic, looking for practical solutions to the problems at hand.",
"ISFJ" : "Phyllis - You are industrious caretakers, loyal to traditions and organizations. They are practical, compassionate, and caring, and are motivated to provide for others and protect them from the perils of life.",
"ISFP" : "Pam - You are gentle caretakers who live in the present moment and enjoy their surroundings with cheerful, low-key enthusiasm. They are flexible and spontaneous, and like to go with the flow to enjoy what life has to offer.",
"INTJ" : "Angela - You are analytical problem-solvers, eager to improve systems and processes with their innovative ideas. They have a talent for seeing possibilities for improvement, whether at work, at home, or in themselves.",
"INTP" : "Creed - You are philosophical innovators, fascinated by logical analysis, systems, and design. They are preoccupied with theory, and search for the universal law behind everything they see. They want to understand the unifying themes of life, in all their complexity.",
"INFJ" : "Toby - You are creative nurturers with a strong sense of personal integrity and a drive to help others realize their potential. Creative and dedicated, they have a talent for helping others with original solutions to their personal challenges.",
"INFP" : "Jim - You are imaginative idealists, guided by their own core values and beliefs. To a Healer, possibilities are paramount; the reality of the moment is only of passing concern. They see potential for a better future, and pursue truth and meaning with their own flair.",
}

def assignletter(letter1, letter2, answer):
  if answer == "yes":
    return letter1
  elif answer == "no":
    return letter2
  else:
    answer1 = input("Your input is not valid, please type in [Yes] or [No] ")
    return assignletter(letter1, letter2, answer1)

result = ""
print("Answer a few questions and find out which character from 'The Office' are you most like? ")

#Yes -> E, No -> I
question1 = input("You regularly make new friends. [Yes]/[No]? ").lower()
result += assignletter("E", "I", question1)

#Yes -> S, No -> N
question2 = input("You prefer to do things the established way, instead of trying out new ideas? [Yes]/[No]? ").lower()
result += assignletter("S", "N", question2)

#Yes -> F, No -> T
question3 = input("Seeing other people cry can easily make you feel like you want to cry too. [Yes]/[No]? ").lower()
result += assignletter("F", "T", question3)

#Yes -> J, No -> P
question4 = input("You like to use organizing tools like schedules and lists. [Yes]/[No] ").lower()
result += assignletter("J", "P", question4)

print("Your result is: ")
print(characters[result])

