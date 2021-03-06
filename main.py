from gtts import gTTS
import os
import requests
from mutagen.mp3 import MP3
import speech_recognition as sr
import time


# A BUNCH OF EDITABLE VARIABLES!
TTSlanguage = "en"
TTSAccent = "co.uk"
yourName = "YOUR NAME HERE"


def hi():
    output('Hi, ' + yourName + '. What would you like to know?')


def listen():
    # search_duckduckgo("what is bitcoin")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            search_duckduckgo(text)
        except:
            output("Sorry I can't do that right now")


def search_duckduckgo(text):
    searchableText = text.replace(" ", "+")
    duckDuckGourl = \
        "https://api.duckduckgo.com/?q=" + searchableText + "&format=json&t=simpliestBotEver"
    try:
        print(duckDuckGourl)
        response = requests.get(duckDuckGourl).json()
        answerLong = response['AbstractText']
        answer = answerLong.split(". ")
        output('The answer to your question: ' + text + '. Is ' + answer[0])
    except:
        output("I'm sorry. I don't know that")


def output(outputtext):
    print(outputtext)
    output = gTTS(text=outputtext, lang=TTSlanguage, slow=False, tld=TTSAccent)
    output.save("output.mp3")
    print("System will now stop listening for just over: " + str(MP3("output.mp3").info.length) + " seconds.")
    os.system("start output.mp3")
    time.sleep(MP3("output.mp3").info.length + 1)
    listen()


if __name__ == '__main__':
    hi()