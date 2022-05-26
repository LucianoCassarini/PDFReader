
#!================================================================
# !                         PDF Reader
#!================================================================

import os
import pdfplumber
import generalFunctions

# devuelve directorio del programa
saved_path = os.getcwd()



# Crea lista de nombres del directorio
file_list = generalFunctions.nameList(saved_path)

if len(file_list) == 0:
    print("No hay ningún archivo cargado...")
else:
    #? permite elegir uno de los archivos de la lista
    print("seleccione el PDF que desea leer")
    count = 0
    for file in file_list:
        print("[" + str(count) + "] " + file)
        count += 1
    
    indiceDeArchivo = input("Seleccione el numero de correspondiente: ")
    indiceDeArchivo = int(indiceDeArchivo)
    
    #? guarda el nombre del archivo seleccionado
    name = file_list[indiceDeArchivo]
    
    
    direccion = saved_path + "/" + name
    with pdfplumber.open(direccion) as temp:
        print("Leyendo. . .")
        for page in temp.pages:
            text = page.extract_text()
            generalFunctions.talk(text)
            
