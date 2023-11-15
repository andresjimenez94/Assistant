import speech_recognition as sr
from gtts import gTTS
import playsound
import os

def speak(message):
    tts = gTTS(text=message,lang="es",slow=False)
    filename = os.path.dirname(__file__) + r"\\voice.mp3"
    #print(filename)
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""
        
        try:
            #reconize_bing()
            #recognize_google_cloud()
            #recognize_ibm()
            
            said = r.recognize_google(audio,key="YOUR_GOOGLE_SPEECH_RECOGNITION_API_KEY",language="es-ES")
            #print(said)
        except Exception as e:
            print("Exception: " + str(e))
    
    return said