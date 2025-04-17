# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:45:51 2024

@author: muozi
"""

import cv2


img1=cv2.imread('resim.jpg')
img2=cv2.imread('logo.jpg')

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

print(img1.shape)
print(img1.dtype)
print(img2.shape)
print(img2.dtype)



bolme=cv2.divide(img2,img1)
cv2.imshow('bolme',bolme)


cv2.waitKey(0)
cv2.destroyAllWindows()