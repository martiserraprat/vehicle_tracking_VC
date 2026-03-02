import matplotlib.pyplot as plt
import cv2

def print_img(img_mat):
    plt.figure(figsize=(10, 6))
    plt.imshow(img_mat, cmap='gray')
    plt.title("Imatge")
    plt.colorbar()
    plt.show()

def gravar_video(results_seq):
    alto, ancho = results_seq[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('cotxes_detectats.avi', fourcc, 20.0, (ancho, alto), isColor=False)
    for frame in results_seq:
        out.write(frame)
    out.release()