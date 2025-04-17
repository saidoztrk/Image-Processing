# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:11:50 2024

@author: muozi
"""

import cv2

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture('Video_Trafic.mp4')

while True:
    # Kameradan görüntüyü al
    ret, goruntu = kamera.read()

    cv2.imshow('WebCam', goruntu)

    goruntu[:,:,2]=255
    
    
    # Görüntüyü göster
    cv2.imshow('WebCam_Kirmizi_Max', goruntu)
    
    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
kamera.release()
# Tüm pencereleri kapat
cv2.destroyAllWindows()
