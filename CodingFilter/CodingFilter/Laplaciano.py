import cv2
import numpy as np


imagem = cv2.imread('Imagens/mario.jpeg', cv2.IMREAD_GRAYSCALE) 


laplaciano = cv2.Laplacian(imagem, cv2.CV_64F)  # cv2.CV_64F para capturar bordas negativas e positivas
 

# Mostrar a imagem original e a imagem com realce de bordas
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Filtro Laplaciano', laplaciano)

# Aguardar uma tecla ser pressionada para fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
