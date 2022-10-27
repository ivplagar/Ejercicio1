import csv
import time

from HTTP_Requests.api_simpsons import obtenerQuote
from HTTP_Requests.download_images import download_image
def returnCharacter():
  contador = 0
  while True:
    character = obtenerQuote()
    name = character['character']
    quote = character['quote']
    image = character['image']
    my_dict = {'Nombre': name, 'Frase': quote}
    words = quote.split()
    for word in words:
      contador += 1
      my_dict2 = {word : contador}
    #dictionary = my_dict2.fromkeys(words, contador)
      with open('Count.csv', 'a') as f:
         [f.write('{0},{1}\n'.format(key, value)) for key, value in my_dict2.items()]
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
      with open('General/General.csv', 'a') as f:
        w = csv.DictWriter(f, my_dict.keys())
        w.writerow(my_dict)
        download_image(image,'General/', name)
    time.sleep(30)