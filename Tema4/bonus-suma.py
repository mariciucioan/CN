from citire_matrice_rara import *

epsilon_error = 1e-6

def suma_matricelor_rare(matrice1, matrice2):
    suma = []
    for i, linie in enumerate(matrice1):
        linie_suma = []
       
        coloane_adaugate = set()

        for valoare1, coloana1 in linie:
            valoare2 = 0.0
   
            for val2, col2 in matrice2[i]:
                if col2 == coloana1:
                    valoare2 = val2
                    break

            valoare_suma = valoare1 + valoare2
            if abs(valoare_suma) < epsilon_error:
                linie_suma.append((valoare_suma, coloana1))
            coloane_adaugate.add(coloana1)

        for valoare2, coloana2 in matrice2[i]:
            if coloana2 not in coloane_adaugate:
                linie_suma.append((valoare2, coloana2))
        

        suma.append(linie_suma)

    return suma

_, matrice_a = citeste_matrice_rara("C:/An3Fac/sem2/numeric calculus/CN/Tema4/4/a.txt")
_, matrice_b = citeste_matrice_rara("C:/An3Fac/sem2/numeric calculus/CN/Tema4/4/b.txt")
_, matrice_aplusb = citeste_matrice_rara("C:/An3Fac/sem2/numeric calculus/CN/Tema4/4/aplusb.txt")

suma = suma_matricelor_rare(matrice_a, matrice_b)


def verifica_egalitate(suma, matrice_aplusb, epsilon_error):
    for i in range(len(suma)):
        for j in range(len(suma[i])):
            if matrice_aplusb[i][j][1] == suma[i][j][1] and abs(suma[i][j][0] - matrice_aplusb[i][j][0]) >= epsilon_error:
                print(f"linia {i} coloana {j} diff: val suma -> {suma[i][j][0]} diferit de aplusb -> {matrice_aplusb[i][j][0]}")
                return False
    return True

egalitate = verifica_egalitate(suma, matrice_aplusb, epsilon_error)
print("Suma matricelor a și b este egală cu matricea din fișierul aplusb.txt:", egalitate)