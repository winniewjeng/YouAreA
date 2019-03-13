# from gtts import gTTS
import os
from gtts import gTTS
from random import *
# # another text to speech library
import pyttsx3


# read file and write to an empty list
adjectives = []
with open("english-adjectives.txt") as f1:
    for i in f1:
        adjectives.append(i.strip('\n'))

f1.close()


nouns = []
with open("english-nouns.txt") as f2:
    for sen in f2:
        nouns.append(sen.rstrip('\n'))
f2.close()

def isVowel(ch='a'):
    # detect vowels to change between "a" or "an"
    vowels = ['a', 'e', 'i', 'o', 'u']
    if ch in vowels:
        return True
    return False


r = randint(0, 10)



while r is not 0:
    # initialize the string
    str = "you are a"
    # init an accusation string
    x = randint(0, 1346)  # generate a rand int in range of adj list length
    y = randint(0, 1524)
    # check adjective's first char to determine if vowel
    if isVowel(adjectives[x][0]):
        str = str + "n " + adjectives[x] + " " + nouns[y]
    # construct a new accusation string
    else:
        str = str + " " + adjectives[x] + " " + nouns[y]
    # string together

    print(str)

    # language to convert
    language = 'en'
    # build the gTTS object
    myobj = gTTS(text=str, lang=language, slow=False)
    # save the converted audio in a mp3 file
    myobj.save("URA.mp3")
    # play the converted file
    os.system("mpg321 URA.mp3")

    # condition loop
    r = randint(0, 10)


engine = pyttsx3.init()

engine.say("Indeed I am not!")
engine.runAndWait()
voices = engine.getProperty('voices')