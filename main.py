import os

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import calendar





listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command
def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calender.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = ['january','february','march','april','may','june','july','august','september','october','november','december',]




def run_alexa():
       command = take_command()
       print(command)
       if 'play' in command:
           song = command.replace('play','')
           talk('playing ' + song)
           pywhatkit.playonyt(song)
       elif'time' in command:
           time = datetime.datetime.now().strftime('%H:%M %p')
           print(time)
           talk('current time is '+time)
       elif'who is' in command:
           person = command.replace('who is', '')
           info = wikipedia.summary(person, 1)
           print(info)
           talk(info)
       elif'open'in command:
           if 'chrome' in command:
               os.startfile('C:\Program Files\Google\Chrome\Application\chrome')
               talk ('opening google chrome')
       elif'where is' in command:
           ind = command.lower().split().index('is')
           location = command.split()[ind + 1:]
           url = 'https://www.google.com/maps/place/' + ''.join(location)
           talk('this is where' + str(location) +'is.')
           webbrowser.open(url)
       elif 'youtube' in command:
           ind = command.lower().split().index('youtube')
           search = command.split()[ind + 1:]
           webbrowser.open('http://www.youtube.com/results?search_query=' + '+'.join(search))
           talk('opening' + str(search) + 'on youtube')
       elif 'search' in command:
           ind = command.lower().split().index('search')
           search = command.split()[ind + 1:]
           webbrowser.open('https://www.google.com/search?q=' + '+'.join(search))
           talk('searching' + str(search) + 'on google')


       elif 'joke' in command:
           talk(pyjokes.get_joke())



       else:
           talk('please say the command again...')


while True:
    run_alexa()




