# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:37:09 2024

@author: muozi
"""

import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)



img[:,:,1]=0


cv2.imshow('green_sifira_cek',img)



img[:,:,1]=225
#neden 225? çünkü 0-255 arası değer alır. 0 olursa yeşil kanalı sıfırlanır. 255 olursa yeşil kanalı doygun olur.


cv2.imshow('green_maks__doyuma_cek',img)






cv2.waitKey(0)
cv2.destroyAllWindows()