import csv
import time

from HTTP_Requests.api_simpsons import obtenerQuote
from HTTP_Requests.download_images import download_image
from HTTP_Requests.count_words import word_count
def returnCharacter():
  contador = 0
  while True:
    contador += 1
    character = obtenerQuote()
    name = character['character']
    quote = character['quote']
    image = character['image']
    my_dict = {'Nombre': name, 'Frase': quote}
    count_words = word_count(quote, contador)
    print(count_words)
    with open('Count.csv', 'a') as f:
         [f.write('{0},{1}\n'.format(key, value)) for key, value in count_words.items()]
        #w = csv.DictWriter(f, count_words)
        #w.writerow(count_words)
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
    time.sleep(1)