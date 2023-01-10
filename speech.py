import pyttsx3
import speech_recognition

engine = pyttsx3.init()

engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


recognizer = speech_recognition.Recognizer()


while True:
    try:
        with speech_recognition.Microphone() as mic:
             recognizer.adjust_for_ambient_noise(mic, duration=0.2) 
             audio = recognizer.listen(mic)
             text = recognizer.recognize_google(audio)
             text =  text.lower()

             print(f"Recognized {text}") 
             engine.say(text)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue


