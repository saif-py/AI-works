import speech_recognition as sr
import os
from subprocess import call
import webbrowser
import pyautogui
import time
import sys
import pyttsx3
from gtts import gTTS

listt = []


def OpenApplication(listt):
    if listt[0].lower() == 'open':
        command = os.popen("""
           aptitude -F' * %p -> %d ' --no-gui --disable-columns search '?and(~i,!?section(libs), 
           !?section(kernel), !?section(devel))'
            """).readlines()
        for i in command:
            if i.__contains__(listt[1].lower()):
                print(i)
                i = i.split()
                print("opening " + i[1])
                call(i[1])


def say(line):
    engine = pyttsx3.init()
    # rate of speech
    newVoiceRate = 160
    engine.setProperty('rate', newVoiceRate)
    voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[17].id)
    engine.setProperty('voice', 'english+f16')
    # testing
    engine.say(line)
    engine.runAndWait()


r = sr.Recognizer()
say("hello! I'm U.B! the virtual assistant! how can i help you")
while True:
    with sr.Microphone() as source:

        print("listening....")
        audio = r.record(source, duration=3)
        try:
            str = r.recognize_google(audio)
        except:
            continue
    print(str)
    listt = str.split()
    if listt[0].lower() == 'search':
        import webbrowser

        search = ''
        for a in listt[1:]:
            search = search + ' ' + a

        webbrowser.open('https://www.google.com.tr/search?q=' + search.strip())
    elif listt[0].lower() == 'what' or listt[0].lower() == 'who' or listt[0].lower() == 'when' or \
            listt[0].lower() == 'how' or listt[0].lower() == 'is':

        search = ''
        for a in listt:
            search = search + ' ' + a

        webbrowser.open('https://www.google.com.tr/search?q=' + search.strip())

    elif listt[0].lower() == 'open':
        OpenApplication(listt)
    elif listt[0].lower() == 'hello' or listt[0].lower() == 'hi' or listt[0].lower() == 'hai':
        mytext = 'hello! i am UB'
        say(mytext)
        language = 'en'

        myobj = gTTS(text=mytext, lang=language, slow=False)

        myobj.save("welcome.mp3")
        os.system("welcome.mp3")

    elif listt[0].lower() == 'play':
        if listt[1].lower() == 'music':
            say("opening music player")
            import sys

            sys.path.insert(0, '/home/saif/PycharmProjects/music_player')
            import music_player
            music_player()
        else:

            from googlesearch import search

            query = ''
            for a in listt:
                query = query + ' ' + a
            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                k = j.split('/')
                if k[2] == 'www.amazon.com' or k[2] == 'www.netflix.com' or k[2] == 'www.primevideo.com':
                    webbrowser.get('firefox').open_new_tab(j)

                    break
                if k[2] == 'www.youtube.com':
                    webbrowser.open_new_tab(j)
                    break

    elif listt[0].lower() == 'exit' or listt[0].lower() == 'quit':
        say('good byee...')
        quit()
    else:
        command = os.popen(str).readlines()
        if command.__contains__('not found'):
            search = ''
            for a in listt:
                search = search + ' ' + a

            webbrowser.open('https://www.google.com.tr/search?q=' + search.strip())
        else:
            print(command)
