#!usr/bin/env python3
import sys, os

song = {
  "Hey Jude":{
    "don't make it bad":"take a sad song and make it better", "don't be afraid":"you were made to go out and get her", "don't let me down":"you have found her, now go and get her"},
  "remember to":{
    "let her into" : "your heart",
    "let her under" : "your skin"},
  "then you":{
    "can start" : "to make it better",
    "begin":"to make it better"},
  "better better better better better waaaaa" : "na na na na na na na na ...."
}
print("type the line number to keep singing")
#list to store all selected lyrics
lyrics = []

def printlyrics(lyrics):
  os.system('clear')
  for item in lyrics:
    print(item)

#check user input for quit
def checkquit(selection):
  if selection == "q":
    sys.exit()

def keepsinging(song):
  #loop through all keys in the song
  words = list(song.keys())
  for word in words:
    print(word)
    lyrics.append(word)
    if type(song[word]) is dict:
      sentences = list(song[word].keys())
      #list for input validation
      indexlist = ["q"]
      for index, sentence in enumerate(sentences):
        indexlist.append(str(index + 1))
        print(index+1, sentence)
      selection = input("number: ")
      checkquit(selection)
      #input validation
      while selection not in indexlist:
        selection = input("Your input is not a valid number, please type in the correct response: ")
        checkquit(selection)
      lyrics.append(sentences[int(selection)-1])
      newline = song[word][sentences[int(selection)-1]]
      lyrics.append(newline)
      printlyrics(lyrics)
    else:
      lyrics.append(song[word])
      printlyrics(lyrics)
      keepsinging(song)

keepsinging(song)
