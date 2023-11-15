from os import name
from time import sleep
import assistant
import dataBase
import utilities

def LlamarAndrea():
    escuchando=True
    while escuchando:
        assistant.speak("a")
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
            idRevision = dataBase.GetIdRevisionConsecutivo()
            id= idRevision[0]
            print(idRevision[0])
            assistant.speak("¿Cual es el nombre del paciente?")
            name= "prueba"
            #name = assistant.listen()
            print(name)
            dataBase.GuardarRevision(id,name)
            assistant.speak("Revision Finalizada")
        elif (action == "consultar"):
            escuchando = False
            assistant.speak("Que revision deseas consultar?")
            revisonid = assistant.listen()
            valor = dataBase.GetRevision(revisonid)
            if (valor >= 320 and valor <= 520):
                assistant.speak("Nivel de afección es Sano")
            
        else:
            assistant.speak("No entendí, puedes repetirme por favor")
            
    