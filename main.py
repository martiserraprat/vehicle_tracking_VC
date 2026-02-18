import FuncionsPP
import numpy as np

def main():
    mat = FuncionsPP.generarMatrius()
    print(mat[0])
    train = mat[0:150]
    test = mat[150:300]
    print(f"Tamaño de train: {train.shape}")
    print(f"Tamaño de test: {test.shape}") 
    print(f"Tamaño de test: {mat.shape}")

if __name__ == "__main__":
    main()