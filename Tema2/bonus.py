def lu_decomposition_same_matrix(A):
    n = len(A)
    L = [0] * (n * (n + 1) // 2)  
    U = [0] * (n * (n + 1) // 2)  

    index = 0  

    for i in range(n):
        for j in range(i, n):
            U[index] = A[i][j] - sum(L[k] * U[(j * (j + 1)) // 2 + k] for k in range(i))

        for j in range(i + 1, n):
            L[index] = (A[j][i] - sum(L[(j * (j + 1)) // 2 + k] * U[k] for k in range(i))) / U[(i * (i + 1)) // 2 + i]
        index += 1

    return L, U

# Testing
A = ([[2, 0, 2],
    [1, 2, 5],
    [1, 1, 7]])

L, U = lu_decomposition_same_matrix(A)
print("Vector L:")
print(L)
print("Vector U:")
print(U)

