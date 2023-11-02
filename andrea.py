import assistant
import dataBase
import utilities

def LlamarAndrea():
    escuchando=True
    while escuchando:
        assistant.speak("Dime")
        utilities.Alert()
        Action = assistant.listen()
        if (Action == "iniciar asistente"):
            assistant.speak("Iniciando la configuracion del asistente")
            dataBase.iniciarAssistant()
            assistant.speak("Finalizó la configuracion del asistente")
            escuchando = False
        if (Action == "nueva revision"):
            pass
        else:
            assistant.speak("No entendí, puedes repetirme por favor")
            
    