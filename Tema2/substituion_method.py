import numpy as np
from descompunereLU import *

def forward_substitution(A, b):
    n = len(b)
    x = np.zeros(n)
    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    return x

def backward_substitution(A, b):
    n = len(b)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
    return x


#Exemplu de utilizare
# A = np.array([[2.0, -1.0, 1.0],
#               [-3.0, 0.0, 1.0],
#               [-2.0, 1.0, 2.0]])
# b = np.array([1.0, 2.0, 3.0])

# # Aplicăm descompunerea LU
# A = lu_decomposition_same_matrix(A)

# # Calculăm xL folosind substituția directă cu matricea A și b
# x_L = forward_substitution(A, b)

# # Calculăm xU folosind substituția inversă cu matricea A și rezultatul obținut anterior
# x_U = backward_substitution(A, x_L)

# print("Solutia aproximativa xLU a sistemului Ax = b este:", x_U)
