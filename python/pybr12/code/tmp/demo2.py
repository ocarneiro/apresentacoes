import cv2

video = cv2.VideoCapture(0)
video.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320)
video.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

_, imagem = video.read()

cv2.imshow("cv", imagem)
cv2.waitKey(2000)
