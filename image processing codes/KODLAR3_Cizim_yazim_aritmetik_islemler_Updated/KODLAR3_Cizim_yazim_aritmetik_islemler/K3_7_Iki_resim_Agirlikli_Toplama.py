# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:45:47 2024

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






atoplam=cv2.addWeighted(img1,0.7,img2,0.5,0)
# #parametreler: resim1, resim1 ağırlığı, resim2, resim2 ağırlığı, eklenen sabit sayı
# #resim1 ve resim2 aynı boyutta olmalı
# #resim1 ve resim2 aynı renk kanallarına sahip olmalı

cv2.imshow('atoplam',atoplam)




cv2.waitKey(0)
cv2.destroyAllWindows()