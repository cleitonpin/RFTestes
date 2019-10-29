from google_images_download import google_images_download   #importing the library
import sys

busca = input('Digite o que você quer baixar -> ')
limit = input('Digite a quantidade de imagens -> ')
tipo = input('Digite o tipo de imagem [face, photo, clip-art, line-drawing, animated] -> ')

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":busca,"limit":limit,"print_urls":True,"type":tipo, "delay":1, "output_directory":"train", "prefix":busca}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images