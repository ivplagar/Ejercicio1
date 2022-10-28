#importamos las librerías necesarias
import csv
import time
from HTTP_Requests.api_simpsons import obtenerQuote
from HTTP_Requests.download_images import download_image
from HTTP_Requests.create_directory import create_directory_simpson

def returnCharacter():
  contador = 0 #declaramos el contador de palabras
  while True: #bucle para definir que mientras la respuesta al servidor sear True se ejecute el código
    
    character = obtenerQuote()#obtenemos el personaje y declaramos las variables que usaremos
    name = character['character']
    quote = character['quote']
    image = character['image']
    words = quote.split()
    
    for word in words: #funcion para recorrer palabra a palabra las quotes de los personajes y contarlas

      contador += 1
      my_dict2 = {'Palabra': word, 'Contador': contador} #se guarda en un diccionario la palabra y el número que ocupa en el recuento
      
      with open('count.csv', 'a') as f: #creamos el csv para introducir el diccionario
        w = csv.DictWriter(f, my_dict2.keys())
        w.writerow(my_dict2) #se escribe 1 a 1 cada palabra con su numero correspondiente
   
    my_dict = {'Nombre': name, 'Frase': quote} #diccionario con el que introduciremos el nombre y la frase en los csv de cada personaje
    
    if(name == 'Lisa Simpson'): #condicional para comprobar que el personaje que recibimos es Lisa
      
      with open('app/Lisa/Lisa.csv', 'a') as f: #creamos el csv de las frases de Lisa
        w = csv.DictWriter(f, my_dict.keys())
        w.writerow(my_dict) #se escribe la frase en el csv
        
        download_image(image,'app/Lisa/', name) #descargamos la imagen de Lisa
    
    elif(name == 'Homer Simpson'): #este elif es lo mismo que antes con Lisa, pero con Homer
      
      with open('app/Homer/Homer.csv', 'a') as f:
        w = csv.DictWriter(f, my_dict.keys())
        w.writerow(my_dict)
        
        download_image(image,'app/Homer/', name)
    
    else: #para todos los demás personajes ejecutamos la siguiente función
      
      create_directory_simpson(name, image, my_dict)
    
    time.sleep(30) #comando para ejecutar la función cada 30 segundos