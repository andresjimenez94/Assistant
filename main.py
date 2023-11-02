import assistant
import andrea
import speech_recognition as sr

def main():
    pass

if __name__=="__main__":
    while True:
        try:
            mic = sr.Microphone()
            with mic as audio_file:
                recog = sr.Recognizer()
                recog.adjust_for_ambient_noise(audio_file)
                audio = recog.listen(audio_file)
                if (recog.recognize_google(audio) == "hola"):
                    andrea.LlamarAndrea()
        except Exception as e:
            print("Sin Escuchar")