def sort_eigenpairs(eigenvalues, eigenvectors):
    """
    Yhdistää ominaisarvot niitä vastaaviin ominaisvektorisarakkeisiin, lajittelee ne suurimmasta pienimpään ja palauttaa lajitellut listat.
    """
    n = len(eigenvalues)
    pairs = []
    
    for j in range(n):
        vector = [eigenvectors[i][j] for i in range(n)]
        pairs.append((eigenvalues[j], vector))
        
    pairs.sort(key=lambda x: x[0], reverse=True)
    
    sorted_eigenvalues = [pair[0] for pair in pairs]
    
    sorted_eigenvectors = [[0.0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        vector = pairs[j][1]
        for i in range(n):
            sorted_eigenvectors[i][j] = vector[i]
            
    return sorted_eigenvalues, sorted_eigenvectors