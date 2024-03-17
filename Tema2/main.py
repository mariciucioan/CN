from descompunereLU import *
from substituion_method import *
import numpy as np
import scipy
def det_LU(A):
    #aici ne asumam faptul ca det U = 1 diagoanala principala a lui U fiind populata doar cu valori de 1
    #in concluzie detA = detL
    return np.prod(np.diag(A))

def calculate_norm(A, b, x):
    # Calculăm produsul matricei A cu soluția aproximativă
    Ax = np.dot(A, x)

    # Calculăm diferența dintre produsul matricei și vectorul termenilor liberi
    diff = Ax - b

    # Calculăm norma euclidiană a diferenței
    norm_diff = np.linalg.norm(diff, ord=2)

    return norm_diff

def generate_matrix(n):
    while True:
        matrix = np.random.randint(0, 100, size=(n, n))
        #activam daca dorim o zeciamala pt a diversifica testele
        # matrix = matrix / 10.0
        # matrix = np.random.rand(n, n)
        det = np.linalg.det(matrix)
        if det != 0:
            return matrix

Ainit = generate_matrix(100)
b = np.random.rand(100)

#matrice de test: 
# Ainit = np.array([[2, 0, 2],
#               [1, 2, 5],
#               [1, 1, 7]])


print("Matricea initiala:")
print(Ainit)
#prima cerinta
B = lu_decomposition_same_matrix(Ainit)
print("Matricea LU:")
print(B)
#cerinta 2
print(f'Determinantul matricei A calculat folosind descompunerea LU: {det_LU(B)}')
#cerinta 3
print(f"Rezolvarea ecuatiei Ax=b, unde b = {b} ")
x_L = forward_substitution(B, b)
print(f'xL: {x_L}')
x_U = backward_substitution(B, x_L)

print("Solutia aproximativa xLU a sistemului Ax = b este:", x_U)
#cerinta 4
norm = calculate_norm(Ainit, b, x_U)
print("Norma euclidiană a diferenței: ", norm)
#cerinta 5
#calculam solutia sistemului, inversa si normele folosind numpy
# Aplicăm descompunerea LU
P, L, U = scipy.linalg.lu(Ainit)

# Calculăm soluția sistemului Ax = b
x_LU = scipy.linalg.solve(Ainit, b)

# Calculăm inversa matricei A
A_inv = np.linalg.inv(Ainit)

# Calculăm soluția sistemului Ax = b folosind inversa matricei A
x_A_inv = np.dot(A_inv, b)

# Calculăm normele
norm_xLU_xlib = np.linalg.norm(x_LU - x_A_inv, ord=2)
norm_xLU_A_inv_b_init = np.linalg.norm(x_LU - np.dot(A_inv, b), ord=2)

# Afișăm soluțiile și normele
print("Solutii folosind biblioteci externe:")
print("Solutia sistemului Ax = b (calculata cu descompunerea LU):", x_LU)
print("Inversa matricei A:", A_inv)
print("Norma ||xLU - xlib||2:", norm_xLU_xlib)
print("Norma ||xLU - A_inv * b_init||2:", norm_xLU_A_inv_b_init)