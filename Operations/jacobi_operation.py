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

        L[p][p] = cosin**2 * L[p][p] + sin**2 * L[q][q] + 2 * cosin * sin * L[p][q]
        L[q][q] = sin**2 * L[p][p] + cosin**2 * L[q][q] - 2 * cosin * sin * L[p][q]
        L[p][q] = 0.0
        L[q][p] = 0.0

        for i in range(length):
            if i != p and i != q:
                L[i][p] = cosin * L[i][p] + sin * L[i][q]
                L[i][q] = -sin * L[i][p] + cosin * L[i][q]
                L[p][i] = L[i][p]
                L[q][i] = L[i][q]

        for i in range(length):
            eigenvectors[i][p] = cosin * eigenvectors[i][p] + sin * eigenvectors[i][q]
            eigenvectors[i][q] = -sin * eigenvectors[i][p] + cosin * eigenvectors[i][q]

    eigenvalues = [L[i][i] for i in range(length)]

    return eigenvalues, eigenvectors

