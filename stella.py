import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

engine.setProperty('rate',150) 
engine.runAndWait()


def speak(str):
     engine.say(str)
     engine.runAndWait()

def wishMe():
     hour=int(datetime.datetime.now().hour)
     if hour>=0 and hour<=12:
          speak("Good  Morning People!")
     
     elif hour>=12 and hour<=17:
          speak("Good Afternoon People!")

     else:
          speak("Good Night People!")

     speak("Hello, I am Stella, How may I help you Sir?")

def takeCommand():
    #It takes microphone input from the user and returns string output

     r = sr.Recognizer()
     with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        str = r.listen(source) 
        
     try: 
        print("Recognizing...")    
        query = r.recognize_google(str, language='en-in') 
        print(f"User said: {query}\n")  #User query will be printed.

     except Exception as e:
            
        print("Say that again please...")  
        return " Oops!! voice not recognised" 
     return query


if __name__ == "__main__":
     wishMe()
     while True:
     
       
        query = takeCommand().lower() 

        
       
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

       
        elif 'open google' in query:
            webbrowser.open("google.com")

       
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        
        
        elif 'play music' in query:
            music_dir = 'H:\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))

        
        
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)



  


