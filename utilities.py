import playsound
import os

def Alert():
    filename = os.path.dirname(__file__) + r"\\Alert.mp3"
    playsound.playsound(filename)
    
def nivelAfeccion(Valor):
    result="fuera de rango"
    
    if (Valor >= 320 and Valor <= 520):
        result = "sano"
    elif (Valor >= 521 and Valor <= 999):
        result = "enfermo"
    elif (Valor >= 1000 and Valor <= 1280):
        result = "grave"
        
    return result