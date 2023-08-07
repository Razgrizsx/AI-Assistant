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

#Browser

firefox = r"C:\Program Files\Mozilla Firefox\firefox.exe"
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox))


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
        print("Couldn't understand")
        speak("Couldn't understand")
        print(exception)
        return "Couldn't understand"
    return query

def speak(text, rate=120):  #rate of scpeech and text
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait() 

def wikipedia_search(query = ''):
    results = wikipedia.search(query)
    if not results:
        print("No results")
        return "No results"
    try:
        wiki = wikipedia.page(results[0])
    except wikipedia.DisambiguationError as err:
        wiki = wikipedia.page(err.options[0])
    print(wiki.title)
    summary = str(wiki.summary)
    return summary    

if __name__ == "__main__":
    speak('Welcome')

    while True: #parse the input into a list
        query = parseCommand().lower().split() #split separates

        if query[0] == activationWord:
            query.pop(0)   #if the first word is the activation word then remove it

            if query[0] == 'say':
                if 'hello' in query:
                    speak("Greetings, all.")
                else:
                    query.pop(0)
                    speech = ' '.join(query)
                    speak(speech)

#WebBrowsing


        if query[0] == 'go' and query[1] == 'to':
            speak("Opening...")
            query = ' '.join(query[2:])
            webbrowser.get('firefox').open_new(query)

        if query[0] == 'question':
            query = ' '.join(query[1:])
            speak("Querying...")
            speak(wikipedia_search(query))
            