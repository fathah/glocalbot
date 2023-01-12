import random
import pyttsx3
import speech_recognition
from result_fetch import get_result,read_json
from scan import getStudentInfo, scanQr
from utils import getCampusName, getProgramName, getStudentName

speaker = pyttsx3.init()
speaker.setProperty('rate', 110)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)

recognizer = speech_recognition.Recognizer()

#get_result()


def respond(response):
    speaker.say(f'{response}')
    speaker.runAndWait()



def tell_result(text):
    response = text.replace('result','').replace('of','').replace('what','').replace('the','')
    
    programs = read_json("programs.json")
    for program in programs['data']:
        if  program['name'].lower().replace(' ','') == response.lower().replace(' ',''):
            if program['resultDeclared'] == "1":
                prList = read_json("prList.json")
                result = []
                for pr in prList['data']:
                    if pr['programid'] == program['id'] and pr['rank'] != "0":
                        result.append(pr)
                resultSorted = sorted(result, key=lambda d: d['rank']) 

                response = f"Result of {program['name']} is declared. {getStudentName(resultSorted[0]['studentid'])} is selected  with rank {resultSorted[0]['rank']}"
                for i in range(1,len(resultSorted)):
                    
                    response += f". and {getStudentName(resultSorted[i]['studentid'])} is selected with rank {resultSorted[i]['rank']}\n"

                response += "Congratulations for the winners."
                break
                
            else:
                response = f"Result of {program['name']} is not declared yet."
                break
        else:
            pass

    speaker.say(f'{response}')
    speaker.runAndWait()


mappings = {
    "greetings":respond,
    "name":respond,
    "introduce":respond,
    "markaz_garden":respond,
    "thanks":respond,
    "whatsup":respond,
    "haha":respond,
    "programmer":respond,
    }



def talkFromIntents(text):
    intents = read_json("intents.json")['intents']
    for intent in intents:
        if intent['tag'] in mappings.keys() and text.lower() in intent['patterns']:
            randomIndex = random.randint(0,len(intent['responses'])-1)
            mappings[intent['tag']](intent['responses'][randomIndex].lower())
        # else:
        #     duckres = duck_search(text)
        #     speaker.say(duckres)
        #     speaker.runAndWait()

speaker.say('Hello, I am  Glocal Bot. How can I assist you?')
speaker.runAndWait()

while True:
    try:
        with speech_recognition.Microphone() as mic:
             recognizer.adjust_for_ambient_noise(mic, duration=0.2) 
             audio = recognizer.listen(mic,phrase_time_limit=5)
             text = recognizer.recognize_google(audio)
             text =  text.lower()

             if "result" in text or "results" in text:
                tell_result(text)
             elif "scan" in text or "identify" in text:
                speaker.say("Please show your Jamia ID")
                speaker.runAndWait()
                jmId = scanQr()
                if "JM" in jmId:
                    student  = getStudentInfo(jmId)
                    speaker.say(f"Hello {student['name']} from {getCampusName(student['campus'])}")

             else:
                talkFromIntents(text)
             
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        # speaker.say('Sorry, I did not get that.')
        # speaker.runAndWait()
        continue


