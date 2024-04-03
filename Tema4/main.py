from citire_matrice_rara import *
from gauss_seidel import *
from norma import *

base_path = "C:/An3Fac/sem2/numeric calculus/CN/Tema4/4/"

for i in range(1, 6):
    print(f"\n \nTestul pentru matricea a_{i} si b{i}:")
    dimensiune, matrice = citeste_matrice_rara(base_path + "a_" + str(i) + ".txt")
    verifica_diagonala_principala_nenula(matrice)
    dim_v, vector = citeste_vector_liber(base_path + "b_" + str(i) + ".txt")

    #Varianta 2 vectori
    print("Gauss seidel 2 vectori:")
    sol, iteratii = gauss_seidel(matrice, vector)
    print(f"solutie Gasita in {iteratii} iteratii")
    print("Norma:")
    norma = calculeaza_norma(matrice, sol, vector)
    print(norma)

    #Solutie folosind un singur vector
    print("Varianta cu un singur vector:")
    sol_un_vector, it_unv= gauss_seidel_un_vector(matrice, vector)
    print(f"Gasita in {it_unv} iteratii")
    print("Norma:")
    norma_unvector = norma = calculeaza_norma(matrice, sol_un_vector, vector)
    print(norma_unvector)


#Test singular 
dimensiune, matrice = citeste_matrice_rara("C:/An3Fac/sem2/numeric calculus/CN/Tema4/4/a_1.txt")
# print(matrice[0])
verifica_diagonala_principala_nenula(matrice)
# verifica_diagonala_secundara_nenula(matrice)

# dim2, mat2 = citeste_matrice_rara_varianta2("C:/An3Fac/sem2/numeric calculus/CN/Tema4/4/a_1.txt")
# verifica_diagonala_principala_nenula_varianta2(mat2)
# verifica_diagonala_secundara_nenula_varianta2

dim_v, vector = citeste_vector_liber(("C:/An3Fac/sem2/numeric calculus/CN/Tema4/4/b_1.txt"))
# print("Dimensiunea sistemului:", dim_v)
# print("Vector:")
# print(vector[3])

sol, iteratii = gauss_seidel(matrice, vector)
# print("Solutie:")
# print(sol) 
print(f"solutie Gasita in {iteratii} iteratii")

#Norma:
print("Norma:")
norma = calculeaza_norma(matrice, sol, vector)
print(norma)

#Solutie folosind un singur vector
print("Varianta cu un singur vector:")
sol_un_vector, it_unv= gauss_seidel_un_vector(matrice, vector)
# print("Solutie un vector:")
# print(sol_un_vector) 
print(f"Gasita in {it_unv} iteratii")
print("Norma:")
norma_unvector = norma = calculeaza_norma(matrice, sol_un_vector, vector)
print(norma_unvector)




# print("Solutia sistemului pe var 2:")
# dim2, mat2 = citeste_matrice_rara_varianta2("C:/An3Fac/sem2/numeric calculus/CN/Tema4/4/a_1.txt")
# sol, iteratii = gauss_seidel_varianta2(mat2, vector)
# print(sol)
# print(f"Gasita in {iteratii} iteratii")