import cv2

# Definição de função que irá redimensionar a imagem/video para que haja um processamento menor;
def redim(img, largura):
    alt = int(img.shape[0]/img.shape[1]*largura)
    img = cv2.resize(img, (largura, alt), interpolation=cv2.INTER_AREA)
    return img

# variavel que receberá o metodo de reconhecimento (face, olho, etc)
df = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("neymar-sentado.jpg")

img = redim(img, 320)
imgPB = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # variavel que receberá o video em Preto e branco

faces = df.detectMultiScale(imgPB, scaleFactor=1.1, minNeighbors=1 , minSize=(2,2))
img_temp = img.copy()
for (x,y,lar,alt) in faces:
    cv2.rectangle(img_temp, (x,y), (x+lar, y+alt), (0,255,255), 1)

cv2.imshow("Detector de faces", redim(img_temp, 640))
cv2.waitKey(0)

