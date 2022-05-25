import pyttsx3
import wikipedia
import os
import smtplib
import webbrowser
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good Evening")

    speak("What can I do for you ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('shivaadhikari499@gmail.com', 'softwarica499')
    server.sendmail('shivaadhikari499@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open('youtube.com')

        elif 'facebook' in query:
            webbrowser.open('facebook.com')

        elif 'time please' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak(f"Hello Aadarsh, the time is {time}")

        elif 'i love you' in query:
            try:
                speak("I love you too my Shiva baby")
            except Exception as e:
                speak("Cannot pronounce that")
                continue

        elif 'open code' in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'shivaadhikari499@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print("Sorry the email is not send")

        elif 'quit' in query:
            exit()
