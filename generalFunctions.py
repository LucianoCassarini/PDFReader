
#!================================================================
# !                        Mi Librería
#!================================================================


import os
import pyttsx3

#* Crea una lista con los nombres de todos los archivos que hay en la dirección
def nameList(directorio):
    file_list = os.listdir(directorio)
    return file_list

#* Convertidor de texto a voz
def talk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    