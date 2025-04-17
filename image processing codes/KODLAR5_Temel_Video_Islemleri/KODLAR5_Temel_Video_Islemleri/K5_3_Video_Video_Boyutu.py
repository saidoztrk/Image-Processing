# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:41:49 2024

@author: muozi
"""

import cv2

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture('Video_Trafic.mp4')

while True:
    # Kameradan görüntüyü al
    ret, goruntu = kamera.read()
    
    # Görüntü boyutunu al
    yukseklik, genislik = goruntu.shape[:2]
    # Görüntü boyutunu yazdır
    #goruntu.shape[0] = yukseklik
    #goruntu.shape[1] = genislik
    #goruntu.shape[2] = renk kanalları (BGR)
    
    goruntuBoyutu=f'Goruntu Boyutu: {goruntu.shape}'
    cv2.putText(goruntu, goruntuBoyutu, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)
    
    
    # Metni görüntünün üstüne yazdır
    metin = f'Genislik(sutun): {genislik}px, Yukseklik(satir): {yukseklik}px'
    cv2.putText(goruntu, metin, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Görüntüyü göster
    cv2.imshow('WebCam', goruntu)
    
    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
kamera.release()
# Tüm pencereleri kapat
cv2.destroyAllWindows()
