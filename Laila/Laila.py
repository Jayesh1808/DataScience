import bs4
import speech_recognition as sr   # for speaking
import pyttsx3    # for voice.
import pywhatkit     # for youtube
import datetime      # for date
import wikipedia     # for searching
import random
import pyjokes
import urllib.request
import operator
import math
import sys
import requests, webbrowser
from bs4 import BeautifulSoup

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def you():
    try:
        s = ['I am Good. Thanks Dear..','I\'m preety Good, Thanks..','Hi, I can\'t Complaint. Thanks for asking ','not too shabby..Thanks for asking..']
        return random.choice(s)
    except:
        pass

def rel():
    try:
        s=['I am in a relationship with wifi..','I\'m married to the idea of helping people..','If you are asking for a date sorry, I have a headache']
        return random.choice(s)
    except:
        pass

def love():
    try:
        s=['I think You\'re Pretty.','well, I enjoy spending quality time with you.','You have my utmost admiration']
        return random.choice(s)
    except:
        pass

def doing():
    try:
        s=['I\'m painting a self-portait. It\'s rather abstract.','I\'m trying to be a good guide for you. ','I\'m learning new words, like "cattyampus", You could just say "diagonal",but that\'s not as fun.','I\'m learning new tricks. Try asking me what I can do for you.']
        return random.choice(s)
    except:
         pass

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Ammmm Hmmmmm..... I am listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'laila' in command:
                command = command.replace('laila', '')
                # print(command)
    except:
        pass
    return command

def addition():
    try:
        with sr.Microphone() as source:
            talk('Say First Number :')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            num1 = command
            n1 = int(command)
            print('Your First Number :' + num1)
            talk('Say Second Number :')

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            num2 = command
            n2 = int(command)
            print('Your Second Number :' + num2)
            n3 = n1 + n2
            sum1 = str(n3)
            return sum1
    except Exception as e:
        print(e)

def subtract():
    try:
        with sr.Microphone() as source:
            talk('Say First Number :')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            num1 = command
            n1 = int(command)
            print('Your First Number :' + num1)
            talk('Say Second Number :')

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            num2 = command
            n2 = int(command)
            print('Your Second Number :' + num2)
            n3 = n1 - n2
            sub1 = str(n3)
            return sub1
    except Exception as e:
        print(e)

def run_laila():
    command = take_command()
    print(command)

    if 'add this' in command:
        sol = addition()
        talk("sum is "+sol)
        print("sum is "+sol)

    elif 'gmail' in command:
        webUrl = webbrowser.open_new('https://mail.google.com/mail/u/0/#inbox')
        print(webUrl)

    elif 'subtract this' in command:
        sol1 =subtract()
        talk("Difference is"+sol1)
        print("Difference is"+sol1)

    elif 'difference' in command:
        sol1=subtract()
        talk("Difference is" + sol1)
        print("Difference is" + sol1)

    elif 'hi' in command:
        talk('Hi, tell me how can i help you')
    elif 'hello' in command:
        talk('Hi, tell me how can i help you')

    elif'hi there' in command:
        talk('Hi, tell me how can i help you')

    elif'hello there' in command:
        talk('Hi, tell me how can i help you')

    elif 'what are you doing' in command:
          do=doing()
          talk(do)
          print(do)

    elif 'what you doing' in command:
          do=doing()
          talk(do)
          print(do)

    elif'doing what you are' in command:
          do=doing()
          talk(do)
          print(do)

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'song' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif'play this song' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'who am i' in command:
        talk('You are Jayesh, my creator..')
        print('You are Jayesh, my creator..')

    elif 'who are you' in command:
        talk('I\'m Laila, Your Assistant. ')
        talk('How can i help you ?')
        print('I\'m Laila, Your Assistant.. ')


    elif 'search this song' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'number' in command:
         number =random.randrange(0,100)
         talk('A random number between 0 and 100 is')
         print('A random number between 0 and 100 is')
         talk(number)
         print(number)

    elif 'how are you' in command:
        a =you()
        talk(a)
        print(a)


    elif 'how' in command:
        talk('Searching' + command)
        info = wikipedia.summary(command, 2)
        print(info)
        talk(info)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what' in command:
        talk('Searching'+command )
        info = wikipedia.summary(command, 1)
        print(info)
        talk(info)

    elif 'can you tell me' in command:
        talk('Searching' + command)
        info = wikipedia.summary(command, 1)
        print(info)
        talk(info)


    elif 'where' in command:
        talk('Searching' + command)
        info = wikipedia.summary(command, 2)
        print(info)
        talk(info)

    elif 'search' in command:
        person = command.replace('search', '')
        talk('Searching' + person)
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'meaning' in command:
        talk('Searching'+command )
        info = wikipedia.summary(command, 1)
        print(info)
        talk(info)

    elif 'do you love me' in command:
        lov = love()
        print(lov)
        talk(lov)
    elif 'who' in command:
        talk('Searching'+command )
        info = wikipedia.summary(command, 2 )
        print(info)
        talk(info)

    elif 'who is the your owner' in command:
        talk('You are Jayesh, my creator..')
        print('You are Jayesh, my creator..')

    elif 'who is the creator' in command:
        talk('You are Jayesh, my creator..')
        print('You are Jayesh, my creator..')


    elif 'date' in command:
        r =rel()
        talk(r)
        print(r)

    elif 'are you single' in command:
        r =rel()
        talk(r)
        print(r)

    elif 'are you dating someone' in command:
        r =rel()
        talk(r)
        print(r)

    elif 'joke' in command:
        x=pyjokes.get_joke()
        talk(x)
        print(x)


    elif 'exit' in command:
        talk('Have a nice day, bye')
        print('Have a nice day, bye')
    #     # breakpoint()

    elif 'bye' in command:
        talk('Have a nice day, bye')
        print('Have a nice day, bye')

    # elif 'zmxnmxnmcbjsjx' not in command:
    #     res = requests.get('https://google.com/search?q='+''.join(command[1:]))
    #     res.raise_for_status()
    #     soup = bs4.BeautifulSoup(res.text,"html.parser")
    #     linkEle = soup.select('.r a')
    #     linkToOpen =  min(3, len(linkEle))
    #     for i in range(linkToOpen):
    #         sol=webbrowser.open('https://google.com'+linkEle[i].get('href'))
    #         talk('Searching on web....')
    #         print(sol)

    elif 'fhidfhkjfhfkhidf' not in command:
        webb = webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open_new(command)
        talk('Searching this on web...')
        print(webb)

    else:
        talk('May Be that\'s beyond my abilities right now..')
        print('May Be that\'s beyond my abilities right now..')

engine.say('Hi, I am Laila. Your Assistant..')
engine.say('How can I help you.?')
print('Hi, I am Laila. Your Assistant..')
print('How can I help you.?')
engine.runAndWait()

while True:
  run_laila()

