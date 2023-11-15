from time import sleep
import assistant
import dataBase
import utilities

def LlamarAndrea():
    escuchando=True
    while escuchando:
        assistant.speak("Dime")
        ##utilities.Alert()
        sleep(1)
        Action = assistant.listen()
        print(Action)
        if (Action == "iniciar"):
            assistant.speak("Iniciando la configuracion del asistente")
            dataBase.iniciarAssistant()
            assistant.speak("Finalizó la configuracion del asistente")
            escuchando = False
        if (Action == "nueva revision"):
            pass
        else:
            assistant.speak("No entendí, puedes repetirme por favor")
            
    