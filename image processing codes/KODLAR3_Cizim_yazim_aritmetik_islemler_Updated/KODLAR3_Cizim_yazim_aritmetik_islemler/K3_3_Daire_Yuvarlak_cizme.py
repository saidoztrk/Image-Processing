# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:33:43 2024

@author: muozi
"""

import cv2




img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)

cv2.circle(img,(200,100),75,(148,0,4),3)
cv2.circle(img,(200,100),150,(0,255,0),3)
# #parametreler: resim, merkez noktası, yarıçap, rgb renk kodu, kalınlıl
cv2.imshow('daire',img)


cv2.waitKey(0)
cv2.destroyAllWindows()