# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:20:57 2024

@author: muozi
"""

import cv2

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture(0)

while True:
    # Kameradan görüntüyü al
    ret, goruntu = kamera.read()
#ret yazma sebebi, görüntü alınamadığında hata vermemesi için
    # Görüntü alındıysa işleme devam et
    # Görüntüyü göster
    cv2.imshow('WebCam', goruntu)
    
    
    
    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
kamera.release()
# Tüm pencereleri kapat
cv2.destroyAllWindows()
