import FuncionsPP
import numpy as np
import utils

def main():
    ## tasca 3
    llindar = 62 # Simplament a partir de quan es considera cotxe despres de fer la resta

    ## tasca 4
    alpha = 1.1 # Si alpha és petit el detector és molt sensible i si es mes gran es mes exigent
    beta = 17 # tarctar el soroll de la càmera quan mes gran mes soroll elimina pero es pot emportar cotxes per davant
    
    mat = FuncionsPP.generarMatrius()
    train_mat = mat[0:150]
    test_mat = mat[150:300]
    mitjana, desviacio = FuncionsPP.calcularModelFons(train_mat)

    opcio = 4 ## 3 o 4, quina Tasca/Mètode volem utilitzar per defecte 4

    res = FuncionsPP.generar_tots_resultats(opcio, test_mat, llindar, alpha, beta, mitjana, desviacio) # (opcio, test_mat, llindar, alpha, beta, mitjana, desviacio)
    utils.gravar_video(res)


if __name__ == "__main__":
    main()