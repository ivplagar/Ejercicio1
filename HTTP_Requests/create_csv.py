import csv
import time
from HTTP_Requests.api_simpsons import obtenerQuote
def returnCharacter():
  while True:
    character = obtenerQuote()['character']
    quote = obtenerQuote()['quote']
    my_dict = {'Nombre': character, 'Frase': quote}
    if(character == 'Lisa Simpson'):
      with open('Lisa/Lisa.csv', 'a') as f:
        w = csv.DictWriter(f, my_dict.keys())
        w.writerow(my_dict)
    elif(character == 'Homer Simpson'):
      with open('Homer/Homer.csv', 'a') as f:
        w = csv.DictWriter(f, my_dict.keys())
        w.writerow(my_dict)
    else:
      with open('General/General.csv', 'a') as f:
        w = csv.DictWriter(f, my_dict.keys())
        w.writerow(my_dict)
    time.sleep(1)