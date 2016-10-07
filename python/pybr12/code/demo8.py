import cv2, numpy as np

camera = cv2.VideoCapture(0)
minimo = np.array([145,120,120])
maximo = np.array([180,255,255])

tecla = 0

while tecla != 27:  # 27 = ESC
    _, imagem = camera.read()
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    mascara = cv2.inRange(hsv, minimo, maximo)
    cv2.imshow("imagem", imagem)
    cv2.imshow("mascara",mascara)
    tecla = cv2.waitKey(33)  # 1000/30 = 33
    tecla = tecla & 0xEFFFFF  # tira modificadores
