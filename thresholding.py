import os
import cv2

img_path = r"/Users/ron.quah/Downloads/1.jpeg"

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
gray_img = img.reshape(img.shape[0]*img.shape[1])
for i in range(gray_img.shape[0]):
    if gray_img[i] > gray_img.mean():
        gray_img[i] = 1
    else:
        gray_img[i] = 0
img = gray_img.reshape(img.shape[0], img.shape[1])