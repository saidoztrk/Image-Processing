# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:00:22 2024

@author: muozi
"""


import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)


img1=cv2.imread('bee.jpg',0)
cv2.imshow('bee1',img1)

a=img.shape # Renkli görüntü boyutu
b=img1.shape # Gri görüntü boyutu


print("Renkli Görüntü Boyutu:"+str(a))
print("Gri Görüntü Boyutu:"+str(img1.shape))

#sonuç renkli için 3, gri için 2 boyutlu bir dizi döner
# Renkli görüntü boyutu: (yükseklik, genişlik, renk kanalları)
# Gri görüntü boyutu: (yükseklik, genişlik)
# Renkli görüntü boyutu: (yükseklik, genişlik, 3)
# Gri görüntü boyutu: (yükseklik, genişlik)


cv2.waitKey(0)
cv2.destroyAllWindows()