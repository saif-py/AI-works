import speech_recognition as sr
import os
from subprocess import call
import webbrowser

listt = []


def OpenApplication(listt):
    if listt[0].lower() == 'open':
        a = os.popen("""
           aptitude -F' * %p -> %d ' --no-gui --disable-columns search '?and(~i,!?section(libs), 
           !?section(kernel), !?section(devel))'
            """).readlines()
        for i in a:
            if i.__contains__(listt[1].lower()):
                print(i)
                i = i.split()
                print("opening " + i[1])
                call(i[1])


r = sr.Recognizer()
while True:
    with sr.Microphone() as source:

        print("listening...")
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
        import webbrowser

        search = ''
        for a in listt:
            search = search + ' ' + a

        webbrowser.open('https://www.google.com.tr/search?q=' + search.strip())

    elif listt[0].lower() == 'open':
        OpenApplication(listt)
    elif listt[0].lower() == 'play':
        from googlesearch import search
        query = ''
        for a in listt:
            query = query + ' ' + a
        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
            k = j.split('/')
            if k[2] == 'www.amazon.com' or k[2] == 'www.netflix.com' or k[2] == 'www.primevideo.com':
                webbrowser.get('firefox').open_new_tab(j)
                webbrowser.open(j)
                break
