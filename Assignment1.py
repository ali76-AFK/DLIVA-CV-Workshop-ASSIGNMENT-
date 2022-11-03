# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ts2j2-3v7Y3Sqx0f_a8Z1hODsHrMLKe-
"""

import cv2
# from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#mount google drive to colab environment
me1 = cv2.imread("me3.jpeg")
me2 = cv2.imread("me2.jpeg")
me3 = cv2.imread("me1.jpeg")

kernel = np.ones((3,3), np.float32)/20
grayImage1 = cv2.cvtColor(me1,cv2.COLOR_RGB2GRAY)
convolvedImg = cv2.filter2D(grayImage1, -1,kernel)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage1, 120, 255, cv2.THRESH_BINARY)
#image1
imgBlur1 = cv2.GaussianBlur(blackAndWhiteImage,(7,7),100)
grayImage2 = cv2.cvtColor(me2,cv2.COLOR_RGB2GRAY)
convolvedImg = cv2.filter2D(grayImage2, -1,kernel)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage2, 120, 255, cv2.THRESH_BINARY)
#image2
imgBlur2 = cv2.GaussianBlur(blackAndWhiteImage,(7,7),5)
grayImage3 = cv2.cvtColor(me3,cv2.COLOR_RGB2GRAY)
convolvedImg = cv2.filter2D(grayImage3, -1,kernel)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage3, 120, 255, cv2.THRESH_BINARY)
#image3
imgBlur3 = cv2.GaussianBlur(blackAndWhiteImage,(7,7),5)
kernel = np.ones((3,3), np.float32)/20 # box filter

# canny
imgCanny1 = cv2.Canny(imgBlur1,100,100)
imgCanny2 = cv2.Canny(imgBlur2,100,100)
imgCanny3 = cv2.Canny(imgBlur3,100,100)
# sobel
sobelx = cv2.Sobel(imgBlur1, cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(imgBlur1, cv2.CV_8U,0,1,ksize=3)
imgSobel1 = sobelx + sobely
sobelx = cv2.Sobel(imgBlur2, cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(imgBlur2, cv2.CV_8U,0,1,ksize=3)
imgSobel2 = sobelx + sobely
sobelx = cv2.Sobel(imgBlur3, cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(imgBlur3, cv2.CV_8U,0,1,ksize=3)
imgSobel3 = sobelx + sobely


plt.imshow(imgCanny1)

plt.imshow(imgCanny2)

plt.imshow(imgCanny3)

plt.imshow(imgSobel1)

plt.imshow(imgSobel2)

plt.imshow(imgSobel3)

imgBlur1 = cv2.GaussianBlur(grayImage1,(9,9),50)
# median = cv2.medianBlur(img,5)
# blur = cv2.bilateralFilter(img,9,75,75)

# Displaying the converted image
# pil_img = Image.fromarray(imgBlur)
# pil_img.show()


plt.imshow(imgBlur1)

imgBlur2 = cv2.GaussianBlur(grayImage2,(9,9),50)
# median = cv2.medianBlur(img,5)
# blur = cv2.bilateralFilter(img,9,75,75)

# Displaying the converted image
# pil_img = Image.fromarray(imgBlur)
# pil_img.show()


plt.imshow(imgBlur2)

imgBlur3 = cv2.GaussianBlur(grayImage3,(9,9),50)
# median = cv2.medianBlur(img,5)


# Displaying the converted image
# pil_img = Image.fromarray(imgBlur)
# pil_img.show()


plt.imshow(imgBlur3)

from google.colab import drive
drive.mount('/content/drive')

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('coins.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray');

blur = cv2.GaussianBlur(gray, (11,11), 0)
plt.imshow(blur, cmap='gray')

canny = cv2.Canny(blur, 30, 150, 3)
plt.imshow(canny, cmap='gray')

dilated = cv2.dilate(canny, (1,1), iterations = 2)
plt.imshow(dilated, cmap='gray')

(cnt, heirarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0,255,0), 2)

plt.imshow(rgb)


print('the number of coins is: ', len(cnt))
plt.show()