import matplotlib.pyplot as plt

def print_img(img_mat):
    plt.figure(figsize=(10, 6))
    plt.imshow(img_mat, cmap='gray')
    plt.title("Imatge")
    plt.colorbar()
    plt.show()