import cv2 
import numpy as np  

filtro = 5

imagem = cv2.imread("Imagens/mario.jpeg")

filterMedia = cv2.blur(imagem,(filtro,filtro))
filterMediana = cv2.medianBlur(imagem,(filtro))
filterGaussian = cv2.GaussianBlur(imagem,(filtro,filtro),0)
cv2.imshow('Original',imagem)
cv2.imshow('Filtro da Media', filterMedia)
cv2.imshow('Filtro da Mediana', filterMediana)
cv2.imshow('Filtro Gaussiano', filterGaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()