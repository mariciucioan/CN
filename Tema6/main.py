import numpy as np


def generare_noduri_valori(f, x0, xn, n):
    h = (xn - x0) / n

    noduri = [x0 + i * h for i in range(n + 1)]

    valori = [f(x) for x in noduri]

    return noduri, valori


def interpolare_Newton(x, noduri, valori):
    n = len(noduri)
    F = [[None] * n for _ in range(n)]
    for i in range(n):
        F[i][0] = valori[i]

    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (noduri[i + j] - noduri[i])

    L_n_x = F[0][0]
    for i in range(1, n):
        term = F[0][i]
        for j in range(i):
            term *= (x - noduri[j])
        L_n_x += term

    return L_n_x


def aitken_schema(x, noduri, valori):
    n = len(noduri)
    p = [[None] * n for _ in range(n)]

    for i in range(n):
        p[i][0] = valori[i]

    for j in range(1, n):
        for i in range(n - j):
            p[i][j] = p[i][j - 1] + (x - noduri[i]) / (noduri[i + j] - noduri[i]) * (p[i + 1][j - 1] - p[i][j - 1])

    return p[0][-1]


def metoda_celor_mai_mici_patrate(noduri, valori, m):
    A = np.zeros((m + 1, m + 1))
    b = np.zeros(m + 1)

    for i in range(m + 1):
        for j in range(m + 1):
            A[i][j] = sum(x ** (i + j) for x in noduri)
        b[i] = sum(valori[k] * noduri[k] ** i for k in range(len(noduri)))

    coeficienti = np.linalg.solve(A, b)
    return coeficienti[::-1]


def polinom_Horner(coeficienti, x):
    rezultat = coeficienti[0]
    for coef in coeficienti[1:]:
        rezultat = rezultat * x + coef
    return rezultat


def f(x):
    return x ** 4 - 12 * x ** 3 + 30 * x ** 2 + 12


x_valori = [0, 1, 2, 3, 4, 5]
f_valori = [50, 47, -2, -121, -310, -545]

print("x   :", x_valori)
print("f(x):", f_valori)

noduri, valori = generare_noduri_valori(f, 1, 5, 5)

x_bar = 1.5
L_n_x = interpolare_Newton(x_bar, noduri, valori)
print("\nL_n(¯x):", L_n_x)
print("|L_n(¯x) − f(¯x)|:", abs(L_n_x - f(x_bar)))

print("\nAproximare folosind schema lui Aitken:", aitken_schema(x_bar, noduri, valori))

m = 2
coeficienti = metoda_celor_mai_mici_patrate(noduri, valori, m)
print("\nCoeficienții polinomului:", coeficienti)

P_m_x = polinom_Horner(coeficienti, x_bar)
print("P_m(¯x):", P_m_x)
print("|P_m(¯x) − f(¯x)|:", abs(P_m_x - f(x_bar)))
suma_erori = sum(abs(polinom_Horner(coeficienti, noduri[i]) - valori[i]) for i in range(len(noduri)))
print("Suma erorilor de interpolare:", suma_erori)
