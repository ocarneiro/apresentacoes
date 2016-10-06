import cv2

camera = cv2.VideoCapture(0)

k = 0

while k != 27:
    _, imagem = camera.read()
    cv2.imshow("demo2", imagem)
    k = cv2.waitKey(10)
    k = k & 0xEFFFFF  # tira modificadores

