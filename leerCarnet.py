from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = r'C:\Users\DeimosLsK\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

img = Image.open("img/2.jpeg")

resultado = pytesseract.image_to_string(img)

print(resultado);


