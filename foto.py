import cv2

def foto():
    # Inicializar la cámara
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return "Error"

    # Capturar una imagen
    ret, frame = cap.read()

    if ret:
        # Guardar la imagen en el archivo especificado
        cv2.imwrite("imagen_muestra", frame)
        return "imagen_muestra"
    else:
        print("Error al capturar la imagen")

    # Liberar la cámara
    cap.release()