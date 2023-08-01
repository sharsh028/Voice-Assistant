import os
import pyttsx3 
import pyjokes
import datetime
import pywhatkit
import wikipedia
import speech_recognition as sr

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Harsh")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Harsh")

    else:
        speak("Good Evening Harsh")

    speak("How may I help you?")

def takeCommand():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print('Command:', command)
    except sr.UnknownValueError:
        print('Sorry, I could not understand.')
    except sr.RequestError as e:
        print('Sorry, there was an issue with the speech recognition service.')
    return command

def play_song(command):
    song = command.replace('play', '')
    speak('Playing'+ song)
    pywhatkit.playonyt(song)

def time():
    current_time = datetime.datetime.now().strftime('%H:%M')
    speak("Current time is " + current_time)

def date():
    current_date = datetime.datetime.now().strftime('%d/%m/%Y')
    speak("Today's date is " +current_date)

def wiki(command):
    command = command.replace('tell me about', '')
    information = wikipedia.summary(command, 1) 
    print(information)
    speak(information)

def joke():
    joke = pyjokes.get_joke()
    speak(joke)

def open_application(command):
    application_name = command.replace('open', '')
    if 'chrome' in application_name:
        os.system('start chrome')
    elif 'code' in application_name:
        os.system('start code')
    else:
        speak("Sorry, I don't know how to open that application.")

def calculator(command):
    try:
        expression = command.replace('calculate', '')
        result = eval(expression)
        speak("The result is " + str(result))
    except Exception as e:
        speak("Sorry, I couldn't perform the calculation.")

def run_Assistant():
    wishMe()
    while True:
        command = takeCommand()

        if 'play' in command:
            play_song(command)
        
        elif 'time' in command:
            time()
        
        elif 'date' in command:
            date()
        
        elif 'tell me about' in command:
            wiki(command)

        elif 'joke' in command:
            joke()

        elif 'open' in command:
            open_application(command)

        elif 'calculate' in command:
            calculator(command)

        elif 'exit' in command:
            break

        else:
            speak("Say that command again")

if __name__ == "__main__":
    run_Assistant()

