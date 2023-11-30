from os import name
from time import sleep
import assistant
import dataBase
import utilities

def LlamarAndrea(action):
    escuchando=True
    while escuchando:
        
        assistant.speak("Iniciando la configuracion del asistente")
        dataBase.iniciarAssistant()
        assistant.speak("que deseas realizar: nueva, consultar?")
        action = assistant.listen()
        action=action.lower()
        print(action)
        
        if action == "":
            assistant.speak("No entendo, puedes repetirme por favor")
            #utilities.Alert()
            action = assistant.listen()
            action=action.lower()
            print(action)
        
        if (action == "nueva"):
            escuchando = False
            idRevision = dataBase.GetIdRevisionConsecutivo()
            id= idRevision[0]
            print(id)
            Paciente = True
            while Paciente:
                assistant.speak("Cual es el nombre del paciente?")
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
                        assistant.speak("Lo siento no entendo")
                    

            assistant.speak("Revision Finalizada")
            
        elif (action == "consultar"):
            escuchando = False
            print("entrando a consultar")
            
            cant_revision = dataBase.ConsultaRegistros()
            revision_n = cant_revision[0]
            print("aca volvi" +revision_n)
            
            assistant.speak("Actualmente tenemos " +revision_n +"Revisiones registradas"))
            print(revision_n)
            print("consultar2")
            
            consultarRevision = True
            while consultarRevision:
                try:
                    assistant.speak("Que revision deseas consultar?")
                    revisonid = assistant.listen()
                    intrevisonid = int(revisonid)
                    valor = dataBase.GetRevision(intrevisonid)
                    suma = valor[0]
                    intSuma = int(suma)
                    diag=""                    
                    diag = utilities.nivelAfeccion(intSuma)
                    assistant.speak("Nivel de afección es "+ diag)
                        
                    consultarRevision = False
                        
                except Exception as e:
                    assistant.speak("No entendí")
                    print("Error en consutar la revision")
                    consultarRevision = True
            
        else:
            assistant.speak("No entendo, puedes repetirme por favor")
            
    