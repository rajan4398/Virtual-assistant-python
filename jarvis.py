import pyttsx3 as pt
import datetime
import speech_recognition as sr
import wikipedia as wk
import os
import random
import webbrowser as wb
engine = pt.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newRAte = 145
engine.setProperty('rate', newRAte)
print(engine.getProperty('rate'))

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour <=18:
        speak("Good evening")
    else :
        speak("Good Evening")


def About():
    speak("Welcome User")
    speak("How are You ")
    speak("I am your voice assistant")

def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        print("Speak...")
        r.pause_threshold = 0.9
        audio = r.listen(src)
    try:
        speak("Recognizing....")
        quert = r.recognize_google(audio, language='en=in')
        speak("you said")
        print(f"{quert}\n")
        speak(quert)
        return quert

    except Exception as e:
        speak("say that again please....")
        exit

def search(query):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    getchrome = wb.get(chrome_path)
    if "wikipedia" in query:
        speak("searching in wikipedia...")
        query = query.replace("wikipedia","")
        result = wk.summary(query,sentences=1)
        speak(f"according  to wikipedia ")
        speak(result)
        url = "https://www.google.com/search?q="+query+"&rlz=1C1CHBF_enIN897IN897&oq="+query+"&aqs=chrome..69i57j0l2j69i64.12279j1j7&sourceid=chrome&ie=UTF-8"
        getchrome.open(url)
        print("1")
    

    elif "youtube" in query:
        query = query.replace("video","")
        query = query.replace("in youtube","")
        query = query.replace("on youtube","")
        query = query.replace("youtube","")
        url = query.strip()
        url = "https://www.youtube.com/results?search_query="+url
        getchrome.open(url)
        print("2")

    elif "search"  in query:
        query = query.replace("search","")
        query = query.replace("browser","")
        url = "https://www.google.com/search?q="+query+"&rlz=1C1CHBF_enIN897IN897&oq=google.com%5Chow&aqs=chrome.3.69i58j69i57j0l3.20935j0j4&sourceid=chrome&ie=UTF-8"
        print(url)
        getchrome.open(url)
        print("3")

    elif "classroom" in query:
        print("classroom")
        url = "https://classroom.google.com/"
        getchrome.open(url)
    
    elif "gmail" in query or "email" in query:
        if "new" in query :
            print("new")
            url = "https://mail.google.com/mail/u/0/#inbox?compose=new"
            getchrome.open(url)
        else :
            print("gmail")
            url="https://mail.google.com/mail/u/0/#inbox"
            getchrome.open(url)

    else :
        query = query.replace(" ","+")
        url = "https://www.google.com/search?q="+query+"&rlz=1C1CHBF_enIN897IN897&oq=google.com%5Chow&aqs=chrome.3.69i58j69i57j0l3.20935j0j4&sourceid=chrome&ie=UTF-8"
        print(url)
        getchrome.open(url)
        print("4")


if __name__ == '__main__':
    wishMe()
    About()
    speak("Listening...")
    i = 0
    if i == 0:
        query = takecmd().lower()
        if 'exit' in query:
            speak("exiting")
            exit()

        elif "search"  in query:
            print("search")
            url =  query.strip()
            speak(f"searching in {url}")
            search(url)

        elif "music"  in query:
            path = "E:\\Songs\\Music"   
            songs = os.listdir(path)
            x = len(songs)
            for i in range(x):
                print(songs[i])
            r = random.randint(1,x)
            print("playing song ",songs[r])
            speak(f"playing {songs[r]}")
            os.startfile(os.path.join(path,songs[r]))
    
        else :
            print("else")
            speak("searching")
            search(url)
            print("123")
        speak("Do you want to continue ")
        speak("say y or yes to continue and anything to exit()")
        repeat = takecmd().lower()
        repeat = "No"
        if "y" or "yes" in repeat:
            i = 0
        else :
            i = -1
                                