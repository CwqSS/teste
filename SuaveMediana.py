import cv2

imagem = cv2.imread("imagem0.jpg")

for i in range(0, imagem.shape[0], 15):
    for j in range(0, imagem.shape[1], 15):
        imagem[i:i+3, j:j+3] = (255, 255, 255)

suave = cv2.medianBlur(imagem, 11)

cv2.imshow("IMG", imagem)
cv2.imshow("JANELA", suave)
cv2.waitKey(0)
