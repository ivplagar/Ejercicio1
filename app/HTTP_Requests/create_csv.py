import csv
import time
import os
from HTTP_Requests.api_simpsons import obtenerQuote
from HTTP_Requests.download_images import download_image
from HTTP_Requests.create_directory import create_directory_simpson

def returnCharacter():
  contador = 0
  while True:
    character = obtenerQuote()
    name = character['character']
    quote = character['quote']
    image = character['image']
    words = quote.split()
    for word in words: #intentar posar en una funció
      contador += 1
      my_dict2 = {'Palabra': word, 'Contador': contador}
      with open('Count.csv', 'a') as f:
        w = csv.DictWriter(f, my_dict2.keys())
        w.writerow(my_dict2)
    my_dict = {'Nombre': name, 'Frase': quote}
    if(name == 'Lisa Simpson'):
      with open('Lisa/Lisa.csv', 'a') as f:
        w = csv.DictWriter(f, my_dict.keys())
        w.writerow(my_dict)
        download_image(image,'Lisa/', name)
    elif(name == 'Homer Simpson'):
      with open('Homer/Homer.csv', 'a') as f:
        w = csv.DictWriter(f, my_dict.keys())
        w.writerow(my_dict)
        download_image(image,'Homer/', name)
    else:
      create_directory_simpson(name, image, my_dict)
    time.sleep(30)