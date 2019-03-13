# from gtts import gTTS
import os
from gtts import gTTS
from random import *

# initialize the string
str = "you are a"

# read file and write to an empty list
adjectives = []
with open("english-adjectives.txt") as f1:
    for i in f1:
        adjectives.append(i.strip('\n'))

f1.close()
x = randint(0, 1346)  # generate a rand int in range of file length

nouns = []
with open("english-nouns.txt") as f2:
    for sen in f2:
        nouns.append(sen.rstrip('\n'))
f2.close()
y = randint(0, 1524)

# detect vowels to change between "a" or "an"
vowels = ['a', 'e', 'i', 'o', 'u']
if adjectives[x][0] in vowels:
    str += "n"

# string together the words to construct sentence
str = str + " " + adjectives[x] + " " + nouns[y]

print(str)

# language to convert
language = 'en'

# build the gTTS object
myobj = gTTS(text=str, lang=language, slow=False)

# save the converted audio in a mp3 file
myobj.save("URA.mp3")

# play the converted file
os.system("mpg321 URA.mp3")

# another text to speech library
import pyttsx3
engine = pyttsx3.init()
engine.say("Indeed I am not!")
engine.runAndWait()
voices = engine.getProperty('voices')