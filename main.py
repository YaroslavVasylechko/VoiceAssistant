import speech_recognition as sr
import pyttsx3
import sys
import time
import subprocess
import urllib
import os
from bs4 import BeautifulSoup as soup
from weather import get_weather
from wikipedia_search import *


def talk(words):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[3].id)
    engine.setProperty("rate", 145)
    engine.say(words)
    engine.runAndWait()


talk('Hi, im your personal voice assistant!')


def command():
    """
    This function converts your speech to text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I\'m listening')
        r.adjust_for_ambient_noise(source, duration=0.5)  # duration = 0.5
        audio = r.listen(source, timeout=5)


    try:
        task = r.recognize_google(audio).lower()  # language = 'ru-RU'
        print(f'[log] {task}')
    except sr.UnknownValueError:
        talk('Please, repeat!')
        task = command()
    except sr.RequestError:
        talk('I don\'t have access to google servers to recognize your speech!')

    return task


def working(task):
    if 'hello' in task:
        talk('Hello')
    elif 'stop' in task or 'goodbye' in task:
        talk('Have a good day!')
        sys.exit()
    elif 'open' in task:
        if 'chrome' in task or 'browser' in task:
            subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        elif 'explorer' in task:
            subprocess.Popen('C:/Windows/explorer.exe')
    elif 'close' in task:
        if 'chrome' in task or 'browser' in task:
            os.system('TASKKILL /F /M chrome.exe')
    # wikipedia
    elif 'what' in task or 'who' in task:
        talk(request_to_wiki(task))
    # weather
    elif 'weather' in task:
        talk('I know the weather of the following countries: USA, Poland and Germany. Which country do you want to know'
             'the weather?')
        country = command()
        talk('What city weather do you want to know?')
        city = command()
        talk(get_weather(country, city))


while True:
    working(command())
