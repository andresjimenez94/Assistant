from time import sleep
import assistant
import dataBase
import utilities

def LlamarAndrea():
    escuchando=True
    while escuchando:
        assistant.speak("ammm")
        #utilities.Alert()
        action = assistant.listen()
        action=action.lower()
        print(action)
        if (action == "iniciar"):
            assistant.speak("Iniciando la configuracion del asistente")
            dataBase.iniciarAssistant()
            assistant.speak("Finalizó la configuracion del asistente")
            escuchando = False
        elif (action == "nueva"):
            escuchando = False
            pass
        elif (action == "consultar"):
            escuchando = False
            assistant.speak("Que revision deseas consultar?")
            revisonid = assistant.listen()
            valor = dataBase.GetRevision(revisonid)
            if (valor >= 320 and valor <= 520):
                assistant.speak("Nivel de afección es Sano")
            
        else:
            assistant.speak("No entendí, puedes repetirme por favor")
            
    