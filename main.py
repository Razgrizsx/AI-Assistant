from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

#Initializing speech engine.

engine = pyttsx3.init()    #initializing, choosing voices, setting the voices as a property, choosing activation word.
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id) #1 for female voices, change to 0 for male.
activationWord = 'computer'

def parseCommand(): #listening
    listener = sr.Recognizer()
    print('Listening')

    with sr.Microphone() as source:  #setting sound source
        listener.pause_threshhold = 2
        input_speech = listener.listen(source)
    
    try:
        print('Capturing speech...')  
        query = listener.recognize_google(input_speech, language='en_gb') #audio recognition using google api
        print(f'You said {query}')
    except Exception as exception:
        print("Couldn'tunderstand")
        speak("Couldn'tunderstand")
        print(exception)
        return None
    return query

def speak(text, rate=120):  #rate of scpeech and text
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait() 


if __name__ == "_main_":
    speak('Welcome')

    while True: #parse the input into a list
        query = parseCommand().lower().split() #split separates

        if query[0] == activationWord:
            query.pop(0)   #if the first word is the activation word the remove it
            
