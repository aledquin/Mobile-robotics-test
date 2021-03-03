import numpy as np
import cv2

canvas = np.zeros((200,600,3),dtype="uint8")
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

copia = canvas.copy()

#Rectangulo
blanco =(255,255,255)
cv2.rectangle(canvas,(20,20),(580,180),blanco,-1)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

rojo=(0,0,255)
cv2.line(canvas, (50,50),(550,150),rojo,3)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)


cv2.circle(canvas, (300,100),50,rojo,-1)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

negro = (0,0,0)
texto = "Gryffindor"
fuente= cv2.FONT_ITALIC
tipo  = cv2.FILLED
pos   = (80,100)

cv2.putText(canvas,texto,pos,fuente,3,negro,5)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
