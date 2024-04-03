from norma import *
def gauss_seidel(A, b, epsilon=1e-6, kmax=10000):
    n = len(b)
    xc = [0.0] * n 
    xp = [0.0] * n  
    
    k = 0
    while k < kmax:
        xp = xc[:]
        for i in range(n):
            sum_ = 0
            for val, j in A[i]: 
                if j != i:
                    sum_ += val * xc[j]
                else:
                    elem_diag = val
            xc[i] = (b[i] - sum_) / elem_diag
        
        # Calculul normei ||xc - xp||
        delta_x = max(abs(xc[i] - xp[i]) for i in range(n))
        
        if delta_x < epsilon:
            return xc, k  
        
        k += 1
    
    return xc, k 

def gauss_seidel_varianta2(A, b, epsilon=1e-6, kmax=10000):
    n = len(b)
    xc = [0.0] * n 
    xp = [0.0] * n  
    
    k = 0
    while k < kmax:
        xp = xc[:]
       
        for i in range(n):
            sum_ = 0  
            elem_diag = None 
            for val, _, coloana in A: 
                if coloana != i:
                    sum_ += val * xc[coloana]
                else:
                    elem_diag = val
            xc[i] = (b[i] - sum_) / elem_diag
        
        # Calculul normei ||xc - xp||
        delta_x = max(abs(xc[i] - xp[i]) for i in range(n))
        
        if delta_x < epsilon:
            return xc, k  
        
        k += 1
    
    return xc, k


def gauss_seidel_un_vector(A, b, epsilon=1e-6, kmax=10000):
    n = len(b)
    xGS = [0.0] * n  
    
    k = 0
    while k < kmax:
        delta_ant = norma(xGS)
        for i in range(n):
            sum_ = 0
            for val, j in A[i]: 
                if j != i:
                    sum_ += val * xGS[j]
                else:
                    elem_diag = val
            xGS[i] = (b[i] - sum_) / elem_diag
            
        delta_x = norma(xGS)
        if abs(delta_x - delta_ant) < epsilon:
            return xGS, k
        
        k += 1
    
    return xGS, k



# A = [(4, 0, 0), (-1, 1, 1), (2, 2, 2)]
# b = [5, 5, 5]
# sol, nr_iteratii = gauss_seidel_varianta2(A, b)
# print("Soluție aproximată:", sol)
# print("Numărul de iterații:", nr_iteratii)