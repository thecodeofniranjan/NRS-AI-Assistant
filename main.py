import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12: speak("Good Morning!")
    elif hour>=12 and hour<18: speak("Good Afternoon!")   
    else: speak("Good Evening!")  
    speak("Jarvis is online. How can I help you today?")       

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
    except Exception:
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, it is {strTime}")

        # --- CUSTOM COMMANDS ---
        elif 'open my game' in query:
            # REPLACE THIS with the path to your actual game (.exe) file
            gamePath = "C:\\Path\\To\\Your\\Game.exe"
            os.startfile(gamePath)
            speak("Launching your game now.")

        elif 'open work folder' in query:
            # REPLACE THIS with your folder path
            folderPath = "C:\\Users\\YourName\\Documents\\Work"
            os.startfile(folderPath)
            speak("Opening your work folder.")

        elif 'exit' in query:
            speak("System offline.")
            break
