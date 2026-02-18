import skimage as ski
import numpy as np
import glob

def generarMatrius():
    archivos = glob.glob("img/*.jpg")
    primera_img = ski.io.imread(archivos[0], as_gray=True)
    alto, ancho = primera_img.shape

    num_fotos = len(archivos)
    matfotos = np.zeros((num_fotos, alto, ancho), dtype=np.uint8)

    for i in range(num_fotos):
            img = ski.io.imread(archivos[i], as_gray=True)
            matfotos[i] = (img * 255).astype(np.uint8)
            
    return matfotos

def Calculmitjana():
        pass