import cv2


def play():
    video = cv2.VideoCapture('video2_480.mp4')
    retorno, imagem = video.read()

    while retorno:
        coisas(imagem)
        cv2.imshow("cv", imagem)
        _ = cv2.waitKey(5)
        retorno, imagem = video.read()

def coisas(imagem):
    pass
