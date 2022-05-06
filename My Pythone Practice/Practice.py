from distutils import command
import speech_recognition
from distutils import command

listener = speech_recognition.Recognizer()

try:
    with speech_recognition.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        c = listener.recognize_google(voice)
        print(c)
except:
    print("Something went wrong.")