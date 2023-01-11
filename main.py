import pyttsx3
import speech_recognition
from neuralintents.main import GenericAssistant

speaker = pyttsx3.init()
speaker.setProperty('rate', 110)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)

recognizer = speech_recognition.Recognizer()

def event_results(response):
    speaker.say(f'Here are the results of the event. {response}')
    speaker.runAndWait()

def greet(response):
    print(response)
    speaker.say(f'{response}')
    speaker.runAndWait()

mappings = {
    "greetings":greet,
    "event_results":event_results }

glocalbot = GenericAssistant('intents.json',intent_methods= mappings, model_name="test_model")
glocalbot.load_model()

while True:
    try:
        with speech_recognition.Microphone() as mic:
             recognizer.adjust_for_ambient_noise(mic, duration=0.2) 
             audio = recognizer.listen(mic,phrase_time_limit=5)
             text = recognizer.recognize_google(audio)
             text =  text.lower()

             glocalbot.request(text)
             
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        # speaker.say('Sorry, I did not get that.')
        # speaker.runAndWait()
        continue


