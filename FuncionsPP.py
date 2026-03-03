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

def calcularModelFons(train_mat):
    mitjana = np.mean(train_mat, axis=0)
    desviacio = np.std(train_mat, axis=0)
    return mitjana, desviacio

def tasca_3(llindar, mitjana, img):
    resta = np.abs(img - mitjana)
    deteccio_binaria = (resta > llindar) * 255
    return deteccio_binaria

def tasca_4(alpha, beta, mitjana, desviacio, img):
    diff = np.abs(img - mitjana)
    llindar_adaptatiu = alpha * desviacio + beta
    mascara = (diff > llindar_adaptatiu) * 255
    return mascara

def generar_tots_resultats(opcio, test_mat, llindar, alpha, beta, mitjana, desviacio):
    results_seq = []
    for i in range(len(test_mat)):

        if(opcio == 3):
            mask = tasca_3(llindar, mitjana, test_mat[i])
        else:
            mask = tasca_4(alpha, beta, mitjana, desviacio, test_mat[i])
        results_seq.append(mask)
    results_seq = np.array(results_seq)
    return results_seq

#Funcion per carregar les imatges de test i les groundtruths
def carregar_groundtruth_test():
    
    gt_files = (glob.glob("groundtruth/*.png"))
    
    gt_test_files = []
    
    for f in gt_files:
        num = int(f.split("gt")[1].split(".")[0])
        if 1201 <= num <= 1350:
            gt_test_files.append(f)
    
    gt_test_files = sorted(gt_test_files)
    
    primera = io.imread(gt_test_files[0], as_gray=True)
    h, w = primera.shape
    
    gt_mat = np.zeros((len(gt_test_files), h, w), dtype=np.uint8)
    
    for i in range(len(gt_test_files)):
        gt_mat[i] = io.imread(gt_test_files[i], as_gray=True)
        
    return gt_mat

def calcular_accuracy(pred_seq, gt_seq):
    
    accuracies = []
    
    for i in range(len(pred_seq)):
        
        pred_bin = (pred_seq[i] == 255)
        gt_bin = (gt_seq[i] == 255)
        
        accuracy = np.mean(pred_bin == gt_bin)
        accuracies.append(accuracy)
        
    accuracy_mitjana = np.mean(accuracies)
    
    return accuracy_mitjana, accuracies
