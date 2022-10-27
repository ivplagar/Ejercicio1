import urllib.request

def download_image(url, file_path, file_name): #definición de la función que descarga imágenes de una url
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)