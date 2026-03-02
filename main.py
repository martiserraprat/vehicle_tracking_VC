import FuncionsPP
import numpy as np
import utils

def main():
    mat = FuncionsPP.generarMatrius()
    train_mat = mat[0:150]
    test_mat = mat[150:300]
    mitjana, desviacio = FuncionsPP.calcularModelFons(train_mat)
    utils.print_img(desviacio)
    utils.print_img(mitjana)

if __name__ == "__main__":
    main()