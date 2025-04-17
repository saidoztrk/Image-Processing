# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:34:58 2024

@author: muozi
"""

import cv2
import numpy as np


img=np.zeros((640,720,3),np.uint8)
##img=np.zeros((640,720,3),np.uint8) #siyah arka plan uint8 tipinde sayılarla dolu
img.fill(255)
#img.fill fomnksiyonu ile beyaz arka plan oluşturuldu. 255 sayısı beyaz rengi temsil eder.
#img.fill(0) #siyah arka plan oluşturmak için kullanılabilir.

fontscale=1.0
#fontscale=1.0  aralığındaki sayılar font boyutunu belirler. 1.0, 2.0, 3.0 gibi değerler alabilir.
color=(0,0,255)
fontface=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"FONT_HERSHEY_COMPLEX",(25,40),fontface,fontscale,color)
#parametreler: resim, yazı, konum, font tipi, font boyutu, renk kodu

fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText(img, "FONT_HERSHEY_COMPLEX_SMALL", (25, 80), fontface, fontscale, color)

fontface = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img, "FONT_HERSHEY_DUPLEX", (25, 120), fontface, fontscale, color)

fontface = cv2.FONT_HERSHEY_PLAIN
cv2.putText(img, "FONT_HERSHEY_PLAIN", (25, 160), fontface, fontscale, color)

fontface = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(img, "FONT_HERSHEY_SCRIPT_COMPLEX", (25, 200), fontface, fontscale, color)

fontface = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(img, "FONT_HERSHEY_SCRIPT_SIMPLEX", (25, 240), fontface, fontscale, color)

fontface = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "FONT_HERSHEY_SIMPLEX", (25, 280), fontface, fontscale, color)

fontface = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img, "FONT_HERSHEY_TRIPLEX", (25, 320), fontface, fontscale, color)

fontface = cv2.FONT_ITALIC
cv2.putText(img, "FONT_ITALIC", (25, 360), fontface, fontscale, color)

cv2.namedWindow('text ornekler')
cv2.imshow('text ornekler',img)


cv2.waitKey(0)
cv2.destroyAllWindows()