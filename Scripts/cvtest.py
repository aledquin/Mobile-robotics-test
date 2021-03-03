import numpy as np
import cv2

canvas = np.zeros((200,600,3),dtype="uint8")
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

copia = canvas.copy()

#linea
cv2.line(canvas, (0,0),(600,200),(255,255,255),5)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

#los colores estan en BGR y no en RGB
color =(0,0,255)
cv2.line(canvas, (0,0),(600,200),color,5)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

color =(0,255,0)
cv2.line(canvas, (0,0),(600,200),color,5)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

color =(255,0,0)
cv2.line(canvas, (0,0),(600,200),color,5)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
