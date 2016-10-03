import cv2

cam = cv2.VideoCapture(0)

_, im = cam.read()

cv2.imshow("cv", im)
cv2.waitKey(2000)
