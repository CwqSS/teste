import cv2
import numpy
# Suavização pela média
# Pega a média dos valores em uma determinado matriz da imagem e os atribui para aquela matriz
# variavel = cv2.blur(var.img, (x, y)) 
# É importante que a matriz seja definida por número ímpares, pois haverá um ponto central

imagem = cv2.imread("imagem0.jpg")

for i in range(0, imagem.shape[0], 15):
    for j in range(0, imagem.shape[1], 15):
        imagem[i:i+3, j:j+3] = (255, 255, 255)

suave = cv2.blur(imagem, (23,23))

cv2.imshow("IMG", imagem)
cv2.imshow("IMG2", suave)  
cv2.waitKey(0)
