import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150) 

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command(): 
    try:
        with sr.Microphone() as source:
            print('I am listening, Say something...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
            return command

    except sr.RequestError:
        print('Sorry, my speech service is down')
        talk('Sorry, my speech service is down')

    except sr.UnknownValueError:
        print('Sorry, I did not catch that')
        talk('Sorry, I did not catch that')

    return ""


def run_alexa():
    command = take_command()
    if not command:
        return
    print('Me:', command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        print('Playing' + song)
        pywhatkit.playonyt(song)

    elif 'search' in command:
        search = command.replace('search', '')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('Here is what I found for ' + search)
        talk('Here is what I found for ' + search)
    
    elif 'map' in command:
        location = command.replace('map', '')
        url = 'https://google.nl/maps/place/' + location
        webbrowser.get().open(url)
        print('Here is the map of ' + location)
        talk('Here is the map of ' + location)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)

    elif 'tell me about' in command:
        ask = command.replace('tell me about', '')
        try:
            info = wikipedia.summary(ask, sentences=2)
            print(info)


            
            talk(info)
        except wikipedia.exceptions.PageError:
            print('Sorry, I could not find information on that topic.')
            talk('Sorry, I could not find information on that topic.')
        except wikipedia.exceptions.DisambiguationError as e:
            print('There are multiple results for this topic. Please be more specific.')
            talk('There are multiple results for this topic. Please be more specific.')

    elif 'sex' in command:
        talk('Hmm...yes we will do sex at night.')

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'who are you' in command:
        talk('I am Alexa, your 24/7 virtual assistant. If you are bored, I can tell you a joke, play YouTube videos for you, and much more.')

    elif 'thank you' in command:
        talk('You are welcome. Anything else you want me to do?')

    elif 'goodbye' in command or 'exit' in command:
        talk('Goodbye, Smarty. See you later, Alligator.')
        exit()

    else:
        print('Sorry, I did not get that')
        talk('Sorry, I did not get that')
        print("sorry can you speak again")






while True:     
    run_alexa()
