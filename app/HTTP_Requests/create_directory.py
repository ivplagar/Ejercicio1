import csv
import os
from HTTP_Requests.download_images import download_image
def create_directory_simpson(str_name, str_image, dict):
    # Directory
    directory = str_name
    # Parent Directory path
    parent_dir = "Characters/"
    # Path
    path = os.path.join(parent_dir, directory)
    character_exists = os.path.exists(path)
    if character_exists == False:
        os.mkdir(path)
        with open(f'{path}/{str_name}.csv', 'a') as f:
            w = csv.DictWriter(f, dict.keys())
            w.writerow(dict)
            download_image(str_image,f'{path}/', str_name)
    else:
        with open(f'{path}/{str_name}.csv', 'a') as f:
            w = csv.DictWriter(f, dict.keys())
            w.writerow(dict)
            download_image(str_image,f'{path}/', str_name)