import cv2

video = cv2.VideoCapture('video2_480.mp4')
retorno, imagem = video.read()

while retorno:
    cv2.imshow("cv", imagem)
    _ = cv2.waitKey(10)
    retorno, imagem = video.read()
