import math
from . import Matrix

def normalize_eigenfaces(U_matrix):
    """
    Normalisoi matriisin jokaisen sarakkeen (ominaiskasvon) yksikköpituuteen 1,0.
    """
    rows = U_matrix.rows
    cols = U_matrix.columns
    
    normalized_U = Matrix.Matrix(rows, cols)
    
    for j in range(cols):
        magnitude_sq = 0.0
        for i in range(rows):
            magnitude_sq += U_matrix.data[i][j] ** 2
            
        magnitude = math.sqrt(magnitude_sq)
        
        if magnitude > 0:
            for i in range(rows):
                normalized_U.data[i][j] = U_matrix.data[i][j] / magnitude
        else:
            for i in range(rows):
                normalized_U.data[i][j] = 0.0
                
    return normalized_U