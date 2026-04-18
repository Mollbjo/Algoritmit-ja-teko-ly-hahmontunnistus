import math

def get_eigen_jacobi(matrix_data, max_iterations=1000, tolerance=1e-9):
    """
    noutaa eigenarvot ja eigenvektorit matriiseista Jacobi-menetelmällä
    """
    length = len(matrix_data)

    L = [[matrix_data[i][j] for j in range (length)] for i in range (length)]

    eigenvectors = [[0.0 for i in range(length)] for i in range(length)]
    for i in range(length):
        eigenvectors[i][i] = 1.0

    for iteration in range(max_iterations):
        
        max_value = 0.0
        p = 0
        q = 0
        for i in range(length):
            for j in range(i + 1, length):
                if abs(L[i][j]) > abs(max_value):
                    max_value = abs(L[i][j])
                    p = i
                    q = j
        
        if max_value < tolerance:
            break

        if L[p][p] == L[q][q]:
            theta = math.pi / 4
            if L[p][q] < 0:
                theta = -theta
        else:
            theta = 0.5 * math.atan2(2 * L[p][q], L[p][p] - L[q][q])

        cosin = math.cos(theta)
        sin = math.sin(theta)

        # 1. Tallenna vanhat arvot väliaikaisesti
        L_pp = L[p][p]
        L_qq = L[q][q]
        L_pq = L[p][q]

        # 2. Käytä laskennassa vanhoja (tallennettuja) arvoja
        L[p][p] = cosin**2 * L_pp + sin**2 * L_qq + 2 * cosin * sin * L_pq
        L[q][q] = sin**2 * L_pp + cosin**2 * L_qq - 2 * cosin * sin * L_pq
        L[p][q] = 0.0
        L[q][p] = 0.0

        for i in range(length):
            if i != p and i != q:
                # Tallenna vanhat arvot
                L_ip = L[i][p]
                L_iq = L[i][q]
                
                L[i][p] = cosin * L_ip + sin * L_iq
                L[i][q] = -sin * L_ip + cosin * L_iq
                L[p][i] = L[i][p]
                L[q][i] = L[i][q]

        for i in range(length):
            # Tallenna vanhat vektorien arvot!
            V_ip = eigenvectors[i][p]
            V_iq = eigenvectors[i][q]
            
            eigenvectors[i][p] = cosin * V_ip + sin * V_iq
            eigenvectors[i][q] = -sin * V_ip + cosin * V_iq

    eigenvalues = [L[i][i] for i in range(length)]

    return eigenvalues, eigenvectors

