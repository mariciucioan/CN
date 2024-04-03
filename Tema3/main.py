import sys
import numpy as np


def data_init(ex6=False, n=3):
    if ex6:
        A = np.random.rand(n, n)
        s = np.random.rand(n)
        return A, s
    else:
        A = [[0, 0, 4],
             [1, 2, 3],
             [0, 1, 2]]
        s = [3, 2, 1]

    return A, s


n=100
epsilon = sys.float_info.epsilon
A, s = data_init(ex6=True, n=n)


def ex1(A, s, log=True):
    n = len(s)
    b = np.zeros(n)
    for j in range(n):
        for i in range(n):
            b[i] += s[j] * A[i][j]

    if log:
        print("Exercitiu 1:\n")
        print("Valoare b =", b)
        print("\n----------------")
    return b


def ex2(A, log=True):
    Q, R = householder_qr(A)

    if log:
        print("Exercitiu 2:\n")
        print("Q:")
        print(Q)
        print("R:")
        print(R)
        print("Q * R:")
        print(np.dot(Q, R))
        print("\n----------------")

    return Q, R


def ex3_first(A_param, b_param, householder):
    if householder:
        Q_local, R_local = ex2(A_param, log=False)
    else:
        Q_local, R_local = np.linalg.qr(A_param)

    return solve_linear_system(Q_local, R_local, b_param)


def ex3():
    print("Exercitiu 3:\n")
    print("numpy QR:")
    print(x_QR)
    print("householder QR:")
    print(x_householder)
    calculate_and_print_norm(x_QR - x_householder, "x_QR - x_householder")
    print("\n----------------")


def ex4():
    print("Exercitiu 4:\n")

    calculate_and_print_norm(A @ x_householder - b, "A*x_householder - b")
    calculate_and_print_norm(A @ x_QR - b, "A*x_QR - b")
    calculate_and_print_norm((x_householder - s) / np.linalg.norm(s), "(x_householder-s)/(norma euclidiana a lui s)")
    calculate_and_print_norm((x_QR - s) / np.linalg.norm(s), "(x_QR - s)/(norma euclidiana a lui s)")

    print("\n----------------")


def ex5():
    print("Exercitiu 5:\n")
    A_inv_householder = calculate_matrix_inverse(Q, R)
    A_inv_numpy = np.linalg.inv(A)

    calculate_and_print_norm(A_inv_householder - A_inv_numpy, "A_inv_householder - A_inv_numpy", ordin=np.inf)
    print("\n----------------")


def householder_qr(A):
    n = len(A)
    R = np.copy(A).astype(float)
    Q = np.eye(n)

    for r in range(n - 1):
        sigma = np.sum(R[r:, r] ** 2)
        if sigma <= epsilon:
            break
        k = np.sqrt(sigma)
        if R[r, r] > 0:
            k = -k
        beta = sigma - k * R[r, r]
        u = np.zeros(n)
        u[r] = R[r, r] - k
        u[r + 1:] = R[r + 1:, r]

        for j in range(r, n):
            gamma = np.sum(u[r:] * R[r:, j]) / beta
            R[r:, j] -= gamma * u[r:]

        for j in range(n):
            gamma = np.sum(u * Q[:, j]) / beta
            Q[:, j] -= gamma * u

    return Q.T, R


def solve_linear_system(Q, R, b):
    Qt_b = np.dot(Q.T, b)

    n = len(b)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = (Qt_b[i] - np.dot(R[i, i + 1:], x[i + 1:])) / R[i, i]

    return x


def calculate_and_print_norm(val, str, ordin=2):
    type = "absoluta"
    if ordin == 2:
        type = "euclidiana"

    print(f"Norma {type} {str} = {np.linalg.norm(val, ord=ordin)}")


def calculate_matrix_inverse(Q, R):
    R_inv = np.linalg.inv(R)
    A_inv = np.dot(R_inv, Q.T)
    return A_inv


b = ex1(A, s)
Q, R = ex2(A)
x_QR = ex3_first(A, b, householder=False)
x_householder = ex3_first(A, b, householder=True)
ex3()
ex4()
ex5()
