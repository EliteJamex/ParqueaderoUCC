import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from foto import foto
from leerCarnet import extraer_texto_de_imagen

# Función para tomar una foto (puedes implementar la lógica aquí)
def tomar_foto():
    print(foto());
    extraer_texto_de_imagen("img/2.jpeg")


# Crear una ventana
ventana = tk.Tk()
ventana.title("Interfaz")

# Crear un marco para la imagen
imagen_marco = tk.Frame(ventana)
imagen_marco.pack(side=tk.LEFT, padx=20, pady=20)

# Cargar la imagen usando PIL
imagen_pil = Image.open('imagen.png')
nuevo_tamano = (200, 200)
imagen_redimensionada = imagen_pil.resize(nuevo_tamano)
imagen_tk = ImageTk.PhotoImage(imagen_pil)

# Crear una etiqueta para la imagen
imagen_label = tk.Label(imagen_marco, image=imagen_tk)
imagen_label.pack()

# Crear un botón "Tomar foto" centrado debajo de la imagen
boton_tomar_foto = tk.Button(ventana, text="Tomar foto", command=tomar_foto)
boton_tomar_foto.pack(side=tk.TOP, padx=10, pady=10)

# Crear un marco para el texto
texto_marco = tk.Frame(ventana)
texto_marco.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Agregar texto estático como etiquetas
nombres_label = tk.Label(texto_marco, text="Nombres: Juanito")
nombres_label.pack(fill=tk.BOTH, expand=True)

apellidos_label = tk.Label(texto_marco, text="Apellidos: Pepito")
apellidos_label.pack(fill=tk.BOTH, expand=True)

carrera_label = tk.Label(texto_marco, text="Carrera: Ingeniería en Sistemas")
carrera_label.pack(fill=tk.BOTH, expand=True)

# Ejecutar el bucle principal
ventana.mainloop()