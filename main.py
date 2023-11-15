import assistant
import andrea
import speech_recognition as sr

def main():
    print("Inicia Andrea")
    while True:
        try:
            audio = assistant.listen()
            audio=audio.lower()
            print(audio)
            if (audio == "hola"):
                andrea.LlamarAndrea()
        except Exception as e:
            print("Sin Escuchar")

if __name__=="__main__":
    main()
    