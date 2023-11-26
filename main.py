import assistant
import andrea
import speech_recognition as sr

def main():
    print("Inicia Andrea")
    while True:
        try:
            print("Habla")
            audio = assistant.listen()
            audio=audio.lower()
            print(audio)
            x = audio.split(" ")
            a = len(x)
            if a==1:
                if (audio == "andrea"):
                    andrea.LlamarAndrea("")
            else:
                if (x[0] == "andrea"):
                    andrea.LlamarAndrea(x[1])
                
        except Exception as e:
            print("Sin Escuchar")

if __name__=="__main__":
    main()
    