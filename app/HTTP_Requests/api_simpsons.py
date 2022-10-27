#importamos las librerías necesarias
import requests

def obtenerQuote():   
# URL -> api-endpoint  
  URL: str = 'https://thesimpsonsquoteapi.glitch.me/quotes' #se define la URL donde haremos la petición para recibir el archivo con las frases
  respuesta = requests.get(url = URL) #obtenemos la respuesta
  quote = respuesta.json() #la convertimos en json
  frase_simpsons: str = quote[0] #obtenemos lo necesario para poder interactuar con el JSON
  return(frase_simpsons) #devolvemos el JSON