import sys

import numpy as np

n = 3
epsilon = sys.float_info.epsilon
A = [[0, 0, 4],
     [1, 2, 3],
     [0, 1, 2]]
s = [3, 2, 1]


def exercitiu1(A, s):
    n = len(s)
    b = np.zeros(n)
    for j in range(n):
        for i in range(n):
            b[i] += s[j] * A[i][j]

    return b


b = exercitiu1(A, s)
print("----------------\nExercitiu 1\n----------------")
print("Valoare b =", b)


def householder(v):
    v = np.asarray(v, dtype=float)
    n = len(v)
    norm_v = np.linalg.norm(v)
    if norm_v == 0:
        return np.eye(n)

    v = v.reshape((n, 1))
    v_normalized = v / norm_v
    P = np.eye(n) - 2 * np.dot(v_normalized, v_normalized.T)

    return P


def qr_decomposition(A):
    A = np.asarray(A, dtype=float)
    R = np.copy(A)
    Q = np.eye(n)

    for i in range(n):
        x = R[i:, i]
        e = np.zeros_like(x)
        e[0] = np.linalg.norm(x)
        v = x - e
        P = householder(v)

        R[i:, i:] = np.dot(P, R[i:, i:])
        Q[:, i:] = np.dot(Q[:, i:], P)

    return Q, R


print("\n----------------\nExercitiu 2\n----------------")

Q, R = qr_decomposition(A)
print("Matricea Q:")
print(Q)
print("\nMatricea R:")
print(R)

print("\nMatricea Q*R:")
print(np.dot(Q, R))
