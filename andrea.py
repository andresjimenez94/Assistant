from os import name
from time import sleep
import assistant
import dataBase
import utilities

def LlamarAndrea(action):
    escuchando=True
    while escuchando:
        if action == "":
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
            print(id)
            Paciente = True
            while Paciente:
                assistant.speak("¿Cual es el nombre del paciente?")
                ##name = assistant.listen()
                name = "Prueba"
                print(name)
                
                try:
                    dataBase.GuardarRevision(id,name)
                    Paciente=False
                except Exception as e:
                    assistant.speak("No entendi el nombre del Paciente")      
                    Paciente=True
                        
            tooths = dataBase.ConsultarTooth()
            
            
            
            for id_tooth,name_tooth in tooths:
                EnRevicion = True
                while EnRevicion:
                    assistant.speak("¿Como se encuentra el Diente" + name_tooth + "?")
                    print("Habla")
                    valor = assistant.listen()
                    valor=valor.lower()
                    print(valor)
                    if valor=="sano" or valor=="disminuido" or valor=="gingivitis" or valor=="periodontitis" or valor=="ausente"  :
                        dataBase.GuardarDetalleRevision(id,id_tooth,valor)
                        EnRevicion = False
                    else:
                        assistant.speak("Lo siento no entendí")
                    

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
            
    