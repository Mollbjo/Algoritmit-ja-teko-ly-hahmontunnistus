from . import Matrix
from . import distance

def calculate_reconstruction_error(original_phi_vector, signature_vector, U_k_matrix):
    """
    Laskee, kuinka hyvin Eigenfaces pystyy rekonstruoimaan annetun kuvan.
    Suuri virhe tarkoittaa, että kuva ei todennäköisesti ole ihmiskasvot.
    """
    # 1. Muunna allekirjoituslista Matrix-sarakkeeksi (K x 1)
    k = len(signature_vector)
    omega_matrix = Matrix.Matrix(k, 1)
    for i in range(k):
        omega_matrix.data[i][0] = signature_vector[i]
        
    # 2. Rekonstruoi keskiarvosta vähennetty kasvokuva (U_k * Omega)
    # U_k on 10304 x K. Omega on K x 1. Tulos on 10304 x 1.
    reconstructed_matrix = U_k_matrix.dot(omega_matrix)
    
    # Poimi takaisin tavalliseksi 1D-listaksi
    reconstructed_phi = [reconstructed_matrix.data[i][0] for i in range(reconstructed_matrix.rows)]
    
    # 3. Laske euklidinen etäisyys alkuperäisen ja rekonstruoidun Phi:n välillä
    error = distance.euclidean_distance(original_phi_vector, reconstructed_phi)
    
    return error