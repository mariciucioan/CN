# Descompunere matricei A in L si U folosind Algoritmul lui Crout

import numpy as np
import copy

#Varianta 1: Folosim 2 matrici auxiliare L si U si le calculam pe baza lui A 
def lu_decomposition_aux(A):
    n = len(A)
    #initializam matricile cu 0
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for p in range(n):
        # Calcul elemente coloanei p din L
        for i in range(p, n):
            L[i][p] = A[i][p]
            for k in range(p):
                L[i][p] -= L[i][k] * U[k][p]
                if p == i and int(L[i][p]) == 0:
                    print(f'A fost gasit L[{i}][{p}] egal cu 0, A nu poate fi descompus in LU')
                    return
                    

        
        # Calcul elemente liniei p din U
        for i in range(p+1, n):
            U[p][i] = A[p][i]
            for k in range(p):
                U[p][i] -= L[p][k] * U[k][i]
            U[p][i] /= L[p][p]

    # Diagonala matricei U se completeaza cu 1
    for i in range(n):
        U[i][i] = 1

    #Float types
    return L, U


#Varianta 2: Calculam L si U direct in A unde U va fi reprezentat de elementele aflate deasupra
#diagonaleiprincipale iar L de diagonala principala + elementele de sub aceasta

import numpy as np

def lu_decomposition_same_matrix(A):
    B = copy.deepcopy(A)
    n = len(B)

    for p in range(n):
        # Calcul elemente coloana p din L si elemente linie p din U
        for i in range(p, n):
            # Calcul elemente coloana p din L
            for k in range(p):
                B[i][p] -= B[i][k] * B[k][p]
                if p == i and int(B[i][p]) == 0:
                    print(f'A fost gasit A[{i}][{p}] egal cu 0, A nu poate fi descompus in LU')
                    return

        #omitem calcularea elementelor de pe diagonala principala, stiind ca sunt 1
        for i in range(p+1, n):
            # Calcul elemente linie p din U
            for k in range(p):
                B[p][i] -= B[p][k] * B[k][i]
            B[p][i] /= B[p][p]

    return B

A = np.array([[2, 0, 2],
              [1, 2, 5],
              [1, 1, 7]])

L, U = lu_decomposition_aux(A)
print("Matricea L:")
print(L)
print("Matricea U:")
print(U)

B = lu_decomposition_same_matrix(A)
print("Matricea LU:")
print(B)