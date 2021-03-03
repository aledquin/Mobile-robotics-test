import cv2
import numpy as np

cam =cv2.VideoCapture(0)
alto = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
ancho = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cam.get(cv2.CAP_PROP_FPS))

_,foto=cam.read()
cv2.imshow("FOTO",foto)
cv2.waitKey(0)

#filtro
#cv2.blur()
#cv2.billateralFilter()
#cv2.median()

borrosa=cv2.GaussianBlur(foto,(19,19),0)
cv2.imshow("borrosa",borrosa)
cv2.waitKey(0)

# HSV
HSV = cv2.cvtColor(borrosa, cv2.COLOR_BGR2HSV)

#Colores lim
azul_min=np.array([103,150,50])
azul_max=np.array([137,255,255])

#Rango/Mask
mascara = cv2.inRange(HSV,azul_min,azul_max)
cv2.imshow("Mask",mascara)
cv2.waitKey(0)

#Contorno
azul=(255,0,0)

(_,conts,_)=cv2.findContours(mascara, cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(mascara,conts,-1,azul,5)
cv2.imshow("mascara",mascara)
cv2.waitKey(0)

#Contorno
azul=(255,0,0)

(_,conts,_)=cv2.findContours(mascara, cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_SIMPLE)
"""
foto_aux=cv2.copy(foto)
cv2.drawContours(foto,conts,-1,azul,5)
cv2.imshow("huiija",foto)
cv2.waitKey(0)
"""

mask = cv2.merge([mascara,mascara,mascara])
cv2.drawContours(mask,conts,-1,azul,5)
cv2.imshow("huija",mask)
cv2.waitKey(0)

#ss
verde =(0,255,0)
for c in conts:
    cv2.drawContours(foto,[c],-1,verde,5)
    M  = cv2.moments(c)
    cX = int(M["m10"]/M["m00"])
    cY = int(M["m01"]/M["m00"])

    cv2.circle(foto,(cX,cY),3, (255,0,0),-1)
    area = cv2.contourArea(c)
    per  = cv2.arcLength(c,True)

    print("area: {}".format(area) )
    print("perimetro: {}".format(per))

    cv2.imshow("Maskt",foto)
    cv2.waitKey(0)








