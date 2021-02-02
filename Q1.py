import cv2
img = cv2.imread("lotus.jpg")
red = img[:, :, 2].copy()


