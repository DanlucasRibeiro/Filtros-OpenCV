import cv2 
import numpy as np  

filtro = 5

imagem = cv2.imread("Imagens/mario.jpeg")

filterRed = cv2.blur(imagem,(filtro,filtro))
filterRed2 = cv2.blur(imagem,(filtro + 2,filtro + 2))

cv2.imshow('Original',imagem)
cv2.imshow('Filtro da Media', filterRed)
cv2.imshow('Filtro da Pos', filterRed2)
cv2.waitKey(0)
cv2.destroyAllWindows()