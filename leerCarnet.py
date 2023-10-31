from PIL import Image
from pytesseract import *

# Configura la ruta de Tesseract
pytesseract.tesseract_cmd = r'C:\Users\DeimosLsK\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def extraer_texto_de_imagen(ruta_de_la_imagen):
    try:
        # Abre la imagen
        img = Image.open(ruta_de_la_imagen)

        # Extrae el texto de la imagen
        resultado = pytesseract.image_to_string(img)

        return resultado
    except Exception as e:
        return str(e)