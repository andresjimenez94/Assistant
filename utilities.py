import playsound
import os

def Alert():
    filename = os.path.dirname(__file__) + r"\\Alert.mp3"
    playsound.playsound(filename)