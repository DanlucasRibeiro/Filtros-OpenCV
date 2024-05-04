import cv2
import numpy as np

filtro = 3

imagem = cv2.imread('Imagens/mario.jpeg')
filterGaussian1 = cv2.GaussianBlur(imagem,(filtro,filtro),0)
filterGaussian2 = cv2.GaussianBlur(imagem,(filtro,filtro),5)

cv2.imshow('Imagem Original', imagem)
cv2.imshow('Filtro Gauciano (0)', filterGaussian1)
cv2.imshow('Filtro Gauciano (5)', filterGaussian2)


cv2.waitKey(0)
cv2.destroyAllWindows()
