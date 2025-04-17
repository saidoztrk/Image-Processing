# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:31:14 2024

@author: muozi
"""

import cv2
import numpy as np



img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)



#shape = img.shape
#print(img.shape)    
#önce yükseklik yani y düzlemi , sonra genişlik yani x düzlemi, sonra renk kanalları





cv2.rectangle(img,(310,70),(612,160),(0,0,255),2)
#parametreler: resim,sol üst köşe,sağ alt köşe,rgb renk kodu,kalınlık
#sol üst köşe: (x1,y1) sağ alt köşe: (x2,y2)    
cv2.imshow('dortgen',img)


cv2.waitKey(0)
cv2.destroyAllWindows()