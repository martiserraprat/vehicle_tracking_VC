import matplotlib.pyplot as plt
import cv2
import numpy as np

def print_img(img_mat):
    plt.figure(figsize=(10, 6))
    plt.imshow(img_mat, cmap='gray')
    plt.title("Imatge")
    plt.colorbar()
    plt.show()

def gravar_video(results_seq):
    alto, ancho = results_seq[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('cotxes_detectats_PYTHON.avi', fourcc, 20.0, (ancho, alto), isColor=True)
    for i in range(len(results_seq)):
        frame_color = cv2.cvtColor(results_seq[i].astype(np.uint8), cv2.COLOR_GRAY2BGR)
        out.write(frame_color)
    out.release()

def print_plot_ACC(acc):
    plt.plot(acc)
    plt.title("Accuracy per frame")
    plt.xlabel("Frame")
    plt.ylabel("Accuracy")
    plt.show()