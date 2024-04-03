#citire matrice rara - varianta 1, vecotr de vectori
def citeste_matrice_rara(nume_fisier):
    matrice_rara = []
    with open(nume_fisier, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        for _ in range(n):
            matrice_rara.append([])
        for line in lines[1:]:
            if line.strip():
                elements = line.strip().split(',')
                elements = [string.replace(' ', '') for string in elements]
                valoare = float(elements[0])
                indice_linie = int(elements[1])
                indice_coloana = int(elements[2])
                for i in range(len(matrice_rara[indice_linie])):
                        if matrice_rara[indice_linie][i][1] == indice_coloana:
                            matrice_rara[indice_linie][i] = (matrice_rara[indice_linie][i][0] + valoare, indice_coloana)
                            # print(f"Am gasit val pt aceeasi linie si coloana: {indice_linie} {indice_coloana}, noua valoare: {matrice_rara[indice_linie][i]}")
                else:
                    matrice_rara[indice_linie].append((valoare, indice_coloana))
    return n, matrice_rara

def verifica_diagonala_principala_nenula(matrice):
    for i in range(len(matrice)):
        for valoare, indice_coloana in matrice[i]:
            if indice_coloana == i:
                if valoare == 0:
                    print(f"Elementul de pe diagonală de la linia {i} este nul.")
                    return False    
    print("Nu au fost gasite elemente pe diagonala principala cu valoarea 0")
    return True

def verifica_diagonala_secundara_nenula(matrice):
    n = len(matrice)
    for i in range(n):
        for valoare, indice_coloana in matrice[i]:
            if indice_coloana == n - i - 1:
                if valoare == 0:
                    print(f"Elementul de pe diagonală de la linia {i} este nul.")
                    return False    
    print("Nu au fost gasite elemente pe diagonala secundara cu valoarea 0")
    return True

#citire matrice rara - varianta 2 (triplet valoare-linie-coloana)
def citeste_matrice_rara_varianta2(nume_fisier):
    matrice_rara = []
    with open(nume_fisier, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        for line in lines[1:]:
            if line.strip():
                elements = line.strip().split(',')
                elements = [string.replace(' ', '') for string in elements]
                valoare = float(elements[0])
                indice_linie = int(elements[1])
                indice_coloana = int(elements[2])
                for i in range(len(matrice_rara)):
                        if matrice_rara[i][1] == indice_linie and matrice_rara[i][2] == indice_coloana:
                            matrice_rara[i] = (matrice_rara[i][0] + valoare, indice_linie, indice_coloana)
                else:
                    matrice_rara.append((valoare, indice_linie, indice_coloana))
    return n, matrice_rara

def verifica_diagonala_principala_nenula_varianta2(matrice):
    for valoare, indice_linie, indice_coloana in matrice:
        if indice_coloana == indice_linie:
            if valoare == 0:
                print(f"Elementul de pe diagonală de la linia - coloana {indice_linie} este nul.")
                return False    
    print("Nu au fost gasite elemente pe diagonala principala cu valoarea 0")
    return True

def verifica_diagonala_secundara_nenula_varianta2(matrice, dim):
    for i in range(dim):
        for valoare, indice_linie, indice_coloana in matrice:
            if indice_linie == i and indice_coloana == dim - i - 1:
                if valoare == 0:
                    print(f"Elementul de pe diagonală de la linia {i} este nul.")
                    return False    
    print("Nu au fost gasite elemente pe diagonala secundara cu valoarea 0")
    return True



def citeste_vector_liber(nume_fisier):
    vector_liber = []
    with open(nume_fisier, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        for line in lines[1:]:
            if line.strip():
                vector_liber.append(float(line.strip()))
    return n, vector_liber


