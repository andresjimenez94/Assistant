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
        if (Action == "nueva"):
            escuchando = False
            pass
        if (Action == "consultar"):
            escuchando = False
            assistant.speak("Que revision deseas consultar?")
            revisonid = assistant.listen()
            valor = dataBase.GetRevision(revisonid)
            if (valor >= 320 and valor <= 520):
                assistant.speak("Nivel de afección es Sano")
            
        else:
            assistant.speak("No entendí, puedes repetirme por favor")
            
    