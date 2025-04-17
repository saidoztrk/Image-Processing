# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:54:19 2024

@author: muozi
"""

import cv2

img=cv2.imread('ari.jpg') # Resmi okuma
cv2.imshow('bee',img)

cv2.waitKey(0) # 0 sonsuz bekler, 1000 ise 1 sn bekler
cv2.destroyAllWindows()     
