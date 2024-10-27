import subprocess

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


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            recognizer.adjust_for_ambient_noise(source, duration=2)
            command = command.lower()
            if 'intelligence' in command:
                command = command.replace('intelligence', '')
                print(command)

    except:
        pass
    return command


def run_Intelligence():
    command = take_command()
    print(command)
    if 'play' in command:
        command = command.replace('intelligence', '')
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'self' in command:
        print('I am intelligence, built by team intelligence for AI Project')
        talk('I am intelligence, built by team intelligence for AI Project')

    elif 'bad' in command:
        print('Please Ask a good question.')
        talk('Please Ask a good question.')

    elif 'teacher' in command:
        print('Jamshed Alam Patwary, He is Associate Professor in IIUC.')
        talk('Jamshed Alam Patwary, He is Associate Professor in IIUC.')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)

    elif 'application' in command:
        print('Sure! Here it is')
        talk('Sure! Here it is')
        program = "C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])

    elif 'video' in command:
        print('Sure! Here it is')
        talk('Sure! Here it is')
        command = command.replace('intelligence', '')
        command = command.replace('video', '')
        command = command.replace('search', '')
        command = command.replace('of', '')
        web = "https://www.youtube.com/results?search_query=" + command
        webbrowser.open_new_tab(web)

    elif 'search' in command:
        print('Sure! Here it is')
        talk('Sure! Here it is')
        command = command.replace('intelligence', '')
        command = command.replace('search', '')
        program = "https://www.google.com/search?q=" + command
        webbrowser.open_new_tab(program)

    elif 'profile' in command:
        print('Opening...')
        talk('Opening...')
        webbrowser.open_new_tab("https://web.facebook.com/muhammed.patwary")

    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())

    elif 'team member' in command:
        print('Your team member are Main, Raihan, Fardeem, Atiq')
        talk('Your team member are Main, Raihan, Fardeem, Atiq')

    elif 'who is' in command:
        person = command.replace('who is' and 'intelligence', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'about' in command:
        things = command.replace('about' and 'intelligence', '')
        info = wikipedia.summary(things, 1)
        print(info)
        talk(info)

    else:
        print('Please say the command again.')
        talk('Please say the command again.')


#while True:
run_Intelligence()