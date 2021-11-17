import speech_recognition as sr
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            tron_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            tron_speak('Sorry, I did not get that')
        except sr.RequestError:
            tron_speak('Sorry, my speech service is down')
        return voice_data

def tron_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 100000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        tron_speak('My name is Tron')
    if 'what time is it' in voice_data:
        tron_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        tron_speak('Here is what I found for ' + search)
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
    if 'activate' in voice_data:
        tron_speak('Activating youtube')
        search = record_audio('')
        url = 'https://youtube.com/search?q=' + search
        webbrowser.get().open(url)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        tron_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        tron_speak('exiting')
        exit()


time.sleep(1)
tron_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)