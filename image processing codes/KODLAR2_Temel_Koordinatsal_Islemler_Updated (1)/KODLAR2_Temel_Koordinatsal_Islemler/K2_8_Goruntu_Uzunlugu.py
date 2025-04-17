# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:13:54 2024

@author: muozi
"""


import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)


img1=cv2.imread('bee.jpg',0)
cv2.imshow('bee1',img1)

print("Renkli Satır+Sütun+Kanal Sayısı veya Uzunlugu:"+str(len(img.shape)))
# sonuç 3 çünkü renkli görüntü 3 boyutludur (yükseklik, genişlik, renk kanalları)
print("Gri Satır+Sütun+Kanal Sayisi veya Uzunlugu:"+str(len(img1.shape)))
# sonuç 2 çünkü gri görüntü 2 boyutludur (yükseklik, genişlik)


cv2.waitKey(0)
cv2.destroyAllWindows()