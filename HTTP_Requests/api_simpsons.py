import requests
import threading

def obtenerQuote():   
# URL -> api-endpoint  
  URL: str = 'https://thesimpsonsquoteapi.glitch.me/quotes'  
  respuesta = requests.get(url = URL)
  quote = respuesta.json()
  frase_simpsons: str = quote[0]
  return(frase_simpsons)