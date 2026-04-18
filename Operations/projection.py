from . import Matrix

def get_top_k_eigenfaces(normalized_U_matrix, k):
    """
    Slices the normalized Eigenface matrix to keep only the top K columns.
    """
    rows = normalized_U_matrix.rows
    
    if k > normalized_U_matrix.columns:
        k = normalized_U_matrix.columns
        
    U_k = Matrix.Matrix(rows, k)
    
    for i in range(rows):
        for j in range(k):
            U_k.data[i][j] = normalized_U_matrix.data[i][j]
            
    return U_k

def project_faces(U_k_matrix, mean_subtracted_matrix):
    """
    Projisoi opetuskuvat, joista on vähennetty keskiarvo, kasvoavaruuteen. Palauttaa matriisin, jonka jokainen sarake edustaa yksittäisen opetuskuvan painoja.
    """
    U_k_transposed = U_k_matrix.transpose()
    
    weights_matrix = U_k_transposed.dot(mean_subtracted_matrix)
    
    return weights_matrix

def extract_labeled_signatures(weights_matrix, images_per_person=7):
    """
    Muuntaa painomatriisin listaksi monikkoja (tuple): (signature_vector, subject_id). Tässä oletetaan, että opetusdata oli järjestetty peräkkäin kohteittain.
    """
    num_signatures = weights_matrix.columns
    k_dimensions = weights_matrix.rows
    
    labeled_signatures = []
    
    for j in range(num_signatures):
        signature = [weights_matrix.data[i][j] for i in range(k_dimensions)]
        
        subject_id = (j // images_per_person) + 1
        
        labeled_signatures.append((signature, subject_id))
        
    return labeled_signatures