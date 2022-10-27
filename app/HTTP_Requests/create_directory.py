#importamos las librerías necesarias
import csv
import os
from HTTP_Requests.download_images import download_image

def create_directory_simpson(str_name, str_image, dict): #definimos la función con la que se crearan los directorios de los personajes que no son Lisa ni Homer

    # Directory
    directory = str_name #obtenemos mediante la llamada a la función en create_csv.py el nombre del directorio
    # Parent Directory path
    parent_dir = "Characters/" #definimos que los directorios irán dentro de la carpeta Characters para mejor orden
    # Path
    path = os.path.join(parent_dir, directory) #definimos la ruta del directorio
    character_exists = os.path.exists(path) #introducimos el directorio en una variable comprobar que existe

    if character_exists == False: 
        os.mkdir(path) #creamos el directorio si no existe
        with open(f'{path}/{str_name}.csv', 'a') as f: #creamos el csv para introducir las frases
            w = csv.DictWriter(f, dict.keys())
            w.writerow(dict) #escribimos la frase con el nombre
            download_image(str_image,f'{path}/', str_name) #llamamos a la función que descarga las imágenes y las guardamos en el directorio propio de cada personaje

    else: #si ya existe el directorio, introducimos las frases en los csv ya existentes, realizando las mismas acciones que en el if anterior
        with open(f'{path}/{str_name}.csv', 'a') as f:
            w = csv.DictWriter(f, dict.keys())
            w.writerow(dict)
            download_image(str_image,f'{path}/', str_name