import speech_recognition
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = speech_recognition.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.setProperty('rate', 120)

engine.say('Hello, How can I help you?')
engine.runAndWait()

def reply_command(command):
    print(command)
    if 'play' in command:
        song = command.replace(command[:command.index('play') + 5], '')
        engine.say('Ok playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        engine.say('Current time is ' + datetime.datetime.now().strftime('%H:%M'))
    elif 'search' in command:
        item = command.replace(command[: command.index('search') + 7], '')
        info = wikipedia.summary(item, 1)
        print(info)
        engine.say('Ok. ' + info)
    elif 'your name' in command:
        engine.say('My name is Alexa. Whats your name?')
    elif 'my name' in command:
        name = command.replace(command[: command.index('is') + 3], '')
        engine.say('Nice to meet you ' + name + '. How can I help you?')
    elif 'you single' in command:
        engine.say('No, currently I am in a relationship with Shahed')
    elif 'bye' in command:
        engine.say('Ok bye. See you soon!')
        # exit()
    else:
        engine.say('I can\'t understand. Can you Please tell me again')

    engine.runAndWait()


def take_command():
    try:
        with speech_recognition.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            reply_command(command)
    except:
        print('Something went wrong.')


while True:
    take_command()

