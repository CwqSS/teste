import numpy as np
import cv2

Azul1 = np.array([100, 67, 0], dtype = "uint8")
Azul2 = np.array([255 , 128, 50], dtype = "uint8")

# (Variavel = cv2.VideoCapture("caminho")) Este metodo lê o vídeo

EstojoVideo = cv2.VideoCapture("Estojo.mp4")

while True:
    (sucesso, frame) = EstojoVideo.read()
    if not sucesso:
        break

    obj = cv2.inRange(frame, Azul1, Azul2) # Este metódo faz o processo de limiarização aprendido na seção 6
    
    cv2.imshow("Objeto", obj)
    cv2.imshow("Janela", frame)
    if cv2.waitKey(1) & 0xFF == ord("s"): # Isto funciona com "&", não com "and"
        break

