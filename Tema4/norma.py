import math

def inmultire_matrice_vector(matrice_rara, xGS, dim_vector):
    rezultat = [0] * dim_vector

    for i, linie in enumerate(matrice_rara):
        for val, indice_coloana in linie:
            rezultat[i] += val * xGS[indice_coloana]
    return rezultat

def norma(vector):
    suma_patrate = math.fsum(x ** 2 for x in vector)
    return math.sqrt(suma_patrate)

def calcul_norma_normalizat(vector):
    max_val = max(abs(x) for x in vector)
    vector_norm = [x / max_val for x in vector]
    suma_patrate = math.fsum(x ** 2 for x in vector_norm)
    return max_val * math.sqrt(suma_patrate)

def calculeaza_norma(matrice_rara, xGS, b):
    AxGs = inmultire_matrice_vector(matrice_rara, xGS, len(b))
    diff = [x - y for x, y in zip(AxGs, b)]
    return calcul_norma_normalizat(diff)


#TEST
# A = [
#     [(3.25, 0)],  
#     [(1.0, 0), (2.3, 1), (3.0, 2)],
#     [(3.2, 1), (2.1, 2)]
# ]  
# xGS = [2, 3, 1]  

# rezultat = inmultire_matrice_vector(A, xGS)
# print("Rezultatul înmulțirii matricei rare cu vectorul xGS:", rezultat)
