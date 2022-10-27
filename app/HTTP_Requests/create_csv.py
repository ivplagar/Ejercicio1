import csv
import time

from HTTP_Requests.api_simpsons import obtenerQuote
from HTTP_Requests.download_images import download_image
def returnCharacter():
  while True:
    character = obtenerQuote()['character']
    quote = obtenerQuote()['quote']
    my_dict = {'Nombre': character, 'Frase': quote}
    if(character == 'Lisa Simpson'):
      with open('Lisa/Lisa.csv', 'a') as f:
        w = csv.DictWriter(f, my_dict.keys())
        w.writerow(my_dict)
        download_image(obtenerQuote()['image'],'Lisa/images', obtenerQuote()['character'])
    elif(character == 'Homer Simpson'):
      with open('Homer/Homer.csv', 'a') as f:
        w = csv.DictWriter(f, my_dict.keys())
        w.writerow(my_dict)
        download_image(obtenerQuote()['image'],'Homer/images', obtenerQuote()['character'])
    else:
      with open('General/General.csv', 'a') as f:
        w = csv.DictWriter(f, my_dict.keys())
        w.writerow(my_dict)
        download_image(obtenerQuote()['image'],'General/images', obtenerQuote()['character'])
    time.sleep(3)