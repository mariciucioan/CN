import numpy as np
import matplotlib.pyplot as plt

def generare_noduri_valori(f, x0, xn, n):
    h = (xn - x0) / n
    noduri = [x0 + i * h for i in range(n+1)]
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
            A[i][j] = sum(x**(i+j) for x in noduri)
        b[i] = sum(valori[k] * noduri[k]**i for k in range(len(noduri)))
    coeficienti = np.linalg.solve(A, b)
    return coeficienti[::-1]

def polinom_Horner(coeficienti, x):
    rezultat = coeficienti[0]
    for coef in coeficienti[1:]:
        rezultat = rezultat * x + coef
    return rezultat

def f(x):
    return x**4 - 12*x**3 + 30*x**2 + 12

x_valori = [0, 1, 2, 3, 4, 5]
f_valori = [f(x) for x in x_valori]

noduri, valori = generare_noduri_valori(f, 0, 5, 5)

x_grafic = np.linspace(0, 5, 1000)
y_f = f(x_grafic)
y_L_n = [interpolare_Newton(x, noduri, valori) for x in x_grafic]
coeficienti = metoda_celor_mai_mici_patrate(noduri, valori, 2)
y_P_m = [polinom_Horner(coeficienti, x) for x in x_grafic]

x_bar = 1.5
f_x_bar = f(x_bar)
L_n_x_bar = interpolare_Newton(x_bar, noduri, valori)
coeficienti = metoda_celor_mai_mici_patrate(noduri, valori, 2)
P_m_x_bar = polinom_Horner(coeficienti, x_bar)

print("Pentru ¯x = 1.5:")
print("f(1.5)   :", f_x_bar)
print("L_n(1.5) :", L_n_x_bar)
print("P_m(1.5) :", P_m_x_bar)

eroare_L_n = abs(L_n_x_bar - f_x_bar)
eroare_P_m = abs(P_m_x_bar - f_x_bar)
suma_eroare_interpolare = sum(abs(polinom_Horner(coeficienti, noduri[i]) - valori[i]) for i in range(len(noduri)))

print("\nErori:")
print("|L_n(¯x) − f(¯x)|:", eroare_L_n)
print("|P_m(¯x) − f(¯x)|:", eroare_P_m)
print("Suma erorilor de interpolare (|P_m(x_i) − y_i)|):", suma_eroare_interpolare)

plt.figure(figsize=(10, 6))
plt.plot(x_grafic, y_f, label="f(x)")
plt.plot(x_grafic, y_L_n, label="L_n(x)")
plt.plot(x_grafic, y_P_m, label="P_m(x)")
plt.scatter(x_valori, f_valori, color='red', label="Noduri de interpolare")
plt.scatter(x_bar, f_x_bar, color='green', label="¯x = 1.5")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Interpolare și aproximare polinomială")
plt.legend()
plt.grid(True)
plt.show()
